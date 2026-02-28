"""Semantic design tokens shared across backends."""

from __future__ import annotations

from copy import deepcopy
from types import MappingProxyType

_TOKENS = {
    "light": {
        "background": "#f7f9fc",
        "panel_background": "#f0f4fa",
        "foreground": "#24364b",
        "muted_foreground": "#5e738a",
        "grid_major": "#d8e1ec",
        "grid_minor": "#e7edf5",
        "accent": "#30598a",
    },
    "dark": {
        "background": "#1f2631",
        "panel_background": "#253040",
        "foreground": "#e8eef7",
        "muted_foreground": "#b5c2d4",
        "grid_major": "#3b4a61",
        "grid_minor": "#324056",
        "accent": "#72bfed",
    },
}

TOKENS = MappingProxyType(
    {name: MappingProxyType(values) for name, values in _TOKENS.items()}
)


def get_tokens(theme: str = "light") -> dict[str, str]:
    """Return a copy of semantic tokens for a theme."""
    if theme not in _TOKENS:
        raise ValueError(f"Unknown theme '{theme}'. Available: {tuple(_TOKENS)}")
    return deepcopy(_TOKENS[theme])
