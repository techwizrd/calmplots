import pytest


pytestmark = pytest.mark.integration


def test_plotnine_theme_and_scales_create_objects():
    pytest.importorskip("plotnine")
    from calmplots import scale_color_calm, scale_fill_calm_c, theme_calm

    th = theme_calm()
    sc = scale_color_calm()
    fc = scale_fill_calm_c()

    assert th is not None
    assert sc is not None
    assert fc is not None
