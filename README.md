# Engineering Skills

Portable Agent Skills for AI/ML research, engineering, and token-efficient technical output.

One repository for Codex, Claude Code, Antigravity IDE, Cursor, and browser assistants.

## Skills

### `study-work`

Research-grade AI/ML engineering workflow for:

- Model training and debugging
- Computer vision and image enhancement
- Industrial defect and anomaly detection
- Experiment design, paper review, and ablation planning
- ONNX, TensorRT, Jetson, latency, and production inference
- Technical reports and experiment records
- Long-session context compaction

Codex:

```text
$study-work diagnose why training loss falls while validation loss rises
```

### `caveman`

Token-efficient output style. Compresses prose while preserving technical detail, code, commands, API names, paths, parameters, and exact error strings.

Levels: `lite`, `full`, `ultra`.

Codex:

```text
$caveman explain this error
$caveman ultra summarize this result
```

Use `stop caveman` or `normal mode` to return to normal prose.

## Install

Clone:

```bash
git clone https://github.com/mcodare709/Engineering-skills.git
cd Engineering-skills
```

Install all skills for all supported clients:

```bash
python scripts/install_skill.py --skill all --client all --scope user
```

Install one skill:

```bash
python scripts/install_skill.py --skill study-work --client codex --scope user
python scripts/install_skill.py --skill caveman --client codex --scope user
```

Project-scoped install:

```bash
python scripts/install_skill.py --skill all --client all --scope project --project-root .
```

Use `--force` to replace an existing installation.

## Install Locations

| Client | Project | User |
|---|---|---|
| Codex | `.agents/skills/<skill>/` | `~/.agents/skills/<skill>/` |
| Claude Code | `.claude/skills/<skill>/` | `~/.claude/skills/<skill>/` |
| Antigravity IDE | `.agents/skills/<skill>/` | `~/.gemini/config/skills/<skill>/` |
| Cursor | `.cursor/skills/<skill>/` | `~/.cursor/skills/<skill>/` |

Codex and Antigravity share the project-level `.agents/skills/` path.

## Web Versions

- [`web/study-work.md`](web/study-work.md)
- [`web/caveman.md`](web/caveman.md)

Copy the full prompt into system instructions, project instructions, or custom instructions.

## Build Downloads

```bash
python scripts/build.py
```

Outputs:

```text
dist/study-work-skill.zip
dist/study-work-web.md
dist/study-work-public.zip
dist/caveman-skill.zip
dist/caveman-web.md
dist/caveman-public.zip
```

## Validate

```bash
python scripts/validate_skill.py
```

Validation checks skill metadata, local links, required references, web prompts, eval files, English-only project text, and forbidden image artifacts.

## Structure

```text
.
├── README.md
├── CHANGELOG.md
├── LICENSE
├── evals/
│   ├── trigger-cases.yaml
│   ├── output-cases.yaml
│   ├── caveman-trigger-cases.yaml
│   └── caveman-output-cases.yaml
├── scripts/
├── skills/
│   ├── study-work/
│   │   ├── SKILL.md
│   │   └── references/
│   └── caveman/
│       └── SKILL.md
└── web/
    ├── study-work.md
    └── caveman.md
```

## License

MIT.

### If u like, get me the star.

## Credits

Caveman reporting method and skill: [caveman](https://github.com/mcodare709/subagent/blob/main/.agents/skills/caveman/SKILL.md). It favors terse, technically accurate output to reduce report/output tokens where clarity remains intact.
