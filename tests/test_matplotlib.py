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
