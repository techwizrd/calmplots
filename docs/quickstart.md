# Quickstart

## Install with uv

```bash
uv sync --extra all
```

## Apply themes

```python
import calmplots

# Matplotlib and Seaborn
calmplots.apply_matplotlib_theme()
calmplots.set_seaborn_theme(context="notebook")

# Plotly
calmplots.register_plotly_template(set_default=True)

# Altair
calmplots.enable_altair_theme()
```

## Plotnine example

```python
from plotnine import aes, geom_point, ggplot
import pandas as pd
from calmplots import theme_calm, scale_color_calm

df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [2, 3, 2, 5], "grp": ["a", "b", "a", "b"]})

p = (
    ggplot(df, aes("x", "y", color="grp"))
    + geom_point(size=3)
    + scale_color_calm()
    + theme_calm()
)
```
