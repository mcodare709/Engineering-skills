# Code Rules

Concise code removes redundancy. It does not compress independent logic into one line.

```python
# Bad
model.eval(); x = x.to(device); y = model(x)

# Good
model.eval()
x = x.to(device)
y = model(x)
```

## Complete Code

Include imports, initialization, validation, error handling, entry point, and verification path. No placeholders when user asks for runnable code.

## Output

- Complete reusable file: create one file or one complete code block.
- Small patch, command, or function: inline code block.
- Do not split one runnable file across disconnected snippets.
- Preserve public interfaces unless user requests change.
- Follow project style.
- Avoid one-use abstraction.
- Validate missing files, invalid shapes, and unavailable devices when relevant.
