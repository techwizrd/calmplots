"""Render a small gallery of common plot types with calmplots."""

from __future__ import annotations

import numpy as np
import pandas as pd

import calmplots


def main() -> None:
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.pyplot as plt
    import seaborn as sns

    rng = np.random.default_rng(42)
    calmplots.apply_matplotlib_theme()
    calmplots.set_seaborn_theme(context="notebook")

    n = 300
    df = pd.DataFrame(
        {
            "x": rng.normal(size=n),
            "y": rng.normal(size=n) + np.linspace(-1, 1, n),
            "cat": rng.choice(list("ABCD"), size=n),
            "grp": rng.choice(["g1", "g2"], size=n),
        }
    )

    fig, axes = plt.subplots(4, 2, figsize=(12, 16), constrained_layout=True)

    sns.lineplot(data=df.sort_values("x"), x="x", y="y", hue="grp", ax=axes[0, 0])
    axes[0, 0].set_title("Line")

    sns.scatterplot(data=df, x="x", y="y", hue="cat", ax=axes[0, 1])
    axes[0, 1].set_title("Scatter")

    sns.countplot(data=df, x="cat", ax=axes[1, 0])
    axes[1, 0].set_title("Bar")

    stacked = pd.crosstab(df["cat"], df["grp"])
    stacked.plot(kind="bar", stacked=True, ax=axes[1, 1])
    axes[1, 1].set_title("Stacked Bar")

    heat = pd.crosstab(df["cat"], df["grp"])
    heatmap_cmap = LinearSegmentedColormap.from_list(
        "calmplots_bluey_seq", calmplots.continuous_palette("bluey_seq")
    )
    sns.heatmap(heat, annot=True, fmt="d", cmap=heatmap_cmap, ax=axes[2, 0])
    axes[2, 0].set_title("Heatmap")

    sns.violinplot(data=df, x="cat", y="y", ax=axes[2, 1], inner=None)
    sns.boxplot(data=df, x="cat", y="y", ax=axes[2, 1], width=0.2)
    axes[2, 1].set_title("Violin + Box")

    sns.histplot(data=df, x="x", hue="grp", bins=24, ax=axes[3, 0], element="step")
    axes[3, 0].set_title("Histogram")

    sns.scatterplot(data=df, x="x", y="y", hue="grp", style="cat", ax=axes[3, 1])
    axes[3, 1].set_title("Grouped Scatter")

    fig.savefig("examples/gallery/gallery_matplotlib.png", dpi=140)
    fig.savefig("examples/gallery/gallery_matplotlib.svg")
    fig.savefig("examples/gallery/gallery_matplotlib.pdf")

    g = sns.FacetGrid(df, col="cat", hue="grp", height=2.2)
    g.map_dataframe(sns.scatterplot, x="x", y="y")
    g.add_legend()
    g.savefig("examples/gallery/gallery_facet.png", dpi=140)


if __name__ == "__main__":
    main()
