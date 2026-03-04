Colorblindness
==============

This page documents how ``calmplots`` approaches color-vision-deficiency (CVD)
robust palette design.

Background
----------

- CVD overview: `Color blindness (Wikipedia) <https://en.wikipedia.org/wiki/Color_blindness>`_
- Design guidance and simulation tool: `Color Oracle <https://colororacle.org/>`_
- Additional simulator for quick checks: `Coblis Color Blindness Simulator <https://www.color-blindness.com/coblis-color-blindness-simulator/>`_

Scope
-----

``calmplots`` includes accessibility-focused palettes and simulation tools.
The goal is clear category separation in common chart defaults.

Current palette groups:

- ``colorblind``
- ``colorblind_dark``
- ``accessible8_light``
- ``accessible8_dark``

The package supports normal vision checks and CVD simulation checks.

The project does not claim universal suitability for every viewer profile, display pipeline, or plot design.

Color science approach
----------------------

``calmplots`` evaluates palette separation in a perceptual color space and
under CVD simulation:

- Perceptual distance uses the `Oklab color space <https://bottosson.github.io/posts/oklab/>`_.
- CVD simulation uses matrices from
  `Machado, Oliveira, Fernandes (2009) <https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html>`_.
- Contrast checks use WCAG luminance contrast guidance:
  `W3C WCAG Contrast (Minimum) <https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html>`_.

Simulation set
--------------

For each candidate palette, ``calmplots`` checks pairwise separation across:

- normal vision
- protan simulation at moderate/full severity
- deutan simulation at moderate/full severity
- tritan simulation at moderate/full severity

The simulation code uses severity interpolation between identity and full
Machado matrices. This supports a smooth range from mild to severe settings.

Scoring and thresholds
----------------------

``calmplots`` computes the minimum pairwise OKLab distance across all selected
simulation modes for each palette.

That value supports a maximin selection strategy:

- maximize the smallest pairwise distance
- preserve readability under weaker conditions

``calmplots`` also computes minimum color-to-background contrast for each
palette under theme background tokens.

Current report helper thresholds:

- ``distance_ok`` when minimum pairwise OKLab distance is at least ``0.08``
- ``contrast_ok`` when minimum contrast ratio to background is at least ``2.0``

These thresholds are practical defaults for categorical marks in theme-level
usage. Teams can set stricter thresholds for domain-specific requirements.

Theme-aware behavior
--------------------

Dark themes use darker backgrounds and panel colors.
The standard ``colorblind`` list includes a near-black color.
Near-black marks lose salience on dark backgrounds.

``calmplots`` resolves ``colorblind`` to ``colorblind_dark`` when
``theme="dark"`` is active in theme-aware integrations.

This resolution keeps category visibility stable across backends.
This resolution applies in Matplotlib, Seaborn, Plotnine, Plotly, and Altair
through the shared palette resolver.

Available palettes
------------------

- ``colorblind``: conventional colorblind-considerate categorical set.
  In dark theme contexts, this resolves to a dark-safe variant to avoid low-contrast black marks.
- ``accessible8_light`` / ``accessible8_dark``: CVD-optimized categorical sets.
- ``accessible_palette(theme="light"|"dark")``: helper for theme-aware selection.

Programmatic helpers
--------------------

- ``simulate_cvd_hex(hex_color, deficiency, severity)``
- ``min_pairwise_oklab_distance(hex_colors, include_cvd=True)``
- ``palette_accessibility_report(hex_colors, background)``

Human testing note
------------------

A contributor with mild to moderate protan color vision performed manual chart
review of the accessibility palettes and dark-mode substitutions.

The review covers category charts, scatter plots, line charts, and small
legend contexts. The review confirms stronger practical separation for their
visual profile.

This manual review adds direct user evidence from an affected viewer.
Automated simulation remains part of the formal check path.

Validate with your own profile
------------------------------

You can run a short repeatable check with their own viewing conditions.

1. Generate gallery outputs for light and dark themes.
2. Open the outputs on the same display class used for regular work.
3. Review category separation in small legends and dense marks.
4. Confirm readability under at least one external simulator.
5. Record any ambiguous pairs and adjust palette choice by chart type.

Example local commands:

.. code-block:: bash

   uv run python examples/gallery/palette_gallery.py
   uv run python examples/gallery/generate_matrix.py

You can then inspect ``examples/gallery/palettes_light.png`` and
``examples/gallery/palettes_dark.png`` first, then review the backend matrix in
``examples/gallery/matrix/README.md``.

Notes
-----

No fixed palette can preserve every distinction for every visual context.
The package targets robust defaults for common use.
High-stakes plots should add direct labels, mark-shape encoding, and careful
category reduction.

References
----------

- `Color blindness (Wikipedia) <https://en.wikipedia.org/wiki/Color_blindness>`_
- `Oklab color space <https://bottosson.github.io/posts/oklab/>`_
- `Machado CVD simulation model <https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html>`_
- `WCAG contrast guidance <https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html>`_
- `Color Oracle simulator <https://colororacle.org/>`_
- `Coblis simulator <https://www.color-blindness.com/coblis-color-blindness-simulator/>`_
