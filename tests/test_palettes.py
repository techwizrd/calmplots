from calmplots.palettes import bluey_palette, colorblind_palette, continuous_palette

import pytest


pytestmark = pytest.mark.unit


def test_bluey10_has_ten_colors():
    colors = bluey_palette("bluey10")
    assert len(colors) == 10


def test_palette_truncates_to_n():
    colors = bluey_palette("heeler", n=3)
    assert len(colors) == 3


def test_colorblind_palette_size():
    colors = colorblind_palette()
    assert len(colors) >= 8


def test_continuous_palette_available():
    colors = continuous_palette("bluey_seq")
    assert len(colors) >= 5
