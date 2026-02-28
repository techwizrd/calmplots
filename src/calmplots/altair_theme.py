"""Altair theme registration for calmplots."""

from __future__ import annotations

from typing import Any

try:
    from typing import LiteralString
except ImportError:  # pragma: no cover
    from typing_extensions import LiteralString

from .palettes import bluey_palette, continuous_palette
from .tokens import get_tokens


def _altair_theme_config(theme: str = "light") -> dict[str, Any]:
    t = get_tokens(theme)
    return {
        "config": {
            "background": t["background"],
            "view": {
                "continuousWidth": 400,
                "continuousHeight": 280,
                "stroke": t["panel_background"],
                "fill": t["panel_background"],
            },
            "axis": {
                "labelColor": t["muted_foreground"],
                "titleColor": t["foreground"],
                "grid": True,
                "gridColor": t["grid_major"],
                "domainColor": t["grid_major"],
                "tickColor": t["grid_major"],
            },
            "title": {"color": t["foreground"], "fontSize": 15},
            "legend": {"labelColor": t["muted_foreground"], "titleColor": t["foreground"]},
            "range": {
                "category": bluey_palette("bluey10"),
                "heatmap": continuous_palette("bluey_seq"),
                "diverging": continuous_palette("bluey_div"),
            },
        }
    }


def register_altair_theme(name: LiteralString = "calmplots", theme: str = "light") -> str:
    """Register calmplots altair theme under a name."""
    try:
        import altair as alt
    except Exception as exc:  # pragma: no cover
        raise ImportError("altair is not installed. Install with: uv add 'calmplots[altair]'") from exc

    if hasattr(alt, "theme") and hasattr(alt.theme, "register"):

        @alt.theme.register(name, enable=False)
        def _theme_fn() -> Any:
            return _altair_theme_config(theme=theme)

    else:  # pragma: no cover
        def _legacy_theme_fn() -> Any:
            return _altair_theme_config(theme=theme)

        alt.themes.register(name, _legacy_theme_fn)
    return name


def enable_altair_theme(name: LiteralString = "calmplots", theme: str = "light") -> str:
    """Register and enable the calmplots altair theme."""
    try:
        import altair as alt
    except Exception as exc:  # pragma: no cover
        raise ImportError("altair is not installed. Install with: uv add 'calmplots[altair]'") from exc

    register_altair_theme(name=name, theme=theme)
    if hasattr(alt, "theme") and hasattr(alt.theme, "enable"):
        alt.theme.enable(name)
    else:  # pragma: no cover
        alt.themes.enable(name)
    return name
