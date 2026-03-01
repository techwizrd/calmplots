"""Color-vision-deficiency helpers and accessibility checks."""

from __future__ import annotations

import math

from .utils import contrast_ratio, hex_to_rgb

_IDENTITY = (
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
)

# Machado et al. 2009 full-severity simulation matrices.
_MACHADO = {
    "protan": (
        (0.152286, 1.052583, -0.204868),
        (0.114503, 0.786281, 0.099216),
        (-0.003882, -0.048116, 1.051998),
    ),
    "deutan": (
        (0.367322, 0.860646, -0.227968),
        (0.280085, 0.672501, 0.047413),
        (-0.011820, 0.042940, 0.968881),
    ),
    "tritan": (
        (1.255528, -0.076749, -0.178779),
        (-0.078411, 0.930809, 0.147602),
        (0.004733, 0.691367, 0.303900),
    ),
}


def _clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _mix_matrix(
    deficiency: str, severity: float
) -> tuple[tuple[float, float, float], ...]:
    if deficiency not in _MACHADO:
        raise ValueError(
            f"Unknown deficiency '{deficiency}'. Expected one of: {tuple(_MACHADO)}"
        )
    s = _clamp01(severity)
    out: list[tuple[float, float, float]] = []
    for id_row, cvd_row in zip(_IDENTITY, _MACHADO[deficiency]):
        out.append(
            (
                (1.0 - s) * id_row[0] + s * cvd_row[0],
                (1.0 - s) * id_row[1] + s * cvd_row[1],
                (1.0 - s) * id_row[2] + s * cvd_row[2],
            )
        )
    return tuple(out)


def _apply_matrix(
    rgb: tuple[float, float, float], matrix: tuple[tuple[float, float, float], ...]
) -> tuple[float, float, float]:
    r, g, b = rgb
    row0, row1, row2 = matrix
    rr = _clamp01(row0[0] * r + row0[1] * g + row0[2] * b)
    gg = _clamp01(row1[0] * r + row1[1] * g + row1[2] * b)
    bb = _clamp01(row2[0] * r + row2[1] * g + row2[2] * b)
    return rr, gg, bb


def _to_linear(channel: float) -> float:
    if channel <= 0.04045:
        return channel / 12.92
    return ((channel + 0.055) / 1.055) ** 2.4


def _linrgb_to_oklab(rgb: tuple[float, float, float]) -> tuple[float, float, float]:
    r, g, b = rgb
    l_comp = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m_comp = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s_comp = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b

    l_ = l_comp ** (1.0 / 3.0)
    m_ = m_comp ** (1.0 / 3.0)
    s_ = s_comp ** (1.0 / 3.0)

    ll = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    aa = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    bb = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    return ll, aa, bb


def _hex_to_oklab(hex_color: str) -> tuple[float, float, float]:
    srgb = hex_to_rgb(hex_color)
    lin = (_to_linear(srgb[0]), _to_linear(srgb[1]), _to_linear(srgb[2]))
    return _linrgb_to_oklab(lin)


def _oklab_distance(
    a: tuple[float, float, float], b: tuple[float, float, float]
) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def simulate_cvd_hex(hex_color: str, deficiency: str, severity: float = 1.0) -> str:
    """Simulate how a hex color appears under CVD."""
    matrix = _mix_matrix(deficiency, severity)
    rgb = hex_to_rgb(hex_color)
    rr, gg, bb = _apply_matrix(rgb, matrix)
    return (
        f"#{int(rr * 255 + 0.5):02x}{int(gg * 255 + 0.5):02x}{int(bb * 255 + 0.5):02x}"
    )


def min_pairwise_oklab_distance(
    hex_colors: list[str], include_cvd: bool = True
) -> float:
    """Return minimum pairwise distance in OKLab across optional CVD modes."""
    if len(hex_colors) < 2:
        return 0.0

    modes: list[tuple[str, float] | None] = [None]
    if include_cvd:
        modes.extend(
            [
                ("protan", 0.6),
                ("protan", 1.0),
                ("deutan", 0.6),
                ("deutan", 1.0),
                ("tritan", 0.6),
                ("tritan", 1.0),
            ]
        )

    min_d = float("inf")
    for i in range(len(hex_colors)):
        for j in range(i + 1, len(hex_colors)):
            a = hex_colors[i]
            b = hex_colors[j]
            for mode in modes:
                if mode is None:
                    aa = _hex_to_oklab(a)
                    bb = _hex_to_oklab(b)
                else:
                    deficiency, severity = mode
                    aa = _hex_to_oklab(simulate_cvd_hex(a, deficiency, severity))
                    bb = _hex_to_oklab(simulate_cvd_hex(b, deficiency, severity))
                min_d = min(min_d, _oklab_distance(aa, bb))
    return min_d


def palette_accessibility_report(
    hex_colors: list[str], background: str
) -> dict[str, float | bool]:
    """Compute a lightweight report for palette separation and contrast."""
    min_distance = min_pairwise_oklab_distance(hex_colors, include_cvd=True)
    min_contrast = min(contrast_ratio(color, background) for color in hex_colors)
    return {
        "min_pairwise_oklab_distance": min_distance,
        "min_contrast_to_background": min_contrast,
        "distance_ok": min_distance >= 0.08,
        "contrast_ok": min_contrast >= 2.0,
    }
