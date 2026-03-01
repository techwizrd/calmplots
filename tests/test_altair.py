import pytest

pytestmark = pytest.mark.integration


def test_altair_theme_enable():
    pytest.importorskip("altair")
    import altair as alt

    from calmplots import enable_altair_theme

    name = enable_altair_theme(name="calmplots_test")
    assert name == "calmplots_test"

    enable_altair_theme(name="calmplots_test_dark", theme="dark")
    cfg = alt.theme.get()()
    assert cfg["config"]["legend"]["labelColor"] == "#b5c2d4"
    assert cfg["config"]["header"]["labelColor"] == "#b5c2d4"
    assert cfg["config"]["text"]["color"] == "#e8eef7"
