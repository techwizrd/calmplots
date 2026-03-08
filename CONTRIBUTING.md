# Contributing to calmplots

Thanks for contributing.

## Development setup

We recommend `uv` for local development.

```bash
uv sync --extra dev
```

Lighter setups are available:

```bash
uv sync --extra test
uv sync --extra docs
uv sync --extra gallery
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

## Reproducibility policy

`calmplots` is a library, so we do not commit a project lockfile.
We keep lower-bounded dependency specs in `pyproject.toml` and validate in CI.

## Plotly static export note

Gallery image export uses `kaleido>=0.2.1,<1` for compatibility with the
current Plotly image engine behavior in CI/dev environments.
When Plotly export is stable on Kaleido 1.x for this project, we should remove
the `<1` pin and the related warning-suppression helper.

## Pull request expectations

- Keep changes focused and small.
- Add or update tests for behavior changes.
- Update docs for user-facing changes.
- Keep public API stable unless there is a clear reason to change it.

## Releases

For a release:

1. Update version in `pyproject.toml`.
2. Add release notes in `CHANGELOG.md`.
3. Ensure both GitHub environments exist:
   - `testpypi` (trusted publisher configured in TestPyPI)
   - `pypi` (trusted publisher configured in PyPI)
   - configure `pypi` with required reviewers if you want manual approval before publish
4. Create and push a tag (`vX.Y.Z`).
5. The release workflow will:
   - build wheel/sdist
   - run `twine check`
   - run wheel install + quickstart smoke checks
   - publish to TestPyPI first
   - publish to PyPI after the TestPyPI gate
