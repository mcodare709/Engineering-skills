from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "study-work"
SKILL_FILE = SKILL_DIR / "SKILL.md"
WEB_FILE = ROOT / "web" / "study-work.md"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CJK_PATTERN = re.compile(r"[\u3400-\u9fff]")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".txt", ".toml"}
REQUIRED_REFERENCES = {
    "context-engineering.md",
    "training.md",
    "debug.md",
    "deployment.md",
    "defect-detection.md",
    "research.md",
    "reporting.md",
    "code-rules.md",
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


def validate_links(body: str) -> list[str]:
    errors: list[str] = []
    for link in LINK_PATTERN.findall(body):
        if link.startswith(("http://", "https://", "#")):
            continue
        target = (SKILL_DIR / link.split("#", 1)[0]).resolve()
        try:
            target.relative_to(SKILL_DIR.resolve())
        except ValueError:
            errors.append(f"Link escapes skill directory: {link}")
            continue
        if not target.exists():
            errors.append(f"Broken link: {link}")
    return errors


def validate_english() -> list[str]:
    errors: list[str] = []
    roots = [ROOT / "README.md", ROOT / "CHANGELOG.md", ROOT / "skills", ROOT / "web", ROOT / "evals", ROOT / "scripts", ROOT / ".github"]
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
    if (SKILL_DIR / "skill.md").exists():
        errors.append("Lowercase skill.md must not exist.")

    try:
        metadata, body = frontmatter(SKILL_FILE.read_text(encoding="utf-8"))
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

    errors.extend(validate_links(body))
    references = SKILL_DIR / "references"
    present = {path.name for path in references.glob("*.md")} if references.exists() else set()
    for missing in sorted(REQUIRED_REFERENCES - present):
        errors.append(f"Missing reference: {missing}")

    if not WEB_FILE.is_file() or not WEB_FILE.read_text(encoding="utf-8").strip():
        errors.append("Missing web/study-work.md")
    for required in (ROOT / "evals" / "trigger-cases.yaml", ROOT / "evals" / "output-cases.yaml"):
        if not required.is_file() or not required.read_text(encoding="utf-8").strip():
            errors.append(f"Missing eval file: {required.relative_to(ROOT)}")

    if (ROOT / "docs" / "images").exists() or (ROOT / "pit").exists():
        errors.append("Image documentation directories must not exist.")
    image_suffixes = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in image_suffixes:
            errors.append(f"Image file not allowed: {path.relative_to(ROOT)}")
    if any((ROOT / "skills").glob("*.zip")):
        errors.append("Generated ZIP must not be committed under skills/.")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        ".agents/skills/study-work/",
        ".claude/skills/study-work/",
        ".cursor/skills/study-work/",
        ".gemini/config/skills/study-work/",
        "web/study-work.md",
        "$study-work",
    ):
        if token not in readme:
            errors.append(f"README missing install target: {token}")

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
