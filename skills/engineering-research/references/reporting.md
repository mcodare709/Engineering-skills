# Technical Reporting Reference

## Daily Report

Use 2–4 concise narrative bullets. Each bullet should contain:

```text
Action performed → technical method → result or current status
```

Avoid empty statements such as「持續研究」or「進行測試」without method or result.

## Weekly / Progress Report

Recommended structure:

1. Objective and scope
2. Work completed
3. Quantitative result or observed behavior
4. Current blocker and root cause
5. Next experiment or engineering action

## Experiment Record

```text
Experiment ID / date:
Hypothesis:
Git commit:
Dataset and split version:
Configuration:
Hardware/software:
Evaluation command:
Primary metrics:
Key observations:
Failure cases:
Decision:
Next action:
```

## Result Paragraph

A research result paragraph should state:

1. Which method/dataset/setting is compared.
2. The important metric difference with exact values.
3. The plausible mechanism supported by evidence.
4. The limitation or condition under which the conclusion holds.

Do not claim causality from one aggregate metric without ablation or controlled comparison.

## Failure Report

```text
Observed symptom:
Expected behavior:
Reproduction condition:
Most likely root cause:
Evidence:
Temporary workaround:
Permanent fix:
Validation status:
```
