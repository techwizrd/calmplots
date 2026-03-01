Colorblindness
==============

This page documents how ``calmplots`` approaches color-vision-deficiency (CVD)
robust palette design.

Background
----------

- CVD overview: `Color blindness (Wikipedia) <https://en.wikipedia.org/wiki/Color_blindness>`_
- Design guidance and simulation tool: `Color Oracle <https://colororacle.org/>`_
- Additional simulator for quick checks: `Coblis Color Blindness Simulator <https://www.color-blindness.com/coblis-color-blindness-simulator/>`_

Color science approach
----------------------

``calmplots`` evaluates palette separation in a perceptual color space and
under CVD simulation:

- Perceptual distance uses the `Oklab color space <https://bottosson.github.io/posts/oklab/>`_.
- CVD simulation uses matrices from
  `Machado, Oliveira, Fernandes (2009) <https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html>`_.
- Contrast checks use WCAG luminance contrast guidance:
  `W3C WCAG Contrast (Minimum) <https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html>`_.

Simulation and optimization objective
-------------------------------------

For each candidate palette, ``calmplots`` checks pairwise separation across:

- normal vision
- protan simulation at moderate/full severity
- deutan simulation at moderate/full severity
- tritan simulation at moderate/full severity

The practical objective is to maximize worst-case color separation while
keeping per-color contrast to background reasonable in default chart settings.

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

Notes
-----

No fixed palette can perfectly preserve all distinctions for all viewers,
chart types, and display conditions. The goal is strong default robustness,
especially for common protan/deutan scenarios, without requiring immediate
style overrides.
