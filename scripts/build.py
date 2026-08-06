from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "study-work"
WEB_FILE = ROOT / "web" / "study-work.md"
DIST = ROOT / "dist"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def add_file(archive: zipfile.ZipFile, source: Path, target: Path) -> None:
    info = zipfile.ZipInfo(target.as_posix(), FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, source.read_bytes())


def skill_files():
    for path in sorted(SKILL_DIR.rglob("*")):
        if path.is_file() and not path.name.startswith("."):
            yield path


def build_skill_zip(output: Path) -> None:
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in skill_files():
            add_file(archive, source, Path(SKILL_DIR.name) / source.relative_to(SKILL_DIR))


def build_public_zip(output: Path) -> None:
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in skill_files():
            add_file(archive, source, Path("local") / SKILL_DIR.name / source.relative_to(SKILL_DIR))
        add_file(archive, WEB_FILE, Path("web") / WEB_FILE.name)
        add_file(archive, ROOT / "README.md", Path("README.md"))
        add_file(archive, ROOT / "LICENSE", Path("LICENSE"))


def main() -> int:
    if not (SKILL_DIR / "SKILL.md").is_file():
        raise FileNotFoundError(f"Missing {SKILL_DIR / 'SKILL.md'}")
    if not WEB_FILE.is_file():
        raise FileNotFoundError(f"Missing {WEB_FILE}")

    DIST.mkdir(parents=True, exist_ok=True)
    build_skill_zip(DIST / "study-work-skill.zip")
    shutil.copy2(WEB_FILE, DIST / "study-work-web.md")
    build_public_zip(DIST / "study-work-public.zip")

    for path in sorted(DIST.iterdir()):
        print(f"Created: {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
