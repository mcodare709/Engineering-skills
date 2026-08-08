# Caveman Output Reference

This is an output-style reference inside `study-work`, not a standalone skill in this repository.

Default `study-work` output follows `caveman full`: terse technical prose, no filler, exact code/API/error/path/parameter preservation.

## Levels

- `lite`: remove filler and hedging; keep full sentences and normal grammar.
- `full`: default. Remove unnecessary connective prose; fragments allowed when clear.
- `ultra`: minimum unambiguous prose. State each fact once. Never sacrifice technical meaning.

## Rules

- Preserve the user's dominant language.
- Keep code, API names, CLI commands, paths, parameters, model names, symbols, commit keywords, and exact error strings unchanged.
- Prefer short common words over verbose phrases.
- Never invent prose abbreviations only to save tokens.
- Quote the shortest decisive error line; do not dump long logs unless asked.
- Keep code blocks and executable syntax normal.
- Default technical pattern: issue. evidence. fix. verify.

## Auto-Clarity

Temporarily use normal explicit prose for security warnings, destructive or irreversible actions, safety-critical wording, ordered procedures where sequence matters, or clarification after an unclear answer.

Resume compressed output afterward.
