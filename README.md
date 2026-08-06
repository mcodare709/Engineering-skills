# Engineering Research Skill

Portable Agent Skill for AI/ML research and engineering.

One canonical skill. Same content for Codex, Claude Code, Antigravity IDE, and Cursor. A self-contained web prompt is included for browser-based assistants.

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

Clone or download this repository:

```bash
git clone https://github.com/mcodare709/Engineering-research-skills.git
cd Engineering-research-skills
```

Run the cross-platform installer:

```bash
python scripts/install_skill.py --client codex --scope user
python scripts/install_skill.py --client claude --scope user
python scripts/install_skill.py --client antigravity --scope user
python scripts/install_skill.py --client cursor --scope user
```

Install for every supported local client:

```bash
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
| Codex | `.agents/skills/engineering-research/` | `~/.agents/skills/engineering-research/` |
| Claude Code | `.claude/skills/engineering-research/` | `~/.claude/skills/engineering-research/` |
| Antigravity IDE | `.agents/skills/engineering-research/` | `~/.gemini/config/skills/engineering-research/` |
| Cursor | `.cursor/skills/engineering-research/` | `~/.cursor/skills/engineering-research/` |

Codex and Antigravity share the project-level `.agents/skills/` path.

## Web Version

Open [`web/engineering-research.md`](web/engineering-research.md). Copy the full file into a system prompt, project instruction, custom instruction, or persistent chat instruction.

The web version is self-contained. It does not require reference-file loading.

## Build Downloads

```bash
python scripts/build.py
```

Outputs:

```text
dist/engineering-research-skill.zip
dist/engineering-research-web.md
dist/engineering-research-public.zip
```

`engineering-research-public.zip` contains both local Agent Skill and web prompt.

## Validate

```bash
python scripts/validate_skill.py
```

Validation checks:

- Exact `SKILL.md` casing
- Required frontmatter and references
- Broken relative links
- English-only repository content
- No image documentation
- Web prompt presence
- Eval presence
- No committed generated ZIP

## Structure

```text
.
├── README.md
├── CHANGELOG.md
├── LICENSE
├── evals/
├── scripts/
│   ├── build.py
│   ├── install_skill.py
│   └── validate_skill.py
├── skills/
│   └── engineering-research/
│       ├── SKILL.md
│       └── references/
└── web/
    └── engineering-research.md
```

## License

MIT.
