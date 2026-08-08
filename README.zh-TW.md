# Engineering Skills

[English](README.md) | **繁體中文**

適用於 AI/ML 研究、工程開發與 token-efficient technical output 的可攜式 Agent Skill。

本專案提供單一 canonical `study-work` skill，可用於 Codex、Claude Code、Antigravity IDE、Cursor 與瀏覽器型 AI assistant。

> 這是依照本人的工作習慣設計，如有不便請自行調整。

## Skill

### `study-work`

研究與工程工作流程涵蓋：

- Model training 與 debugging
- Computer vision 與 image enhancement
- Industrial defect detection 與 anomaly detection
- Experiment design、paper review 與 ablation planning
- ONNX、TensorRT、Jetson、latency 與 production inference
- Technical report 與 experiment record
- Long-session context compaction
- 使用 Caveman reporting method 的 token-efficient technical output

Skill：[study-work](https://github.com/mcodare709/Engineering-skills/tree/main/skills/study-work "study-work")

Caveman 在本專案中不是獨立 skill，而是整合於 [`references/caveman.md`](skills/study-work/references/caveman.md) 的輸出方法 reference。

Codex：

```text
$study-work diagnose why training loss falls while validation loss rises
```

## 安裝

```bash
git clone https://github.com/mcodare709/Engineering-skills.git
cd Engineering-skills
python scripts/install_skill.py --client all --scope user
```

Project scope 安裝：

```bash
python scripts/install_skill.py --client all --scope project --project-root .
```

若要覆蓋既有安裝，加入 `--force`。

## 安裝位置

| Client | Project | User |
|---|---|---|
| Codex | `.agents/skills/study-work/` | `~/.agents/skills/study-work/` |
| Claude Code | `.claude/skills/study-work/` | `~/.claude/skills/study-work/` |
| Antigravity IDE | `.agents/skills/study-work/` | `~/.gemini/config/skills/study-work/` |
| Cursor | `.cursor/skills/study-work/` | `~/.cursor/skills/study-work/` |

Codex 與 Antigravity 在 project scope 共用 `.agents/skills/` 路徑。

## Web 版本

開啟 [`web/study-work.md`](web/study-work.md)，將完整內容複製到 system instructions、project instructions 或 custom instructions。

## 建置下載檔

```bash
python scripts/build.py
```

輸出：

```text
dist/study-work-skill.zip
dist/study-work-web.md
dist/study-work-public.zip
```

## 驗證

```bash
python scripts/validate_skill.py
```

Validation 會檢查 single-skill layout、metadata、local links、必要 references、web prompt、eval files、英文技術內容與禁止出現的 legacy artifacts。

## 專案結構

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

### 如果這個專案對你有幫助，歡迎給個 Star。

## Credits

Caveman reporting method：[caveman](https://github.com/mcodare709/subagent/tree/main/.agents/skills/caveman "caveman")。此方法以精簡且技術正確的輸出為主，在不影響清晰度的前提下降低 report/output token 使用量。
