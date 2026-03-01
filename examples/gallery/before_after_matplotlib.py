"""Generate a small before/after comparison for README."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import calmplots


def _sample_df(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    n = 140
    return pd.DataFrame(
        {
            "x": rng.normal(size=n),
            "y": rng.normal(size=n) + np.linspace(-0.8, 0.8, n),
            "cat": rng.choice(list("ABCD"), size=n),
        }
    )


def _save_default(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(7, 4.5), constrained_layout=True)
    for category in sorted(df["cat"].unique()):
        sub = df[df["cat"] == category]
        ax.scatter(sub["x"], sub["y"], label=category, alpha=0.8)
    ax.set_title("Default Matplotlib")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(title="cat")
    fig.savefig("examples/gallery/before_default_scatter.png", dpi=140)
    plt.close(fig)


def _save_calmplots(df: pd.DataFrame) -> None:
    calmplots.apply_matplotlib_theme(theme="light", palette="bluey")
    fig, ax = plt.subplots(figsize=(7, 4.5), constrained_layout=True)
    for category in sorted(df["cat"].unique()):
        sub = df[df["cat"] == category]
        ax.scatter(sub["x"], sub["y"], label=category, alpha=0.85)
    ax.set_title("calmplots (bluey)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(title="cat")
    fig.savefig("examples/gallery/before_calmplots_scatter.png", dpi=140)
    plt.close(fig)


def main() -> None:
    df = _sample_df()
    _save_default(df)
    _save_calmplots(df)


if __name__ == "__main__":
    main()
