# Code Rules Reference

## Core Rule

Concise = remove redundant structure, not compress logic into one line.

## Line Formatting

Never chain independent statements:
```python
# Bad
model.eval(); x = x.to(device); y = model(x)

# Good
model.eval()
x = x.to(device)
y = model(x)
```

Allowed one-liners — only when they don't hide logic:
```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Net().to(device).eval()
img = cv2.imread(str(img_path))
files = sorted(Path(root).glob("*.png"))
x = x.to(device, non_blocking=True)
loss = criterion(output, target.long())
```

## Artifact vs Inline

| Use artifact | Use inline code block |
|---|---|
| Complete scripts | Short snippets or patches |
| > ~40 lines | CLI commands |
| Code user will edit/reuse | Single functions |
| Training / inference pipelines | Illustrative examples |

Artifact contains only code. Explanation goes in chat.

## Completeness by Request

| Request | Must include |
|---|---|
| "完整程式碼" | All imports, init, error handling — no placeholders |
| "簡潔程式碼" | Remove unused vars, redundant comments, verbose wrappers |
| Training pipeline | Dataset, model, loss, optimizer, loop, validation, checkpoint |
| Inference pipeline | Preprocessing, load, infer, post-process, output |
| Refactor | Preserve behavior unless user explicitly says otherwise |

## What "Concise" Means

Remove: redundant comments, repeated logic, unused variables, unnecessary wrappers.

Keep: correctness, execution order, imports, error handling, readability.
