from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
WEB_ROOT = ROOT / "web"
DIST = ROOT / "dist"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def add_file(archive: zipfile.ZipFile, source: Path, target: Path) -> None:
    info = zipfile.ZipInfo(target.as_posix(), FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, source.read_bytes())


def skill_dirs() -> list[Path]:
    return sorted(path for path in SKILLS_ROOT.iterdir() if (path / "SKILL.md").is_file())


def skill_files(skill_dir: Path):
    for path in sorted(skill_dir.rglob("*")):
        if path.is_file() and not path.name.startswith("."):
            yield path


def build_skill_zip(skill_dir: Path, output: Path) -> None:
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in skill_files(skill_dir):
            add_file(archive, source, Path(skill_dir.name) / source.relative_to(skill_dir))


def build_public_zip(skill_dir: Path, web_file: Path, output: Path) -> None:
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in skill_files(skill_dir):
            add_file(archive, source, Path("local") / skill_dir.name / source.relative_to(skill_dir))
        add_file(archive, web_file, Path("web") / web_file.name)
        add_file(archive, ROOT / "README.md", Path("README.md"))
        add_file(archive, ROOT / "LICENSE", Path("LICENSE"))


def main() -> int:
    skills = skill_dirs()
    if not skills:
        raise FileNotFoundError(f"No skills found under {SKILLS_ROOT}")

    DIST.mkdir(parents=True, exist_ok=True)
    for skill_dir in skills:
        name = skill_dir.name
        web_file = WEB_ROOT / f"{name}.md"
        if not web_file.is_file():
            raise FileNotFoundError(f"Missing {web_file}")

        build_skill_zip(skill_dir, DIST / f"{name}-skill.zip")
        shutil.copy2(web_file, DIST / f"{name}-web.md")
        build_public_zip(skill_dir, web_file, DIST / f"{name}-public.zip")

    for path in sorted(DIST.iterdir()):
        print(f"Created: {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
