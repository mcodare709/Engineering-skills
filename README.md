# Study Work Skill

Portable Agent Skill for AI/ML research and engineering.

One canonical skill for Codex, Claude Code, Antigravity IDE, and Cursor. A self-contained web prompt is included for browser assistants.

## Invoke in Codex

Type `$`, then select `study-work`.

Direct invocation:

```text
$study-work <task>
```

Example:

```text
$study-work diagnose why training loss falls while validation loss rises
```

## Scope

Use for:

- Model training and debugging
- Computer vision and image enhancement
- Industrial defect and anomaly detection
- Experiment design, paper review, and ablation planning
- ONNX, TensorRT, Jetson, latency, and production inference
- Technical reports and experiment records
- Long-session context compaction

Do not use for generic programming, routine Git commands, or unrelated writing.

## Install

```bash
git clone https://github.com/mcodare709/Engineering-research-skills.git
cd Engineering-research-skills
python scripts/install_skill.py --client all --scope user
```

Project-scoped install:

```bash
python scripts/install_skill.py --client all --scope project --project-root .
```

Use `--force` to replace an existing installation.

## Install Locations

| Client | Project | User |
|---|---|---|
| Codex | `.agents/skills/study-work/` | `~/.agents/skills/study-work/` |
| Claude Code | `.claude/skills/study-work/` | `~/.claude/skills/study-work/` |
| Antigravity IDE | `.agents/skills/study-work/` | `~/.gemini/config/skills/study-work/` |
| Cursor | `.cursor/skills/study-work/` | `~/.cursor/skills/study-work/` |

Codex and Antigravity share the project-level `.agents/skills/` path.

## Web Version

Open [`web/study-work.md`](web/study-work.md). Copy the full file into system instructions, project instructions, or custom instructions.

## Build Downloads

```bash
python scripts/build.py
```

Outputs:

```text
dist/study-work-skill.zip
dist/study-work-web.md
dist/study-work-public.zip
```

## Validate

```bash
python scripts/validate_skill.py
```

## Structure

```text
.
├── README.md
├── CHANGELOG.md
├── LICENSE
├── evals/
├── scripts/
├── skills/
│   └── study-work/
│       ├── SKILL.md
│       └── references/
└── web/
    └── study-work.md
```

## License

MIT.

### If u like, get me the star.

## Credits

Caveman reporting method and skill: [caveman](https://github.com/mcodare709/subagent/blob/main/.agents/skills/caveman/SKILL.md). It favors terse, technically accurate output to reduce report/output tokens where clarity remains intact.
