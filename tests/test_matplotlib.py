from pathlib import Path

import pytest

pytestmark = pytest.mark.integration


def test_matplotlib_theme_applies_without_error():
    mpl = pytest.importorskip("matplotlib")
    from calmplots import apply_matplotlib_theme

    apply_matplotlib_theme()
    assert mpl.rcParams["axes.grid"] is True


def test_stylesheet_loads():
    pytest.importorskip("matplotlib")
    from calmplots import use_matplotlib_stylesheet

    path = use_matplotlib_stylesheet()
    assert path.endswith("calmplots.mplstyle")

    dark_path = use_matplotlib_stylesheet(theme="dark")
    assert dark_path.endswith("calmplots_dark.mplstyle")


def test_dark_theme_sets_readable_legend_text_color():
    mpl = pytest.importorskip("matplotlib")
    from calmplots import apply_matplotlib_theme

    apply_matplotlib_theme(theme="dark")
    assert mpl.rcParams["text.color"] == "#e8eef7"
    assert mpl.rcParams["legend.labelcolor"] == "#e8eef7"


def test_stylesheet_and_rcparams_share_core_tokens():
    pytest.importorskip("matplotlib")
    from calmplots.matplotlib_theme import matplotlib_rcparams

    checks = [
        "figure.facecolor",
        "axes.facecolor",
        "grid.color",
        "text.color",
        "legend.labelcolor",
    ]

    for theme, style_file in [
        ("light", "src/calmplots/styles/calmplots.mplstyle"),
        ("dark", "src/calmplots/styles/calmplots_dark.mplstyle"),
    ]:
        rc = matplotlib_rcparams(theme=theme)
        style_values: dict[str, str] = {}
        style_path = Path(style_file)
        for line in style_path.read_text(encoding="utf-8").splitlines():
            if not line or line.lstrip().startswith("#"):
                continue
            key, value = line.split(":", 1)
            style_values[key.strip()] = value.strip()

        for key in checks:
            assert str(rc[key]) == style_values[key]
