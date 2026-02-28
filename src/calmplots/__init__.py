"""calmplots: cohesive plot themes across popular Python viz libraries."""

from .altair_theme import enable_altair_theme, register_altair_theme
from .matplotlib_theme import apply_matplotlib_theme, use_matplotlib_stylesheet
from .palettes import (
    bluey_palette,
    colorblind_palette,
    continuous_palette,
    list_palettes,
)
from .plotly_theme import register_plotly_template
from .plotnine_theme import (
    scale_color_calm,
    scale_color_calm_c,
    scale_fill_calm,
    scale_fill_calm_c,
    theme_calm,
)
from .presets import apply_notebook_theme
from .seaborn_theme import set_seaborn_theme
from .tokens import get_tokens

__all__ = [
    "apply_matplotlib_theme",
    "apply_notebook_theme",
    "bluey_palette",
    "colorblind_palette",
    "continuous_palette",
    "enable_altair_theme",
    "get_tokens",
    "list_palettes",
    "register_altair_theme",
    "register_plotly_template",
    "scale_color_calm",
    "scale_color_calm_c",
    "scale_fill_calm",
    "scale_fill_calm_c",
    "set_seaborn_theme",
    "theme_calm",
    "use_matplotlib_stylesheet",
]

__version__ = "0.1.0"
