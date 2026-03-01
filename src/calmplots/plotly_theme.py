"""Plotly template integration for calmplots."""

from __future__ import annotations

from copy import deepcopy

from .palettes import continuous_palette, themed_palette
from .tokens import get_tokens


def _scale_entries(colors: list[str]) -> list[list[float | str]]:
    if len(colors) == 1:
        return [[0.0, colors[0]]]
    step = 1 / (len(colors) - 1)
    return [[i * step, color] for i, color in enumerate(colors)]


def _colorbar_style(tokens: dict[str, str]) -> dict:
    return {
        "tickfont": {"color": tokens["muted_foreground"]},
        "title": {"font": {"color": tokens["foreground"]}},
        "outlinecolor": tokens["grid_major"],
    }


def _axis_style(tokens: dict[str, str]) -> dict:
    return {
        "gridcolor": tokens["grid_major"],
        "linecolor": tokens["grid_major"],
        "zerolinecolor": tokens["grid_major"],
        "tickcolor": tokens["muted_foreground"],
        "tickfont": {"color": tokens["muted_foreground"]},
        "title": {"font": {"color": tokens["foreground"]}},
    }


def _non_cartesian_layout(tokens: dict[str, str]) -> dict:
    def axis_style() -> dict:
        return {
            "gridcolor": tokens["grid_major"],
            "linecolor": tokens["grid_major"],
            "tickfont": {"color": tokens["muted_foreground"]},
        }

    def scene_axis_style() -> dict:
        return {
            "backgroundcolor": tokens["panel_background"],
            "gridcolor": tokens["grid_major"],
            "linecolor": tokens["grid_major"],
            "tickfont": {"color": tokens["muted_foreground"]},
            "title": {"font": {"color": tokens["foreground"]}},
        }

    return {
        "polar": {
            "bgcolor": tokens["panel_background"],
            "angularaxis": axis_style(),
            "radialaxis": axis_style(),
        },
        "ternary": {
            "bgcolor": tokens["panel_background"],
            "aaxis": axis_style(),
            "baxis": axis_style(),
            "caxis": axis_style(),
        },
        "scene": {
            "xaxis": scene_axis_style(),
            "yaxis": scene_axis_style(),
            "zaxis": scene_axis_style(),
        },
    }


def _trace_defaults(colorbar_style: dict) -> dict:
    return {
        "heatmap": [{"colorbar": deepcopy(colorbar_style)}],
        "contour": [{"colorbar": deepcopy(colorbar_style)}],
        "surface": [{"colorbar": deepcopy(colorbar_style)}],
        "scatter": [{"marker": {"colorbar": deepcopy(colorbar_style)}}],
        "scattergl": [{"marker": {"colorbar": deepcopy(colorbar_style)}}],
        "scatter3d": [{"marker": {"colorbar": deepcopy(colorbar_style)}}],
    }


def build_plotly_template(theme: str = "light", discrete: str = "bluey10"):
    """Return a plotly template object configured with calmplots tokens."""
    try:
        import plotly.graph_objects as go
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "plotly is not installed. Install with: uv add 'calmplots[plotly]'"
        ) from exc

    t = get_tokens(theme)
    seq = continuous_palette("bluey_seq")
    div = continuous_palette("bluey_div")
    colorbar_style = _colorbar_style(t)
    non_cartesian = _non_cartesian_layout(t)
    trace_defaults = _trace_defaults(colorbar_style)
    return go.layout.Template(
        data=trace_defaults,
        layout={
            "paper_bgcolor": t["background"],
            "plot_bgcolor": t["panel_background"],
            "font": {"color": t["foreground"], "size": 13},
            "colorway": themed_palette(discrete, theme=theme),
            "hoverlabel": {
                "bgcolor": t["panel_background"],
                "font": {"color": t["foreground"]},
                "bordercolor": t["grid_major"],
            },
            "legend": {
                "font": {"color": t["foreground"]},
                "title": {"font": {"color": t["foreground"]}},
                "bgcolor": t["panel_background"],
            },
            "xaxis": _axis_style(t),
            "yaxis": _axis_style(t),
            "colorscale": {
                "sequential": _scale_entries(seq),
                "diverging": _scale_entries(div),
            },
            "coloraxis": {"colorbar": colorbar_style},
            **non_cartesian,
        },
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
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "plotly is not installed. Install with: uv add 'calmplots[plotly]'"
        ) from exc

    pio.templates[name] = build_plotly_template(theme=theme, discrete=discrete)
    if set_default:
        pio.templates.default = name
    return name
