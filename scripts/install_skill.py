from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

CLIENT_PATHS = {
    "codex": {"project": Path(".agents/skills"), "user": Path.home() / ".agents" / "skills"},
    "claude": {"project": Path(".claude/skills"), "user": Path.home() / ".claude" / "skills"},
    "antigravity": {"project": Path(".agents/skills"), "user": Path.home() / ".gemini" / "config" / "skills"},
    "cursor": {"project": Path(".cursor/skills"), "user": Path.home() / ".cursor" / "skills"},
}


def available_skills() -> list[str]:
    return sorted(path.name for path in SKILLS_ROOT.iterdir() if (path / "SKILL.md").is_file())


def selected_skills(value: str) -> list[str]:
    return available_skills() if value == "all" else [value]


def clients(value: str) -> list[str]:
    return list(CLIENT_PATHS) if value == "all" else [value]


def targets(skill_name: str, client_names: list[str], scope: str, project_root: Path) -> list[Path]:
    found: list[Path] = []
    seen: set[Path] = set()
    for client in client_names:
        base = CLIENT_PATHS[client][scope]
        destination = (project_root / base if scope == "project" else base) / skill_name
        destination = destination.expanduser().resolve()
        if destination not in seen:
            seen.add(destination)
            found.append(destination)
    return found


def install(source: Path, destination: Path, force: bool) -> None:
    if destination.exists():
        if not force:
            raise FileExistsError(f"{destination} exists. Use --force to replace it.")
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)


def main() -> int:
    skills = available_skills()
    if not skills:
        raise FileNotFoundError(f"No skills found under {SKILLS_ROOT}")

    parser = argparse.ArgumentParser(description="Install portable Agent Skills.")
    parser.add_argument("--skill", choices=[*skills, "all"], default="study-work")
    parser.add_argument("--client", choices=[*CLIENT_PATHS, "all"], required=True)
    parser.add_argument("--scope", choices=["project", "user"], default="user")
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    for skill_name in selected_skills(args.skill):
        source = SKILLS_ROOT / skill_name
        for destination in targets(skill_name, clients(args.client), args.scope, project_root):
            install(source, destination, args.force)
            print(f"Installed {skill_name}: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
