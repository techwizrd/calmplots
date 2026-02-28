"""Seaborn integration for calmplots."""

from __future__ import annotations

from typing import Literal

from .matplotlib_theme import matplotlib_rcparams
from .palettes import bluey_palette, continuous_palette


def set_seaborn_theme(
    context: Literal["paper", "notebook", "talk", "poster"] = "notebook",
    theme: str = "light",
    palette: str = "bluey10",
) -> dict:
    """Apply calmplots defaults through seaborn.set_theme()."""
    try:
        import seaborn as sns
    except Exception as exc:  # pragma: no cover
        raise ImportError("seaborn is not installed. Install with: uv add 'calmplots[seaborn]'") from exc

    rc = matplotlib_rcparams(theme=theme, palette=palette)
    sns.set_theme(
        context=context,
        style="whitegrid",
        palette=bluey_palette(palette),
        rc=rc,
    )
    return rc


def seaborn_discrete_palette(name: str = "bluey10") -> list[str]:
    """Return a seaborn-ready categorical palette list."""
    return bluey_palette(name)


def seaborn_continuous_palette(name: str = "bluey_seq") -> list[str]:
    """Return a seaborn/matplotlib continuous scale anchor list."""
    return continuous_palette(name)
