"""Small Plotly demo with calmplots template."""

from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.express as px

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
    fig.write_html("examples/gallery/plotly_scatter.html")


if __name__ == "__main__":
    main()
