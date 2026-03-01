from calmplots.palettes import bluey_palette


def test_blueycolors_palettes_match_upstream_exactly():
    expected = {
        "bluey": ["#d2ebff", "#88cafc", "#404066", "#2b2c41", "#edcc6f"],
        "chilli": ["#fffad8", "#ffd08d", "#ffb070", "#9c5e33", "#46362a"],
        "heeler": ["#30598a", "#72bfed", "#e4dcbd", "#f1b873", "#e27a37"],
        "socks": ["#8f9fd8", "#201a3f", "#a97d45", "#c3cae1", "#3e2b0b"],
    }
    for name, colors in expected.items():
        assert bluey_palette(name) == colors
