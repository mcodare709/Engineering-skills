from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
SKILL_DIR = SKILLS_ROOT / "study-work"
SKILL_FILE = SKILL_DIR / "SKILL.md"
WEB_FILE = ROOT / "web" / "study-work.md"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CJK_PATTERN = re.compile(r"[\u3400-\u9fff]")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".txt", ".toml"}
REQUIRED_REFERENCES = {
    "caveman.md",
    "context-engineering.md",
    "training.md",
    "debug.md",
    "deployment.md",
    "defect-detection.md",
    "research.md",
    "reporting.md",
    "code-rules.md",
}
REQUIRED_EVALS = {"trigger-cases.yaml", "output-cases.yaml"}
FORBIDDEN_LEGACY_PATHS = {
    SKILLS_ROOT / "caveman",
    ROOT / "web" / "caveman.md",
    ROOT / "evals" / "caveman-trigger-cases.yaml",
    ROOT / "evals" / "caveman-output-cases.yaml",
}


def frontmatter(text: str) -> tuple[dict[str, str], str, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter.")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter is not closed.") from exc

    header = lines[1:end]
    data: dict[str, str] = {}
    key: str | None = None
    folded: list[str] = []

    def flush() -> None:
        nonlocal key, folded
        if key and folded:
            data[key] = " ".join(line.strip() for line in folded)
        key = None
        folded = []

    for line in header:
        if line.startswith("  ") and key:
            folded.append(line)
            continue
        flush()
        if ":" not in line:
            continue
        current, value = line.split(":", 1)
        current = current.strip()
        value = value.strip()
        if value in {">", "|"}:
            key = current
        elif value:
            data[current] = value.strip("\"'")
    flush()
    return data, "\n".join(lines[end + 1 :]), header


def validate_markdown_links() -> list[str]:
    errors: list[str] = []
    for markdown in SKILL_DIR.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for link in LINK_PATTERN.findall(text):
            clean = link.split("#", 1)[0].strip()
            if not clean or clean.startswith(("http://", "https://", "#")):
                continue
            target = (markdown.parent / clean).resolve()
            try:
                target.relative_to(SKILL_DIR.resolve())
            except ValueError:
                errors.append(f"Link escapes skill directory: {markdown.relative_to(ROOT)} -> {link}")
                continue
            if not target.exists():
                errors.append(f"Broken link: {markdown.relative_to(ROOT)} -> {link}")
    return errors


def validate_english() -> list[str]:
    errors: list[str] = []
    roots = [
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        SKILLS_ROOT,
        ROOT / "web",
        ROOT / "evals",
        ROOT / "scripts",
        ROOT / ".github",
    ]
    paths: list[Path] = []
    for item in roots:
        if item.is_file():
            paths.append(item)
        elif item.exists():
            paths.extend(path for path in item.rglob("*") if path.is_file())
    for path in paths:
        if path.suffix.lower() in TEXT_SUFFIXES and CJK_PATTERN.search(path.read_text(encoding="utf-8")):
            errors.append(f"Non-English CJK text found: {path.relative_to(ROOT)}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []

    if not SKILL_FILE.is_file():
        return ["Missing skills/study-work/SKILL.md"]

    extra_skills = sorted(
        path.name for path in SKILLS_ROOT.iterdir() if path.is_dir() and path.name != SKILL_DIR.name
    )
    if extra_skills:
        errors.append(f"Only study-work may exist under skills/: {', '.join(extra_skills)}")

    for path in sorted(FORBIDDEN_LEGACY_PATHS):
        if path.exists():
            errors.append(f"Forbidden standalone Caveman artifact: {path.relative_to(ROOT)}")

    if (SKILL_DIR / "skill.md").exists():
        errors.append("Lowercase skill.md must not exist.")

    try:
        metadata, body, header = frontmatter(SKILL_FILE.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [str(exc)]

    for field in ("name", "description"):
        if not metadata.get(field):
            errors.append(f"Missing frontmatter field: {field}")

    name = metadata.get("name", "")
    if name and not NAME_PATTERN.fullmatch(name):
        errors.append("Skill name must use lowercase kebab-case.")
    if name and name != SKILL_DIR.name:
        errors.append("Skill directory must match frontmatter name.")
    if len(metadata.get("description", "")) > 1024:
        errors.append("Description exceeds 1024 characters.")
    if not body.strip():
        errors.append("SKILL.md body is empty.")

    if any(line.strip().startswith("metadata:") for line in header):
        errors.append("SKILL.md frontmatter must not contain metadata block.")
    if any(re.match(r"^\s*version\s*:", line) for line in header):
        errors.append("SKILL.md frontmatter must not contain version.")

    references = SKILL_DIR / "references"
    present = {path.name for path in references.glob("*.md")} if references.exists() else set()
    for missing in sorted(REQUIRED_REFERENCES - present):
        errors.append(f"Missing reference: {missing}")

    errors.extend(validate_markdown_links())

    if not WEB_FILE.is_file() or not WEB_FILE.read_text(encoding="utf-8").strip():
        errors.append("Missing web/study-work.md")

    for filename in sorted(REQUIRED_EVALS):
        eval_file = ROOT / "evals" / filename
        if not eval_file.is_file() or not eval_file.read_text(encoding="utf-8").strip():
            errors.append(f"Missing eval file: {eval_file.relative_to(ROOT)}")
        elif "skill: study-work" not in eval_file.read_text(encoding="utf-8"):
            errors.append(f"Eval must target study-work: {eval_file.relative_to(ROOT)}")

    if (ROOT / "docs" / "images").exists() or (ROOT / "pit").exists():
        errors.append("Image documentation directories must not exist.")

    image_suffixes = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in image_suffixes:
            errors.append(f"Image file not allowed: {path.relative_to(ROOT)}")
    if any(SKILLS_ROOT.glob("*.zip")):
        errors.append("Generated ZIP must not be committed under skills/.")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required_readme = (
        "$study-work",
        "skills/study-work",
        "references/caveman.md",
        "web/study-work.md",
        "python scripts/install_skill.py --client all --scope user",
    )
    for token in required_readme:
        if token not in readme:
            errors.append(f"README missing required token: {token}")

    forbidden_readme = (
        "$caveman",
        "Engineering-skills/tree/main/skills/caveman",
        "web/caveman.md",
        "--skill",
    )
    for token in forbidden_readme:
        if token in readme:
            errors.append(f"README contains standalone Caveman/multi-skill token: {token}")

    errors.extend(validate_english())
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
