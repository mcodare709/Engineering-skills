from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
WEB_ROOT = ROOT / "web"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CJK_PATTERN = re.compile(r"[\u3400-\u9fff]")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".txt", ".toml"}
REQUIRED_REFERENCES = {
    "study-work": {
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
}
REQUIRED_EVALS = {
    "study-work": {"trigger-cases.yaml", "output-cases.yaml"},
    "caveman": {"caveman-trigger-cases.yaml", "caveman-output-cases.yaml"},
}


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter.")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter is not closed.") from exc

    data: dict[str, str] = {}
    key: str | None = None
    folded: list[str] = []

    def flush() -> None:
        nonlocal key, folded
        if key and folded:
            data[key] = " ".join(line.strip() for line in folded)
        key = None
        folded = []

    for line in lines[1:end]:
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
    return data, "\n".join(lines[end + 1 :])


def skill_dirs() -> list[Path]:
    return sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir()) if SKILLS_ROOT.exists() else []


def validate_links(body: str, skill_dir: Path) -> list[str]:
    errors: list[str] = []
    for link in LINK_PATTERN.findall(body):
        if link.startswith(("http://", "https://", "#")):
            continue
        target = (skill_dir / link.split("#", 1)[0]).resolve()
        try:
            target.relative_to(skill_dir.resolve())
        except ValueError:
            errors.append(f"{skill_dir.name}: link escapes skill directory: {link}")
            continue
        if not target.exists():
            errors.append(f"{skill_dir.name}: broken link: {link}")
    return errors


def validate_english() -> list[str]:
    errors: list[str] = []
    roots = [ROOT / "README.md", ROOT / "CHANGELOG.md", SKILLS_ROOT, WEB_ROOT, ROOT / "evals", ROOT / "scripts", ROOT / ".github"]
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


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"Missing {skill_file.relative_to(ROOT)}"]
    if (skill_dir / "skill.md").exists():
        errors.append(f"{skill_dir.name}: lowercase skill.md must not exist.")

    try:
        metadata, body = frontmatter(skill_file.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [f"{skill_dir.name}: {exc}"]

    for field in ("name", "description"):
        if not metadata.get(field):
            errors.append(f"{skill_dir.name}: missing frontmatter field: {field}")
    name = metadata.get("name", "")
    if name and not NAME_PATTERN.fullmatch(name):
        errors.append(f"{skill_dir.name}: skill name must use lowercase kebab-case.")
    if name and name != skill_dir.name:
        errors.append(f"{skill_dir.name}: directory must match frontmatter name.")
    if len(metadata.get("description", "")) > 1024:
        errors.append(f"{skill_dir.name}: description exceeds 1024 characters.")
    if not body.strip():
        errors.append(f"{skill_dir.name}: SKILL.md body is empty.")

    errors.extend(validate_links(body, skill_dir))

    required = REQUIRED_REFERENCES.get(skill_dir.name, set())
    references = skill_dir / "references"
    present = {path.name for path in references.glob("*.md")} if references.exists() else set()
    for missing in sorted(required - present):
        errors.append(f"{skill_dir.name}: missing reference: {missing}")

    web_file = WEB_ROOT / f"{skill_dir.name}.md"
    if not web_file.is_file() or not web_file.read_text(encoding="utf-8").strip():
        errors.append(f"Missing {web_file.relative_to(ROOT)}")

    for filename in sorted(REQUIRED_EVALS.get(skill_dir.name, set())):
        eval_file = ROOT / "evals" / filename
        if not eval_file.is_file() or not eval_file.read_text(encoding="utf-8").strip():
            errors.append(f"{skill_dir.name}: missing eval file: {eval_file.relative_to(ROOT)}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    skills = skill_dirs()
    if not skills:
        return ["No skill directories found under skills/."]

    for skill_dir in skills:
        errors.extend(validate_skill(skill_dir))

    if (ROOT / "docs" / "images").exists() or (ROOT / "pit").exists():
        errors.append("Image documentation directories must not exist.")
    image_suffixes = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in image_suffixes:
            errors.append(f"Image file not allowed: {path.relative_to(ROOT)}")
    if any(SKILLS_ROOT.glob("*.zip")):
        errors.append("Generated ZIP must not be committed under skills/.")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in ("$study-work", "$caveman", "web/study-work.md", "web/caveman.md", "--skill"):
        if token not in readme:
            errors.append(f"README missing required token: {token}")

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
