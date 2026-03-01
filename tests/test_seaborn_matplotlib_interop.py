import pytest

pytestmark = pytest.mark.integration


def test_seaborn_and_matplotlib_theme_interop():
    mpl = pytest.importorskip("matplotlib")
    pytest.importorskip("seaborn")
    from calmplots import apply_matplotlib_theme, set_seaborn_theme

    apply_matplotlib_theme()
    set_seaborn_theme(context="notebook")

    assert mpl.rcParams["axes.grid"] is True
    assert mpl.rcParams["grid.linewidth"] > 0


def test_seaborn_dark_theme_keeps_readable_text_defaults():
    mpl = pytest.importorskip("matplotlib")
    pytest.importorskip("seaborn")
    from calmplots import set_seaborn_theme

    set_seaborn_theme(context="notebook", theme="dark")
    assert mpl.rcParams["axes.facecolor"] == "#253040"
    assert mpl.rcParams["text.color"] == "#e8eef7"


def test_seaborn_discrete_palette_respects_dark_replacements():
    from calmplots.seaborn_theme import seaborn_discrete_palette

    colors = seaborn_discrete_palette("colorblind", theme="dark")
    assert "#000000" not in colors
