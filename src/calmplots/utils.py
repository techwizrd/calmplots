"""Utility functions for color conversion and contrast checks."""

from __future__ import annotations


def hex_to_rgb(hex_color: str) -> tuple[float, float, float]:
    """Convert #RRGGBB into floats in [0, 1]."""
    c = hex_color.strip().lstrip("#")
    if len(c) != 6:
        raise ValueError(f"Expected #RRGGBB hex color, got: {hex_color}")
    r = int(c[0:2], 16) / 255.0
    g = int(c[2:4], 16) / 255.0
    b = int(c[4:6], 16) / 255.0
    return r, g, b


def _srgb_to_linear(v: float) -> float:
    if v <= 0.04045:
        return v / 12.92
    return ((v + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_color: str) -> float:
    """Compute WCAG relative luminance for a hex color."""
    r, g, b = hex_to_rgb(hex_color)
    rl = _srgb_to_linear(r)
    gl = _srgb_to_linear(g)
    bl = _srgb_to_linear(b)
    return 0.2126 * rl + 0.7152 * gl + 0.0722 * bl


def contrast_ratio(color_a: str, color_b: str) -> float:
    """Compute WCAG contrast ratio between two colors."""
    la = relative_luminance(color_a)
    lb = relative_luminance(color_b)
    lighter = max(la, lb)
    darker = min(la, lb)
    return (lighter + 0.05) / (darker + 0.05)


def contrast_sanity(
    text: str, background: str, line: str, grid: str
) -> dict[str, float | bool]:
    """Return basic contrast checks used for visual sanity validation."""
    text_bg = contrast_ratio(text, background)
    line_grid = contrast_ratio(line, grid)
    return {
        "text_vs_bg": text_bg,
        "line_vs_grid": line_grid,
        "text_ok": text_bg >= 4.5,
        "line_ok": line_grid >= 1.5,
    }
