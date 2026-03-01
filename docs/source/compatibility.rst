Compatibility
=============

- Python: 3.9+
- Matplotlib: 3.6+
- Seaborn: 0.12+
- Plotnine: 0.12+
- Plotly: 5.15+
- Altair: 5.0+

Notes
-----

- Base palette attribution: ``bluey``, ``chilli``, ``heeler``, and ``socks``
  come from `blueycolors <https://github.com/ekholme/blueycolors>`_.
- Seaborn builds on Matplotlib rcParams, and ``set_seaborn_theme`` applies
  compatible rc defaults.
- Plotly template changes are opt-in until set as default.
- Altair theme registration is process-local and should be re-enabled in new
  kernels.

Backend parity
--------------

.. list-table::
   :header-rows: 1

   * - Feature
     - Matplotlib
     - Seaborn
     - Plotnine
     - Plotly
     - Altair
   * - Discrete palette support
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
   * - Continuous scale support
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
   * - Light/dark token support
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
   * - One-line apply helper
     - ``apply_matplotlib_theme``
     - ``set_seaborn_theme``
     - ``theme_calm``
     - ``register_plotly_template``
     - ``enable_altair_theme``
