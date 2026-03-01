"""Plotly static export helpers used by gallery scripts."""

from __future__ import annotations

import warnings

_KALEIDO_DEPRECATION_PREFIX = (
    "Support for Kaleido versions less than 1.0.0 is deprecated"
)


def write_image_safely(fig, path: str, *, width: int, height: int, scale: int) -> bool:
    """Write a plotly image while suppressing known Kaleido deprecation noise."""
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message=f"{_KALEIDO_DEPRECATION_PREFIX}.*",
                category=DeprecationWarning,
            )
            fig.write_image(path, width=width, height=height, scale=scale)
        return True
    except Exception as exc:
        print(f"Plotly image export skipped [{path}]: {exc}")
        return False
