"""Plotnine theme and scales for calmplots."""

from __future__ import annotations

from .palettes import bluey_palette, continuous_palette
from .tokens import get_tokens


def theme_calm(theme: str = "light"):
    """Return a clean minimal plotnine theme."""
    try:
        from plotnine import element_blank, element_line, element_rect, element_text, theme as p9_theme, theme_minimal
    except Exception as exc:  # pragma: no cover
        raise ImportError("plotnine is not installed. Install with: uv add 'calmplots[plotnine]'") from exc

    t = get_tokens(theme)
    return theme_minimal() + p9_theme(
        panel_background=element_rect(fill=t["panel_background"], color=t["panel_background"]),
        plot_background=element_rect(fill=t["background"], color=t["background"]),
        panel_grid_major=element_line(color=t["grid_major"], size=0.45),
        panel_grid_minor=element_line(color=t["grid_minor"], size=0.25),
        axis_text=element_text(color=t["muted_foreground"], size=9),
        axis_title=element_text(color=t["foreground"], size=10),
        plot_title=element_text(color=t["foreground"], size=13),
        panel_border=element_blank(),
        legend_background=element_rect(fill=t["background"], color=t["background"]),
        legend_key=element_rect(fill=t["panel_background"], color=t["panel_background"]),
    )


def scale_color_calm(name: str = "bluey10", **kwargs):
    """Discrete color scale for plotnine."""
    try:
        from plotnine import scale_color_manual
    except Exception as exc:  # pragma: no cover
        raise ImportError("plotnine is not installed. Install with: uv add 'calmplots[plotnine]'") from exc
    return scale_color_manual(values=bluey_palette(name), **kwargs)


def scale_fill_calm(name: str = "bluey10", **kwargs):
    """Discrete fill scale for plotnine."""
    try:
        from plotnine import scale_fill_manual
    except Exception as exc:  # pragma: no cover
        raise ImportError("plotnine is not installed. Install with: uv add 'calmplots[plotnine]'") from exc
    return scale_fill_manual(values=bluey_palette(name), **kwargs)


def scale_color_calm_c(name: str = "bluey_seq", **kwargs):
    """Continuous color scale for plotnine."""
    try:
        from plotnine import scale_color_gradientn
    except Exception as exc:  # pragma: no cover
        raise ImportError("plotnine is not installed. Install with: uv add 'calmplots[plotnine]'") from exc
    return scale_color_gradientn(colors=continuous_palette(name), **kwargs)


def scale_fill_calm_c(name: str = "bluey_seq", **kwargs):
    """Continuous fill scale for plotnine."""
    try:
        from plotnine import scale_fill_gradientn
    except Exception as exc:  # pragma: no cover
        raise ImportError("plotnine is not installed. Install with: uv add 'calmplots[plotnine]'") from exc
    return scale_fill_gradientn(colors=continuous_palette(name), **kwargs)
