from __future__ import annotations

from io import BytesIO

import pytest

pytestmark = pytest.mark.integration


def test_matplotlib_exports_png_and_svg_have_content():
    plt = pytest.importorskip("matplotlib.pyplot")
    np = pytest.importorskip("numpy")
    from calmplots import apply_matplotlib_theme

    apply_matplotlib_theme(theme="light", palette="bluey")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y)
    ax.set_title("export test")

    png = BytesIO()
    svg = BytesIO()
    fig.savefig(png, format="png", dpi=120)
    fig.savefig(svg, format="svg")
    plt.close(fig)

    png_bytes = png.getvalue()
    svg_text = svg.getvalue().decode("utf-8", errors="ignore")

    assert len(png_bytes) > 5_000
    assert "<svg" in svg_text
