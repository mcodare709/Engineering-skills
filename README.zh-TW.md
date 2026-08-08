# Engineering Skills（工程技能）

[英文](README.md) | **繁體中文**

適用於 AI/ML 研究、工程開發與節省 token 的技術輸出之可攜式 Agent 技能。

本專案提供單一正式的 `study-work` 技能，可用於 Codex、Claude Code、Antigravity IDE、Cursor 與瀏覽器型 AI 助手。

> 這是依照本人的工作習慣設計，如有不便請自行調整。

## 技能

### `study-work`

研究與工程工作流程涵蓋：

- 模型訓練與除錯
- 電腦視覺與影像增強
- 工業瑕疵檢測與異常檢測
- 實驗設計、論文審查與消融實驗規劃
- ONNX、TensorRT、Jetson、延遲與生產環境推論
- 技術報告與實驗紀錄
- 長對話上下文壓縮
- 使用 Caveman 精簡回應方式，降低技術輸出的 token 使用量

技能：[study-work](https://github.com/mcodare709/Engineering-skills/tree/main/skills/study-work "study-work")

Caveman 在本專案中不是獨立技能，而是整合於 [`references/caveman.md`](skills/study-work/references/caveman.md) 的輸出風格參考規則。

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

專案範圍安裝：

```bash
python scripts/install_skill.py --client all --scope project --project-root .
```

若要覆蓋既有安裝，加入 `--force`。

## 安裝位置

| 用戶端 | 專案 | 使用者 |
|---|---|---|
| Codex | `.agents/skills/study-work/` | `~/.agents/skills/study-work/` |
| Claude Code | `.claude/skills/study-work/` | `~/.claude/skills/study-work/` |
| Antigravity IDE | `.agents/skills/study-work/` | `~/.gemini/config/skills/study-work/` |
| Cursor | `.cursor/skills/study-work/` | `~/.cursor/skills/study-work/` |

Codex 與 Antigravity 在專案範圍共用 `.agents/skills/` 路徑。

## 網頁版

開啟 [`web/study-work.md`](web/study-work.md)，將完整內容複製到系統指令、專案指令或自訂指令。

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

驗證程序會檢查單一技能架構、中繼資料、本地連結、必要參考檔、網頁提示詞、評估檔案、英文技術內容，以及禁止出現的舊版殘留檔案。

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

## 授權

MIT。

### 如果這個專案對你有幫助，歡迎給個 Star。

## 致謝

Caveman 精簡回應方式：[caveman](https://github.com/mcodare709/subagent/tree/main/.agents/skills/caveman "caveman")。此方法以精簡且技術正確的輸出為主，在不影響清晰度的前提下降低回應 token 使用量。
