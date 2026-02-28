"""Small Altair demo with calmplots theme."""

from __future__ import annotations

import numpy as np
import pandas as pd
import altair as alt

import calmplots


def main() -> None:
    calmplots.enable_altair_theme()
    rng = np.random.default_rng(11)
    df = pd.DataFrame(
        {
            "x": rng.normal(size=150),
            "y": rng.normal(size=150),
            "cat": rng.choice(list("ABC"), size=150),
        }
    )
    chart = (
        alt.Chart(df)
        .mark_circle(size=65)
        .encode(x="x", y="y", color="cat")
        .properties(title="calmplots Altair Scatter")
    )
    chart.save("examples/gallery/altair_scatter.html")


if __name__ == "__main__":
    main()
