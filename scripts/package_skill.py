from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "engineering-research"
OUTPUT = ROOT / "dist" / "engineering-research.zip"
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts and not path.name.startswith("."):
            yield path


def package(skill_dir: Path = SKILL_DIR, output: Path = OUTPUT) -> Path:
    if not (skill_dir / "SKILL.md").is_file():
        raise FileNotFoundError(f"Missing {skill_dir / 'SKILL.md'}")

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in iter_files(skill_dir):
            relative = Path(skill_dir.name) / source.relative_to(skill_dir)
            info = zipfile.ZipInfo(relative.as_posix(), FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, source.read_bytes())
    return output


def main() -> int:
    try:
        output = package()
    except (OSError, zipfile.BadZipFile) as exc:
        print(f"Packaging failed: {exc}", file=sys.stderr)
        return 1
    print(f"Created {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
