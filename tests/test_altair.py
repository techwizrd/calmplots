import pytest


pytestmark = pytest.mark.integration


def test_altair_theme_enable():
    pytest.importorskip("altair")
    from calmplots import enable_altair_theme

    name = enable_altair_theme(name="calmplots_test")
    assert name == "calmplots_test"
