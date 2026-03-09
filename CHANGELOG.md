# Changelog

All notable changes to this project are documented in this file.

The format is based on Keep a Changelog, and this project follows Semantic Versioning.

## [0.1.2] - 2026-03-09

### Added

- Trusted-publishing release automation with TestPyPI-first workflow, package install smoke checks, and guarded PyPI publishing controls.
- CI package smoke test that installs the built wheel and validates quickstart theme setup calls.
- Community health assets (issue templates, PR template, support and security guidance).

### Changed

- Install guidance now prioritizes `pip install calmplots` and includes optional extras plus Git URL install commands for `pip` and `uv`.
- README gallery preview links now use stable docs-hosted assets for correct rendering on package indexes.
- Packaging metadata updated for current setuptools license standards (`license` SPDX string and `license-files`).

## [0.1.0] - 2026-02-28

### Added

- Initial `calmplots` package with integrations for Matplotlib, Seaborn, Plotnine, Plotly, and Altair.
- Shared tokens and palette registry including `bluey10` and a colorblind-considerate set.
- Gallery scripts and user docs (quickstart, do/don't, compatibility).
- Test suite for palette behavior and backend application smoke tests.
- Pre-commit configuration with Ruff and Pyrefly checks.
