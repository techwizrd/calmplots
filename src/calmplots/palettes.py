"""Color palette registry and helper functions."""

from __future__ import annotations

# Inspired by ekholme/blueycolors
BLUEY_SOURCE = {
    "bluey": ["#d2ebff", "#88cafc", "#404066", "#2b2c41", "#edcc6f"],
    "chilli": ["#fffad8", "#ffd08d", "#ffb070", "#9c5e33", "#46362a"],
    "heeler": ["#30598a", "#72bfed", "#e4dcbd", "#f1b873", "#e27a37"],
    "socks": ["#8f9fd8", "#201a3f", "#a97d45", "#c3cae1", "#3e2b0b"],
}

PALETTES = {
    "bluey10": [
        "#30598a",
        "#72bfed",
        "#e27a37",
        "#404066",
        "#edcc6f",
        "#8f9fd8",
        "#9c5e33",
        "#2b2c41",
        "#88cafc",
        "#a97d45",
    ],
    "bluey": BLUEY_SOURCE["bluey"],
    "chilli": BLUEY_SOURCE["chilli"],
    "heeler": BLUEY_SOURCE["heeler"],
    "socks": BLUEY_SOURCE["socks"],
    "colorblind": [
        "#0072B2",
        "#E69F00",
        "#009E73",
        "#D55E00",
        "#CC79A7",
        "#56B4E9",
        "#F0E442",
        "#000000",
    ],
    "colorblind_dark": [
        "#56B4E9",
        "#E69F00",
        "#009E73",
        "#D55E00",
        "#CC79A7",
        "#7FD6FF",
        "#F0E442",
        "#F2F4F8",
    ],
    "accessible8_light": [
        "#4303af",
        "#cd9c1f",
        "#8d180e",
        "#4a84cc",
        "#5a6a09",
        "#cf2872",
        "#3dbca7",
        "#6e086b",
    ],
    "accessible8_dark": [
        "#23f792",
        "#6d65fe",
        "#e62b34",
        "#9da2fb",
        "#a38528",
        "#fcac11",
        "#2a9c91",
        "#37c6a8",
    ],
}

CONTINUOUS = {
    "bluey_seq": ["#eaf4ff", "#bcdffb", "#72bfed", "#3b7eb6", "#2b2c41"],
    "sunset_seq": ["#fff4d7", "#ffd08d", "#f1b873", "#e27a37", "#9c5e33"],
    "bluey_div": ["#2b2c41", "#72bfed", "#f0f4fa", "#f1b873", "#9c5e33"],
}


def _validate_n(n: int) -> None:
    if n <= 0:
        raise ValueError("n must be >= 1")


def list_palettes() -> list[str]:
    """List available discrete palettes."""
    return sorted(PALETTES.keys())


def bluey_palette(name: str = "bluey10", n: int | None = None) -> list[str]:
    """Return a discrete palette by name.

    If n is provided, colors are truncated to the first n entries.
    """
    if name not in PALETTES:
        raise ValueError(f"Unknown palette '{name}'. Available: {list_palettes()}")
    colors = list(PALETTES[name])
    if n is None:
        return colors
    _validate_n(n)
    if n > len(colors):
        raise ValueError(
            f"Palette '{name}' has only {len(colors)} colors; requested {n}."
        )
    return colors[:n]


def _resolve_palette_name(name: str, theme: str) -> str:
    if name == "colorblind" and theme == "dark":
        return "colorblind_dark"
    return name


def themed_palette(
    name: str = "bluey10", theme: str = "light", n: int | None = None
) -> list[str]:
    """Return palette with theme-aware substitutions when needed."""
    return bluey_palette(_resolve_palette_name(name, theme), n=n)


def colorblind_palette(n: int | None = None, theme: str = "light") -> list[str]:
    """Return colorblind palette, with dark-theme substitution when needed."""
    return themed_palette("colorblind", theme=theme, n=n)


def accessible_palette(theme: str = "light", n: int | None = None) -> list[str]:
    """Return a CVD-optimized categorical palette for light or dark themes."""
    name = "accessible8_light" if theme == "light" else "accessible8_dark"
    return bluey_palette(name, n=n)


def continuous_palette(name: str = "bluey_seq") -> list[str]:
    """Return a continuous palette anchor list."""
    if name not in CONTINUOUS:
        raise ValueError(
            f"Unknown continuous palette '{name}'. Available: {sorted(CONTINUOUS)}"
        )
    return list(CONTINUOUS[name])
