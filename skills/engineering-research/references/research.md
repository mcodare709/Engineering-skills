# Research and Paper Reference

## Paper Explanation Template

When explaining a paper or method, cover all six points:

```
核心概念：what the method is doing, in one sentence
架構流程：how data moves through the model, step by step
設計動機：why the authors made this design choice
優點：what problem it solves well and under what conditions
限制：where it fails or what assumptions it relies on
和你任務的關聯：how this connects to what the user is currently building
```

Do not just summarize the abstract. Focus on mechanism, assumptions, and practical use.

## Experiment Design Template

Apply IEEE-style research thinking. For every proposed direction:

```
Hypothesis:    [verifiable claim being tested]
Method:        [proposed approach]
Baselines:     [what must be compared against]
Ablations:     [which components need isolated testing]
Metrics:       [evaluation protocol and dataset]
Expected contribution: [what gap this fills]
Reviewer concerns:     [what reviewers will likely challenge]
```

A good research direction must be testable, not just interesting.

## Novelty Self-Check

Before finalizing an experiment proposal, verify:

- Is the baseline up to date? (check papers from last 1–2 years)
- Is the evaluation dataset standard in this subfield?
- Is the ablation sufficient to prove the claimed contribution?
- Is the metric the right one for the task, or just the easiest to compute?
- Would a reviewer say "this is just X + Y with no new insight"?

## Common Reviewer Concerns by Area

| Area | Typical Concern |
|---|---|
| Image enhancement | Evaluated only on synthetic degradation |
| Anomaly detection | Evaluated only on MVTec, not industrial data |
| Object detection | No comparison with latest RT-DETR / YOLOv9+ |
| Medical imaging | Small dataset, no external validation |
| Edge deployment | No real latency measurement on target hardware |
