import pytest

pytestmark = pytest.mark.integration


def test_plotly_template_registration():
    pytest.importorskip("plotly")
    from calmplots import register_plotly_template
    from calmplots.plotly_theme import build_plotly_template

    name = register_plotly_template(name="calmplots_test", set_default=False)
    assert name == "calmplots_test"

    template = build_plotly_template(theme="dark")
    assert template.layout.legend.font.color == "#e8eef7"
    assert template.layout.legend.title.font.color == "#e8eef7"
    assert template.layout.legend.bgcolor == "#253040"
    assert template.layout.hoverlabel.font.color == "#e8eef7"
    assert template.layout.xaxis.tickfont.color == "#b5c2d4"
    assert template.layout.yaxis.tickfont.color == "#b5c2d4"
    assert template.layout.coloraxis.colorbar.tickfont.color == "#b5c2d4"
    assert template.layout.polar.angularaxis.tickfont.color == "#b5c2d4"
    assert template.layout.ternary.aaxis.tickfont.color == "#b5c2d4"
    assert template.layout.scene.xaxis.tickfont.color == "#b5c2d4"
