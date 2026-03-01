import calmplots


def test_public_api_matches_supported_surface():
    expected = {
        "apply_matplotlib_theme",
        "apply_notebook_theme",
        "accessible_palette",
        "bluey_palette",
        "colorblind_palette",
        "continuous_palette",
        "enable_altair_theme",
        "get_tokens",
        "list_palettes",
        "min_pairwise_oklab_distance",
        "palette_accessibility_report",
        "register_altair_theme",
        "register_plotly_template",
        "scale_color_calm",
        "scale_color_calm_c",
        "scale_fill_calm",
        "scale_fill_calm_c",
        "set_seaborn_theme",
        "simulate_cvd_hex",
        "theme_calm",
        "use_matplotlib_stylesheet",
    }
    assert set(calmplots.__all__) == expected
