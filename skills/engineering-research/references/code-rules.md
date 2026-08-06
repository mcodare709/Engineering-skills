# Code Rules Reference

## Core Rule

精簡 code 是移除重複與不必要結構，不是將獨立邏輯壓縮成同一行。

```python
# Bad
model.eval(); x = x.to(device); y = model(x)

# Good
model.eval()
x = x.to(device)
y = model(x)
```

## Completeness

| Request | Must include |
|---|---|
| 完整程式碼 | Imports, initialization, validation, error handling, entry point |
| 精簡程式碼 | Remove unused variables, duplication and verbose wrappers |
| Training pipeline | Dataset, model, loss, optimizer, loop, validation, checkpoint |
| Inference pipeline | Preprocess, load, infer, post-process, output |
| Refactor | Preserve behavior unless explicitly requested otherwise |
| Debug fix | Minimal patch plus verification; full file when changes span locations |

## Output Method

For complete or reusable code:

1. If the client supports file/artifact creation, create a standalone file.
2. Otherwise return one complete fenced code block.
3. Do not split one runnable file across many disconnected snippets.
4. Put explanation outside the code file unless comments are required for maintenance.

For short commands, one function or a small patch, use an inline code block.

## Style

- Follow language conventions and existing project style.
- Do not chain independent statements with semicolons.
- Preserve function/API names and public interfaces.
- Add type hints and input validation when they improve correctness.
- Handle missing files, invalid shapes and unavailable devices where applicable.
- Do not introduce abstraction that has only one trivial use.

## Safe Changes

Before destructive operations, state what will be removed or overwritten. Prefer backup, new output path, new Git branch or non-force operation.
