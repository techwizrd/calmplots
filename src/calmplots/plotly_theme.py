"""Plotly template integration for calmplots."""

from __future__ import annotations

from .palettes import bluey_palette, continuous_palette
from .tokens import get_tokens


def _scale_entries(colors: list[str]) -> list[list[float | str]]:
    if len(colors) == 1:
        return [[0.0, colors[0]]]
    step = 1 / (len(colors) - 1)
    return [[i * step, color] for i, color in enumerate(colors)]


def build_plotly_template(theme: str = "light", discrete: str = "bluey10"):
    """Return a plotly template object configured with calmplots tokens."""
    try:
        import plotly.graph_objects as go
    except Exception as exc:  # pragma: no cover
        raise ImportError("plotly is not installed. Install with: uv add 'calmplots[plotly]'") from exc

    t = get_tokens(theme)
    seq = continuous_palette("bluey_seq")
    div = continuous_palette("bluey_div")
    return go.layout.Template(
        layout={
            "paper_bgcolor": t["background"],
            "plot_bgcolor": t["panel_background"],
            "font": {"color": t["foreground"], "size": 13},
            "colorway": bluey_palette(discrete),
            "xaxis": {
                "gridcolor": t["grid_major"],
                "linecolor": t["grid_major"],
                "zerolinecolor": t["grid_major"],
                "tickcolor": t["muted_foreground"],
                "title": {"font": {"color": t["foreground"]}},
            },
            "yaxis": {
                "gridcolor": t["grid_major"],
                "linecolor": t["grid_major"],
                "zerolinecolor": t["grid_major"],
                "tickcolor": t["muted_foreground"],
                "title": {"font": {"color": t["foreground"]}},
            },
            "colorscale": {
                "sequential": _scale_entries(seq),
                "diverging": _scale_entries(div),
            },
        }
    )


def register_plotly_template(
    name: str = "calmplots",
    theme: str = "light",
    discrete: str = "bluey10",
    set_default: bool = True,
) -> str:
    """Register calmplots as a plotly template and optionally set default."""
    try:
        import plotly.io as pio
    except Exception as exc:  # pragma: no cover
        raise ImportError("plotly is not installed. Install with: uv add 'calmplots[plotly]'") from exc

    pio.templates[name] = build_plotly_template(theme=theme, discrete=discrete)
    if set_default:
        pio.templates.default = name
    return name
