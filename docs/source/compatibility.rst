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

- Seaborn builds on Matplotlib rcParams, and ``set_seaborn_theme`` applies
  compatible rc defaults.
- Plotly template changes are opt-in until set as default.
- Altair theme registration is process-local and should be re-enabled in new
  kernels.
