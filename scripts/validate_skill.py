from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL = ROOT / "skills" / "engineering-research"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")

    try:
        end = lines[1:].index("---") + 1
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc

    data: dict[str, str] = {}
    current_key: str | None = None
    folded: list[str] = []

    def flush() -> None:
        nonlocal current_key, folded
        if current_key is not None and folded:
            data[current_key] = " ".join(part.strip() for part in folded).strip()
        current_key = None
        folded = []

    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  "):
            if current_key is not None:
                folded.append(raw)
            continue
        flush()
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in {">", "|"}:
            current_key = key
            continue
        if value:
            data[key] = value.strip('"\'')
    flush()
    return data, "\n".join(lines[end + 1 :])


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.is_file():
        return [f"Missing required file: {skill_file.relative_to(ROOT)}"]
    if (skill_dir / "skill.md").exists():
        errors.append("Lowercase skill.md must not coexist with SKILL.md")

    try:
        metadata, body = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        return [str(exc)]

    for key in ("name", "description"):
        if not metadata.get(key):
            errors.append(f"Missing frontmatter field: {key}")

    name = metadata.get("name", "")
    if name and not NAME_PATTERN.fullmatch(name):
        errors.append("name must use lowercase kebab-case")
    if name and skill_dir.name != name:
        errors.append(f"Directory name '{skill_dir.name}' must match skill name '{name}'")

    description = metadata.get("description", "")
    if len(description) > 1024:
        errors.append(f"description exceeds 1024 characters: {len(description)}")

    if not body.strip():
        errors.append("SKILL.md body is empty")

    for target in LINK_PATTERN.findall(body):
        if target.startswith(("http://", "https://", "#")):
            continue
        clean_target = target.split("#", 1)[0]
        resolved = (skill_dir / clean_target).resolve()
        try:
            resolved.relative_to(skill_dir.resolve())
        except ValueError:
            errors.append(f"Link escapes skill directory: {target}")
            continue
        if not resolved.exists():
            errors.append(f"Broken relative link: {target}")

    references = skill_dir / "references"
    if not references.is_dir():
        errors.append("Missing references directory")
    else:
        for path in sorted(references.glob("*.md")):
            if not path.read_text(encoding="utf-8").strip():
                errors.append(f"Empty reference file: {path.relative_to(ROOT)}")

    required_references = {
        "training.md",
        "debug.md",
        "deployment.md",
        "defect-detection.md",
        "research.md",
        "reporting.md",
        "code-rules.md",
    }
    existing = {path.name for path in references.glob("*.md")} if references.exists() else set()
    for missing in sorted(required_references - existing):
        errors.append(f"Missing reference file: references/{missing}")

    if any((ROOT / "skills").glob("*.zip")):
        errors.append("Do not commit generated ZIP files under skills/; run package_skill.py")

    for eval_file in (ROOT / "evals" / "trigger-cases.yaml", ROOT / "evals" / "output-cases.yaml"):
        if not eval_file.is_file() or not eval_file.read_text(encoding="utf-8").strip():
            errors.append(f"Missing or empty eval file: {eval_file.relative_to(ROOT)}")

    readme = ROOT / "README.md"
    if readme.is_file():
        readme_text = readme.read_text(encoding="utf-8")
        if "skills/engineering-research/SKILL.md" not in readme_text:
            errors.append("README must reference the exact SKILL.md path")

    return errors


def main() -> int:
    skill_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_SKILL
    errors = validate(skill_dir)
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed: {skill_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
