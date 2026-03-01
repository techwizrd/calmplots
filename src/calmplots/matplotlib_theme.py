"""Matplotlib integration for calmplots."""

from __future__ import annotations

from importlib import resources

from .palettes import themed_palette
from .tokens import get_tokens


def matplotlib_rcparams(theme: str = "light", palette: str = "bluey10") -> dict:
    """Build rcParams values for the calmplots theme."""
    tokens = get_tokens(theme)
    colors = themed_palette(palette, theme=theme)
    return {
        "figure.facecolor": tokens["background"],
        "axes.facecolor": tokens["panel_background"],
        "savefig.facecolor": tokens["background"],
        "text.color": tokens["foreground"],
        "axes.edgecolor": tokens["grid_major"],
        "axes.labelcolor": tokens["foreground"],
        "axes.titlecolor": tokens["foreground"],
        "axes.titlesize": 14,
        "axes.labelsize": 11,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": tokens["grid_major"],
        "grid.alpha": 1.0,
        "grid.linestyle": "-",
        "grid.linewidth": 0.8,
        "xtick.color": tokens["muted_foreground"],
        "ytick.color": tokens["muted_foreground"],
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.frameon": False,
        "legend.fontsize": 10,
        "legend.labelcolor": tokens["foreground"],
        "legend.edgecolor": tokens["background"],
        "font.size": 11,
        "lines.linewidth": 2.1,
        "lines.markersize": 6,
        "patch.edgecolor": tokens["panel_background"],
        "patch.linewidth": 0.5,
        "axes.prop_cycle": _build_color_cycle(colors),
        "axes.spines.top": False,
        "axes.spines.right": False,
    }


def _build_color_cycle(colors: list[str]):
    try:
        from cycler import cycler
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "The 'cycler' package is required for matplotlib theming."
        ) from exc
    return cycler(color=colors)


def apply_matplotlib_theme(theme: str = "light", palette: str = "bluey10") -> dict:
    """Apply rcParams to the active matplotlib runtime."""
    try:
        import matplotlib as mpl
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "matplotlib is not installed. Install with: uv add 'calmplots[matplotlib]'"
        ) from exc

    rc = matplotlib_rcparams(theme=theme, palette=palette)
    mpl.rcParams.update(rc)
    return rc


def use_matplotlib_stylesheet(theme: str = "light") -> str:
    """Load the packaged .mplstyle stylesheet and return its path."""
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "matplotlib is not installed. Install with: uv add 'calmplots[matplotlib]'"
        ) from exc

    style_name = "calmplots_dark.mplstyle" if theme == "dark" else "calmplots.mplstyle"
    style_resource = resources.files("calmplots").joinpath(f"styles/{style_name}")
    with resources.as_file(style_resource) as style_path:
        plt.style.use(str(style_path))
        return str(style_path)
