# Changelog

## [1.4.0] - 2026-08-08

### Added

- Added `skills/study-work/references/caveman.md` as the canonical Caveman output-method reference inside `study-work`.
- Added Caveman compression, exact-string preservation, auto-clarity, and normal-mode coverage to the `study-work` output evals.

### Changed

- Kept the repository as one canonical Agent Skill: `study-work`.
- Centralized detailed Caveman rules in the `study-work` reference instead of duplicating them in `SKILL.md`.
- Restored single-skill installer, builder, validator, README, and CI behavior.
- Corrected clone instructions to `mcodare709/Engineering-skills`.

### Removed

- Removed standalone `caveman` skill packaging and invocation.
- Removed standalone `web/caveman.md` and Caveman-only eval files.
- Removed multi-skill `--skill` installer/build behavior.

## [1.3.0] - 2026-08-08

### Added

- Added explicit Caveman output modes: `lite`, `full`, and `ultra` inside `study-work`.
- Made `caveman full` the default compact output mode.
- Added automatic clarity fallback for security, irreversible actions, ambiguous ordered procedures, and clarification.
- Synced compact-output behavior between the canonical Agent Skill and web prompt.

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
- Adapted output rules from the Caveman method: terse, exact, no filler.
- Reduced platform-specific wording and kept one canonical Agent Skill source.

### Removed

- `docs/images/` and all screenshot documentation.

## [1.1.0] - 2026-08-06

- Added validation, packaging, evals, and domain references.
- Renamed `skill.md` to `SKILL.md`.
