# calmplots

[![CI](https://github.com/techwizrd/calmplots/actions/workflows/ci.yml/badge.svg)](https://github.com/techwizrd/calmplots/actions/workflows/ci.yml)
[![Docs](https://github.com/techwizrd/calmplots/actions/workflows/docs.yml/badge.svg)](https://github.com/techwizrd/calmplots/actions/workflows/docs.yml)
[![codecov](https://codecov.io/gh/techwizrd/calmplots/graph/badge.svg)](https://codecov.io/gh/techwizrd/calmplots)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB.svg)](https://www.python.org/downloads/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)

`calmplots` is a cohesive visualization theme package for:

- Matplotlib
- Seaborn
- Plotnine
- Plotly
- Altair

It is inspired by the spirit of the `blueycolors` palette family and aims to provide attractive, consistent defaults across notebooks, reports, and dashboards.

## Install with uv

```bash
uv sync
```

Install with all plotting backends:

```bash
uv sync --extra all
```

For development (tests + all integrations):

```bash
uv sync --extra dev
```

## Quickstart

```python
import calmplots

# Matplotlib + Seaborn
calmplots.apply_matplotlib_theme()
calmplots.set_seaborn_theme(context="notebook")

# Plotly
calmplots.register_plotly_template(set_default=True)

# Altair
calmplots.enable_altair_theme()
```

## Core design

- Clarity first: readable labels, lines, and grid hierarchy
- Consistent tokens: one semantic token source reused across backends
- Sensible defaults: subtle grid, softened spines, accessible emphasis
- Accessible by design: includes a colorblind-considerate categorical palette

## Documentation

- Website: `https://techwizrd.github.io/calmplots/`
- Quickstart: `docs/source/quickstart.rst`
- Do/Don't guide: `docs/source/do_dont.rst`
- Compatibility notes: `docs/source/compatibility.rst`
- Gallery scripts: `examples/gallery/`

## Contributing

See `CONTRIBUTING.md` for development setup, checks, and release process.
