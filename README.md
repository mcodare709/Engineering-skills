# Engineering Skills

**English** | [Traditional Chinese](README.zh-TW.md)

Portable Agent Skill for AI/ML research, engineering, and token-efficient technical output.

One canonical `study-work` skill for Codex, Claude Code, Antigravity IDE, Cursor, and browser assistants.

> This reflects my personal workflow preferences; adjust as needed.

## Skill

### `study-work`

Research-grade AI/ML engineering workflow for:

- Model training and debugging
- Computer vision and image enhancement
- Industrial defect and anomaly detection
- Experiment design, paper review, and ablation planning
- ONNX, TensorRT, Jetson, latency, and production inference
- Technical reports and experiment records
- Long-session context compaction
- Token-efficient technical output using the Caveman reporting method

Skill: [study-work](https://github.com/mcodare709/Engineering-skills/tree/main/skills/study-work "study-work")

Caveman is not a separate skill in this repository. Its output method is integrated as [`references/caveman.md`](skills/study-work/references/caveman.md).

Codex:

```text
$study-work diagnose why training loss falls while validation loss rises
```

## Install

```bash
git clone https://github.com/mcodare709/Engineering-skills.git
cd Engineering-skills
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

Validation checks the single-skill layout, metadata, local links, required references, web prompt, eval files, English-only project text, and forbidden legacy artifacts.

## Structure

```text
.
├── README.md
├── README.zh-TW.md
├── CHANGELOG.md
├── LICENSE
├── evals/
│   ├── trigger-cases.yaml
│   └── output-cases.yaml
├── scripts/
├── skills/
│   └── study-work/
│       ├── SKILL.md
│       └── references/
│           └── caveman.md
└── web/
    └── study-work.md
```

## License

MIT.

### If u like, get me the star.

## Credits

Caveman reporting method: [caveman](https://github.com/mcodare709/subagent/tree/main/.agents/skills/caveman "caveman"). It favors terse, technically accurate output to reduce report/output tokens where clarity remains intact.
