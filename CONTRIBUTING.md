# Contributing to calmplots

Thanks for contributing.

## Development setup

We recommend `uv` for local development.

```bash
uv sync --extra dev
```

Run checks:

```bash
uv run pytest
uv run pyrefly check
uv run pre-commit run --all-files
```

Install hooks (recommended with `prek`, supported with `pre-commit`):

```bash
prek install
```

or

```bash
pre-commit install
```

## Documentation

Build docs locally with Sphinx:

```bash
uv run sphinx-build -b html docs/source docs/_build/html
```

## Pull request expectations

- Keep changes focused and small.
- Add or update tests for behavior changes.
- Update docs for user-facing changes.
- Keep public API stable unless there is a clear reason to change it.

## Releases

For a release:

1. Update version in `pyproject.toml`.
2. Add release notes in `CHANGELOG.md`.
3. Create and push a tag (`vX.Y.Z`).
