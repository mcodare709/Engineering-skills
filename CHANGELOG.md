# Changelog

All notable changes to this project are documented here.

## [1.1.0] - 2026-08-06

### Added

- Automated skill validation and packaging scripts.
- GitHub Actions validation workflow.
- Trigger and output evaluation cases.
- Reporting reference for daily, weekly and experiment summaries.
- Frontmatter metadata, compatibility scope and explicit task routing.

### Changed

- Renamed the main entry file from `skill.md` to `SKILL.md`.
- Narrowed the activation description to reduce false triggering.
- Replaced product-specific code artifact rules with capability-neutral behavior.
- Moved screenshots from `pit/` to `docs/images/`.

### Removed

- Committed `skills/engineering-research.zip`; packages are now generated from source.
