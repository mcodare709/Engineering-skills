# Context Engineering

## Trigger

Compact when any condition appears:

- Conversation or tool output is long enough to hide early constraints.
- Same fact is repeated or contradicted.
- Output is truncated.
- Multiple files, experiments, branches, or tool calls are active.
- Model starts re-asking answered questions.
- Platform signals automatic compaction or context pressure.

## Checkpoint

Use this exact structure:

```text
Goal:
Constraints:
Decisions:
Evidence:
Files and symbols:
Commands and results:
Current state:
Open risks:
Next action:
```

## Rules

- Keep facts, not transcript.
- Preserve exact paths, names, hashes, versions, metrics, thresholds, and errors.
- Mark assumptions as assumptions.
- Mark failed attempts and why they failed.
- Remove rejected options unless rejection reason remains relevant.
- Keep only latest state for each file or decision.
- Never omit destructive-operation risk, uncommitted work, or validation status.
- Use one current checkpoint as authoritative working context.
- Continue from checkpoint immediately.

If hidden scratch state is unavailable, emit checkpoint in conversation, then continue.
