"""Small Plotly demo with calmplots template."""

from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.express as px
from _plotly_export import write_image_safely

import calmplots


def main() -> None:
    calmplots.register_plotly_template(set_default=True)
    rng = np.random.default_rng(7)
    df = pd.DataFrame(
        {
            "x": rng.normal(size=160),
            "y": rng.normal(size=160),
            "cat": rng.choice(list("ABCD"), size=160),
        }
    )
    fig = px.scatter(df, x="x", y="y", color="cat", title="calmplots Plotly Scatter")
    write_image_safely(
        fig,
        "examples/gallery/plotly_scatter.png",
        width=900,
        height=600,
        scale=2,
    )
    write_image_safely(
        fig,
        "examples/gallery/plotly_scatter.svg",
        width=900,
        height=600,
        scale=1,
    )


if __name__ == "__main__":
    main()
