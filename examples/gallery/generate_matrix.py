"""Generate gallery matrix across themes, palettes, and backends."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from _plotly_export import write_image_safely

import calmplots

THEMES = ["light", "dark"]
BASE_PALETTES = ["bluey", "chilli", "heeler", "socks", "colorblind"]
EXTENDED_PALETTES = ["bluey10"]
LIBRARIES = ["matplotlib_seaborn", "plotnine", "plotly", "altair"]


def _matrix_dir(theme: str, palette: str, library: str) -> Path:
    path = Path("examples/gallery/matrix") / theme / palette / library
    path.mkdir(parents=True, exist_ok=True)
    return path


def _sample_data(seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    n = 260
    return pd.DataFrame(
        {
            "x": rng.normal(size=n),
            "y": rng.normal(size=n) + np.linspace(-1, 1, n),
            "cat": rng.choice(list("ABCD"), size=n),
        }
    )


def _render_matplotlib_seaborn(
    theme: str, palette: str, out_dir: Path, df: pd.DataFrame
) -> list[str]:
    import matplotlib.pyplot as plt
    import seaborn as sns

    calmplots.apply_matplotlib_theme(theme=theme, palette=palette)
    calmplots.set_seaborn_theme(theme=theme, palette=palette)

    fig, ax = plt.subplots(figsize=(9, 6), constrained_layout=True)
    sns.scatterplot(data=df, x="x", y="y", hue="cat", ax=ax)
    ax.set_title(f"Matplotlib/Seaborn - {theme} - {palette}")

    png = out_dir / "scatter.png"
    svg = out_dir / "scatter.svg"
    fig.savefig(png, dpi=160)
    fig.savefig(svg)
    plt.close(fig)
    return [str(png), str(svg)]


def _render_plotnine(
    theme: str, palette: str, out_dir: Path, df: pd.DataFrame
) -> list[str]:
    from plotnine import aes, geom_point, ggplot, labs

    p = (
        ggplot(df, aes("x", "y", color="cat"))
        + geom_point(size=2.3, alpha=0.9)
        + calmplots.scale_color_calm(name=palette)
        + calmplots.theme_calm(theme=theme)
        + labs(title=f"Plotnine - {theme} - {palette}")
    )

    png = out_dir / "scatter.png"
    svg = out_dir / "scatter.svg"
    p.save(str(png), width=9, height=6, dpi=160)
    p.save(str(svg), width=9, height=6)
    return [str(png), str(svg)]


def _render_plotly(
    theme: str,
    palette: str,
    out_dir: Path,
    df: pd.DataFrame,
    failures: list[str],
) -> list[str]:
    import plotly.express as px

    template_name = f"calmplots_{theme}_{palette}"
    calmplots.register_plotly_template(
        name=template_name, theme=theme, discrete=palette, set_default=False
    )

    fig = px.scatter(
        df,
        x="x",
        y="y",
        color="cat",
        title=f"Plotly - {theme} - {palette}",
        template=template_name,
    )

    generated: list[str] = []
    png = out_dir / "scatter.png"
    svg = out_dir / "scatter.svg"

    if write_image_safely(fig, str(png), width=900, height=600, scale=2):
        generated.append(str(png))

    if write_image_safely(fig, str(svg), width=900, height=600, scale=1):
        generated.append(str(svg))
    else:
        failures.append(f"plotly static export unavailable {theme}/{palette}")
    return generated


def _render_altair(
    theme: str,
    palette: str,
    out_dir: Path,
    df: pd.DataFrame,
    failures: list[str],
) -> list[str]:
    import altair as alt

    theme_name = f"calmplots_{theme}_{palette}".replace("-", "_")
    calmplots.enable_altair_theme(name=theme_name, theme=theme, discrete=palette)

    chart = (
        alt.Chart(df)
        .mark_circle(size=65)
        .encode(x="x", y="y", color="cat")
        .properties(title=f"Altair - {theme} - {palette}")
    )

    generated: list[str] = []
    png = out_dir / "scatter.png"
    svg = out_dir / "scatter.svg"
    try:
        chart.save(str(png))
        generated.append(str(png))
    except Exception as exc:
        failures.append(f"altair png {theme}/{palette}: {exc}")

    try:
        chart.save(str(svg))
        generated.append(str(svg))
    except Exception as exc:
        failures.append(f"altair svg {theme}/{palette}: {exc}")
    return generated


def _render_combo(
    theme: str, palette: str, df: pd.DataFrame, failures: list[str]
) -> list[str]:
    generated: list[str] = []
    generated.extend(
        _render_matplotlib_seaborn(
            theme, palette, _matrix_dir(theme, palette, "matplotlib_seaborn"), df
        )
    )
    generated.extend(
        _render_plotnine(theme, palette, _matrix_dir(theme, palette, "plotnine"), df)
    )
    generated.extend(
        _render_plotly(
            theme, palette, _matrix_dir(theme, palette, "plotly"), df, failures
        )
    )
    generated.extend(
        _render_altair(
            theme, palette, _matrix_dir(theme, palette, "altair"), df, failures
        )
    )
    return generated


def _write_index(paths: list[str], palettes: list[str], include_extended: bool) -> None:
    lines = [
        "# Gallery Matrix",
        "",
        "Generated outputs by theme, palette, and backend.",
        "",
        "Each row links directly to repository artifacts using relative paths.",
        "",
    ]
    for theme in THEMES:
        lines.append(f"## {theme.title()}")
        lines.append("")
        for palette in palettes:
            lines.append(f"### {palette}")
            lines.append(
                "- Matplotlib/Seaborn: "
                f"[PNG]({theme}/{palette}/matplotlib_seaborn/scatter.png) | "
                f"[SVG]({theme}/{palette}/matplotlib_seaborn/scatter.svg)"
            )
            lines.append(
                "- Plotnine: "
                f"[PNG]({theme}/{palette}/plotnine/scatter.png) | "
                f"[SVG]({theme}/{palette}/plotnine/scatter.svg)"
            )
            lines.append(
                "- Plotly: "
                f"[PNG]({theme}/{palette}/plotly/scatter.png) | "
                f"[SVG]({theme}/{palette}/plotly/scatter.svg)"
            )
            lines.append(
                "- Altair: "
                f"[PNG]({theme}/{palette}/altair/scatter.png) | "
                f"[SVG]({theme}/{palette}/altair/scatter.svg)"
            )
            lines.append("")

    lines.append("## Notes")
    lines.append("")
    if include_extended:
        lines.append("- Includes extended palette: `bluey10`.")
    else:
        lines.append(
            "- Includes only base palettes from blueycolors plus `colorblind`."
        )
    lines.append(
        "- For a complete palette swatch overview, see "
        "`examples/gallery/palettes_light.png` and `examples/gallery/palettes_dark.png`."
    )
    lines.append(
        "- Generated files are intentionally not listed inline to keep this index compact."
    )
    lines.append(
        "- Re-run `python examples/gallery/generate_matrix.py` to refresh outputs."
    )

    index_path = Path("examples/gallery/matrix/README.md")
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate calmplots matrix gallery")
    parser.add_argument(
        "--extended",
        action="store_true",
        help="Include extended palettes such as bluey10",
    )
    args = parser.parse_args()

    palettes = list(BASE_PALETTES)
    if args.extended:
        palettes.extend(EXTENDED_PALETTES)

    all_paths: list[str] = []
    failures: list[str] = []
    for theme in THEMES:
        for palette in palettes:
            all_paths.extend(
                _render_combo(theme, palette, _sample_data(seed=11), failures)
            )
    _write_index(all_paths, palettes, include_extended=args.extended)
    print(f"Generated {len(all_paths)} files in examples/gallery/matrix")
    if failures:
        print("\nExport failures:")
        for item in failures:
            print(f"- {item}")


if __name__ == "__main__":
    main()
