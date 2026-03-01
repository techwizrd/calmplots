"""Generate compact palette swatch galleries for README/docs."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from calmplots.palettes import PALETTES, bluey_palette


def _draw_palette_gallery(background: str, text: str, output_base: Path) -> None:
    names = sorted(PALETTES)
    max_colors = max(len(bluey_palette(name)) for name in names)

    cell_w = 1.0
    row_h = 0.78
    label_w = 3.6

    width = label_w + max_colors * cell_w + 0.8
    height = row_h * len(names) + 0.8
    fig, ax = plt.subplots(
        figsize=(width * 0.7, height * 0.55), constrained_layout=True
    )

    fig.patch.set_facecolor(background)
    ax.set_facecolor(background)

    for row, name in enumerate(names):
        y = len(names) - row - 1
        ax.text(
            0.15,
            y + 0.35,
            name,
            color=text,
            fontsize=10,
            va="center",
            ha="left",
            family="DejaVu Sans",
        )
        colors = bluey_palette(name)
        for i, color in enumerate(colors):
            x = label_w + i * cell_w
            rect = plt.Rectangle((x, y), 0.88, 0.68, color=color, ec=background, lw=0.7)
            ax.add_patch(rect)

    ax.set_xlim(0, width - 0.2)
    ax.set_ylim(0, len(names) + 0.2)
    ax.axis("off")

    output_base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_base.with_suffix(".png"), dpi=180)
    fig.savefig(output_base.with_suffix(".svg"))
    plt.close(fig)


def main() -> None:
    _draw_palette_gallery(
        background="#f7f9fc",
        text="#24364b",
        output_base=Path("examples/gallery/palettes_light"),
    )
    _draw_palette_gallery(
        background="#1f2631",
        text="#e8eef7",
        output_base=Path("examples/gallery/palettes_dark"),
    )


if __name__ == "__main__":
    main()
