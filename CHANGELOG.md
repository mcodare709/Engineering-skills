# Changelog

## [1.4.0] - 2026-08-08

### Added

- Added `caveman` as a standalone portable Agent Skill.
- Added a self-contained `web/caveman.md` prompt.
- Added Caveman trigger and output eval cases.
- Added `--skill study-work|caveman|all` installation support.
- Added per-skill build outputs for local, web, and public bundles.

### Changed

- Converted installer, builder, and validator from single-skill to multi-skill operation.
- Updated README for both `$study-work` and `$caveman`.
- Corrected clone instructions to `mcodare709/Engineering-skills`.

## [1.3.0] - 2026-08-08

### Added

- Added explicit Caveman output modes: `lite`, `full`, and `ultra`.
- Made `caveman full` the persistent default output mode.
- Added automatic clarity fallback for security, irreversible actions, ambiguous ordered procedures, and clarification.
- Synced Caveman behavior between the canonical Agent Skill and web prompt.

## [1.2.1] - 2026-08-06

### Changed

- Renamed the public skill from `engineering-research` to `study-work`.
- Updated Codex invocation to `$study-work`.
- Updated install paths, web prompt, build outputs, eval metadata, and validation.

## [1.2.0] - 2026-08-06

### Added

- One cross-client installer for Codex, Claude Code, Antigravity IDE, and Cursor.
- Self-contained web prompt.
- Systematic context-compaction protocol.
- Public bundle build containing local skill and web version.
- English-only and no-image validation.

### Changed

- Rewrote all skill content in concise English.
- Adapted output rules from the Caveman skill: terse, exact, no filler.
- Reduced platform-specific wording and kept one canonical Agent Skill source.

### Removed

- `docs/images/` and all screenshot documentation.

## [1.1.0] - 2026-08-06

- Added validation, packaging, evals, and domain references.
- Renamed `skill.md` to `SKILL.md`.
