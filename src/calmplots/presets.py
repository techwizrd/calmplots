"""Convenience cross-library presets."""

from __future__ import annotations

from typing import Literal

from .matplotlib_theme import apply_matplotlib_theme
from .seaborn_theme import set_seaborn_theme


def apply_notebook_theme(
    theme: str = "light",
    palette: str = "bluey10",
    context: Literal["paper", "notebook", "talk", "poster"] = "notebook",
) -> dict:
    """Apply a sensible notebook baseline for matplotlib and seaborn."""
    mpl = apply_matplotlib_theme(theme=theme, palette=palette)
    sns = set_seaborn_theme(context=context, theme=theme, palette=palette)
    return {"matplotlib": mpl, "seaborn": sns}
