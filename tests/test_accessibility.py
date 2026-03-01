from calmplots import (
    accessible_palette,
    min_pairwise_oklab_distance,
    palette_accessibility_report,
    simulate_cvd_hex,
)


def test_accessible_palette_shape():
    assert len(accessible_palette("light")) == 8
    assert len(accessible_palette("dark")) == 8


def test_cvd_simulation_returns_hex():
    out = simulate_cvd_hex("#0072B2", "protan", 0.6)
    assert out.startswith("#")
    assert len(out) == 7


def test_accessible_palette_separation_under_cvd_modes():
    d_light = min_pairwise_oklab_distance(accessible_palette("light"), include_cvd=True)
    d_dark = min_pairwise_oklab_distance(accessible_palette("dark"), include_cvd=True)
    assert d_light >= 0.09
    assert d_dark >= 0.09


def test_accessibility_report_has_passing_thresholds():
    light_report = palette_accessibility_report(
        accessible_palette("light"), background="#f7f9fc"
    )
    dark_report = palette_accessibility_report(
        accessible_palette("dark"), background="#1f2631"
    )
    assert light_report["distance_ok"] is True
    assert dark_report["distance_ok"] is True
    assert light_report["contrast_ok"] is True
    assert dark_report["contrast_ok"] is True
