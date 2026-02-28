# Compatibility notes

- Python: 3.9+
- Matplotlib: 3.6+
- Seaborn: 0.12+
- Plotnine: 0.12+
- Plotly: 5.15+
- Altair: 5.0+

## Backend-specific notes

- Seaborn builds on Matplotlib rcParams. `set_seaborn_theme` uses calmplots rc defaults to avoid conflicting style state.
- Plotly template is non-destructive until you set it as default.
- Altair theme registration is process-local. Re-enable in each fresh notebook/kernel.
