"""Seaborn integration for calmplots."""

from __future__ import annotations

from typing import Literal

from .matplotlib_theme import matplotlib_rcparams
from .palettes import continuous_palette, themed_palette


def set_seaborn_theme(
    context: Literal["paper", "notebook", "talk", "poster"] = "notebook",
    theme: str = "light",
    palette: str = "bluey10",
) -> dict:
    """Apply calmplots defaults through seaborn.set_theme()."""
    try:
        import seaborn as sns
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "seaborn is not installed. Install with: uv add 'calmplots[seaborn]'"
        ) from exc

    rc = matplotlib_rcparams(theme=theme, palette=palette)
    style = "darkgrid" if theme == "dark" else "whitegrid"
    sns.set_theme(
        context=context,
        style=style,
        palette=themed_palette(palette, theme=theme),
        rc=rc,
    )
    return rc


def seaborn_discrete_palette(name: str = "bluey10", theme: str = "light") -> list[str]:
    """Return a seaborn-ready categorical palette list."""
    return themed_palette(name, theme=theme)


def seaborn_continuous_palette(name: str = "bluey_seq") -> list[str]:
    """Return a seaborn/matplotlib continuous scale anchor list."""
    return continuous_palette(name)
