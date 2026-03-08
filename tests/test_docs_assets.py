from __future__ import annotations

from pathlib import Path


def test_readme_gallery_assets_exist():
    required = [
        "examples/gallery/palettes_light.png",
        "examples/gallery/palettes_dark.png",
        "examples/gallery/before_default_scatter.png",
        "examples/gallery/before_calmplots_scatter.png",
        "examples/gallery/gallery_matplotlib.png",
        "examples/gallery/plotnine_scatter.png",
        "examples/gallery/plotly_scatter.png",
        "examples/gallery/altair_scatter.png",
        "examples/gallery/matrix/README.md",
    ]
    for rel in required:
        assert Path(rel).exists(), f"Missing README-linked asset: {rel}"


def test_matrix_readme_links_follow_expected_layout():
    matrix_root = Path("examples/gallery/matrix")
    text = (matrix_root / "README.md").read_text(encoding="utf-8")
    links = []
    for part in text.split("["):
        if "](" not in part:
            continue
        tail = part.split("](", 1)[1]
        link = tail.split(")", 1)[0]
        if link.endswith(".png") or link.endswith(".svg"):
            links.append(link)

    assert links, "No gallery links found in matrix README"
    assert len(links) == 80

    valid_themes = {"light", "dark"}
    valid_palettes = {"bluey", "chilli", "heeler", "socks", "colorblind"}
    valid_backends = {"matplotlib_seaborn", "plotnine", "plotly", "altair"}
    for link in links:
        path = Path(link)
        assert len(path.parts) == 4, f"Unexpected matrix link shape: {link}"
        theme, palette, backend, filename = path.parts
        assert theme in valid_themes, f"Unexpected theme segment: {link}"
        assert palette in valid_palettes, f"Unexpected palette segment: {link}"
        assert backend in valid_backends, f"Unexpected backend segment: {link}"
        assert filename in {
            "scatter.png",
            "scatter.svg",
        }, f"Unexpected filename: {link}"
