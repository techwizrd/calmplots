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
