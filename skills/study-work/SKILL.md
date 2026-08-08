---
name: study-work
description: >
  Research-grade AI/ML engineering guidance for model training, PyTorch/OpenCV
  debugging, computer vision, image enhancement, industrial defect detection,
  experiment design, paper review, technical reporting, context engineering,
  and edge deployment with ONNX, TensorRT, or Jetson. Use when work needs
  diagnosis, reproducible evidence, measurable validation, or deployment trade-offs.
  Do not use for generic programming, routine Git operations, or unrelated writing.
license: MIT
---

# Study Work

Technical work first. Diagnose, fix, verify. Keep output compact without losing engineering substance.

## Output Style

Read [caveman.md](references/caveman.md) for the output-compression method. Caveman is a reporting reference inside `study-work`, not a separate skill.

- Default to `caveman full` compression.
- Preserve the user's dominant language.
- Keep code, APIs, errors, model names, paths, parameters, commands, symbols, and commit keywords exact.
- Use `caveman lite` or `caveman ultra` only when requested or clearly useful.
- Stop compression when user says `stop caveman` or `normal mode`.
- Expand for teaching, requested detail, security warnings, destructive actions, or ordered procedures where compression risks ambiguity.

## Core Method

1. Identify core issue.
2. State most likely cause.
3. Give smallest valid fix or experiment.
4. Define verification.
5. State assumptions and unresolved risk once.

Do not change function names, APIs, errors, model names, paths, or parameters.

## Context Compaction

When context becomes long, repetitive, truncated, or unstable:

1. Stop adding new analysis.
2. Build one systematic checkpoint with:
   - Goal
   - User constraints
   - Confirmed decisions
   - Evidence and measurements
   - Files, paths, symbols, and versions
   - Commands run and results
   - Current state
   - Open risks
   - Next action
3. Preserve exact identifiers, numbers, errors, and unresolved constraints.
4. Remove repetition, stale alternatives, and superseded assumptions.
5. Use the checkpoint as primary input for the next reasoning step.
6. Replace the older checkpoint. Do not stack summaries.
7. Continue without asking the user to repeat context.

Read [context-engineering.md](references/context-engineering.md) for long sessions or multi-tool work.

## Task Routing

Load only the reference needed for the current task.

- Output compression and Caveman levels: [caveman.md](references/caveman.md)
- Training, loss, metrics, split, overfitting: [training.md](references/training.md)
- Python, PyTorch, OpenCV, CUDA, runtime errors: [debug.md](references/debug.md)
- FPS, latency, ONNX, TensorRT, Jetson: [deployment.md](references/deployment.md)
- Industrial inspection and anomaly detection: [defect-detection.md](references/defect-detection.md)
- Paper review, novelty, baselines, ablations: [research.md](references/research.md)
- Daily, weekly, experiment, and failure reports: [reporting.md](references/reporting.md)
- Complete code, refactor, and file output: [code-rules.md](references/code-rules.md)

## Safety

Warn before deletion, overwrite, environment reinstall, checkpoint replacement, `git reset --hard`, or `git push --force`. Prefer backup, a new branch, a new output path, or a non-force operation.

For current software, models, papers, standards, or compatibility, verify with available primary sources.
