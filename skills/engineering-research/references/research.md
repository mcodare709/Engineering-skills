# Research and Paper Reference

## Paper Explanation

必須涵蓋：

```text
核心概念：方法實際做什麼
架構流程：資料如何通過各模組
設計動機：為何需要此設計
優點：在哪些條件下有效
限制：假設、失敗案例與成本
任務關聯：如何連結使用者目前研究
```

不要只重述 abstract。優先分析 mechanism、assumption、training objective、inference behavior 與實驗證據。

## Experiment Design

```text
Hypothesis:
Method:
Baselines:
Ablations:
Datasets and split protocol:
Metrics and statistical test:
Expected contribution:
Failure cases:
Reviewer concerns:
```

每個研究方向必須是可反駁、可測量、可重現的 hypothesis。

## Baseline Selection

- Include a simple/classical baseline to measure actual gain.
- Include the closest architectural or methodological baseline.
- Include recent peer-reviewed and currently maintained strong baselines verified at execution time.
- Distinguish paper claims, official-code results and independently reproduced results.
- Match dataset split, image resolution, metric implementation and test-time processing.

## Novelty Check

- Is the contribution more than combining known modules?
- What causal claim does each component support?
- Can ablation isolate every claimed contribution?
- Is improvement larger than run-to-run variance?
- Does the method add compute, data, supervision or hidden preprocessing?
- Does the evaluation include cross-dataset or real-world generalization?

## Reviewer Concerns

| Area | Typical concern |
|---|---|
| Image enhancement | Only synthetic degradation; perceptual quality not validated |
| Anomaly detection | Only one benchmark; threshold protocol unclear |
| Object detection | Weak or outdated baseline; inconsistent training budget |
| Medical imaging | Small dataset; no external validation; leakage risk |
| Edge deployment | Desktop estimate instead of target-hardware measurement |
| New module | Insufficient ablation; improvement within variance |

## Evidence Discipline

When discussing latest work, current software compatibility or state-of-the-art claims, verify publication/release dates and use available primary sources. Clearly separate verified facts from inference.
