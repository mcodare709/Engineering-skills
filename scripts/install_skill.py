from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills" / "engineering-research"
SKILL_NAME = SOURCE.name

CLIENT_PATHS = {
    "codex": {
        "project": Path(".agents/skills"),
        "user": Path.home() / ".agents" / "skills",
    },
    "claude": {
        "project": Path(".claude/skills"),
        "user": Path.home() / ".claude" / "skills",
    },
    "antigravity": {
        "project": Path(".agents/skills"),
        "user": Path.home() / ".gemini" / "config" / "skills",
    },
    "cursor": {
        "project": Path(".cursor/skills"),
        "user": Path.home() / ".cursor" / "skills",
    },
}


def clients(value: str) -> list[str]:
    return list(CLIENT_PATHS) if value == "all" else [value]


def targets(client_names: list[str], scope: str, project_root: Path) -> list[Path]:
    found: list[Path] = []
    seen: set[Path] = set()
    for client in client_names:
        base = CLIENT_PATHS[client][scope]
        destination = (project_root / base if scope == "project" else base) / SKILL_NAME
        destination = destination.expanduser().resolve()
        if destination not in seen:
            seen.add(destination)
            found.append(destination)
    return found


def install(destination: Path, force: bool) -> None:
    if destination.exists():
        if not force:
            raise FileExistsError(f"{destination} exists. Use --force to replace it.")
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description="Install engineering-research Agent Skill.")
    parser.add_argument("--client", choices=[*CLIENT_PATHS, "all"], required=True)
    parser.add_argument("--scope", choices=["project", "user"], default="user")
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    if not (SOURCE / "SKILL.md").is_file():
        raise FileNotFoundError(f"Missing source skill: {SOURCE}")

    destinations = targets(clients(args.client), args.scope, args.project_root.resolve())
    for destination in destinations:
        install(destination, args.force)
        print(f"Installed: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
