from calmplots.tokens import get_tokens
from calmplots.utils import contrast_sanity


def test_text_contrast_is_sane_for_light_theme():
    t = get_tokens("light")
    sanity = contrast_sanity(
        t["foreground"], t["background"], t["accent"], t["grid_major"]
    )
    assert sanity["text_ok"] is True


def test_text_contrast_is_sane_for_dark_theme():
    t = get_tokens("dark")
    sanity = contrast_sanity(
        t["foreground"], t["background"], t["accent"], t["grid_major"]
    )
    assert sanity["text_ok"] is True
