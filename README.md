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

It is inspired by the spirit of the [`blueycolors`](https://github.com/ekholme/blueycolors) palette family and aims to provide attractive, consistent defaults across notebooks, reports, and dashboards.

## Palette compatibility

- Exact `blueycolors` palettes: `bluey`, `chilli`, `heeler`, `socks`
- calmplots extensions: `bluey10`, `colorblind`, and continuous ramps (`bluey_seq`, `sunset_seq`, `bluey_div`)
- In dark themes, `colorblind` is automatically mapped to a dark-safe variant for contrast.
- Public API stability: names exported in `calmplots.__all__` are considered stable

## Palette quick guide

- Use `bluey`, `chilli`, `heeler`, or `socks` when you want strict `blueycolors` compatibility.
- Use `colorblind` when category distinction and accessibility are the top priority.
- Use `accessible_palette(theme="light"|"dark")` for CVD-optimized defaults.
- Use `bluey10` for larger categorical charts (up to 10 categories).
- For very high category counts, group categories and highlight only key series.
- Use continuous ramps (`bluey_seq`, `bluey_div`) for heatmaps and gradients.

Accessibility note:

- `calmplots` uses Color Vision Deficiency (CVD) simulation checks, perceptual distance checks, and contrast checks for accessibility-focused palettes.
- This evidence supports real-world usage. It does not claim universal suitability for all CVD types, severities, or chart designs.

## Attribution

The base palette set is derived from
[`blueycolors`](https://github.com/ekholme/blueycolors) by Eric Ekholm.

## Install with uv

```bash
uv sync --extra all
```

For docs and test tooling only:

```bash
uv sync --extra docs --extra test
```

For full development (all backends + docs + checks):

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

- Website: [techwizrd.github.io/calmplots](https://techwizrd.github.io/calmplots/)
- Quickstart: [Quickstart](https://techwizrd.github.io/calmplots/quickstart.html)
- Do/Don't guide: [Do/Don't](https://techwizrd.github.io/calmplots/do_dont.html)
- Compatibility notes: [Compatibility](https://techwizrd.github.io/calmplots/compatibility.html)
- Colorblindness approach: [Colorblindness](https://techwizrd.github.io/calmplots/colorblindness.html)
- Gallery page: [Gallery](https://techwizrd.github.io/calmplots/gallery.html)
- Matrix index: [examples/gallery/matrix/README.md](examples/gallery/matrix/README.md)

## Gallery Preview

Palette Gallery (all palettes)

Light background

![calmplots palettes light](examples/gallery/palettes_light.png)

Dark background

![calmplots palettes dark](examples/gallery/palettes_dark.png)

Before vs After (Matplotlib)

| Default Matplotlib | calmplots |
|---|---|
| ![Default Matplotlib](examples/gallery/before_default_scatter.png) | ![calmplots Matplotlib](examples/gallery/before_calmplots_scatter.png) |

Matplotlib/Seaborn

![Matplotlib Seaborn Gallery](examples/gallery/gallery_matplotlib.png)

Plotnine

![Plotnine Scatter](examples/gallery/plotnine_scatter.png)

Plotly

![Plotly Scatter](examples/gallery/plotly_scatter.png)

Altair

![Altair Scatter](examples/gallery/altair_scatter.png)

## Contributing

See `CONTRIBUTING.md` for development setup, checks, and release process.
