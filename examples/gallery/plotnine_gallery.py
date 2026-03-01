"""Small Plotnine demo with calmplots theme."""

from __future__ import annotations

import numpy as np
import pandas as pd
from plotnine import aes, geom_point, ggplot, labs

import calmplots


def main() -> None:
    rng = np.random.default_rng(21)
    df = pd.DataFrame(
        {
            "x": rng.normal(size=220),
            "y": rng.normal(size=220) + np.linspace(-0.8, 0.8, 220),
            "cat": rng.choice(list("ABCD"), size=220),
        }
    )

    p = (
        ggplot(df, aes("x", "y", color="cat"))
        + geom_point(size=2.4, alpha=0.9)
        + calmplots.scale_color_calm()
        + calmplots.theme_calm()
        + labs(title="calmplots Plotnine Scatter")
    )
    p.save("examples/gallery/plotnine_scatter.png", width=9, height=6, dpi=160)
    p.save("examples/gallery/plotnine_scatter.svg", width=9, height=6)


if __name__ == "__main__":
    main()
