import pytest


pytestmark = pytest.mark.integration


def test_plotly_template_registration():
    pytest.importorskip("plotly")
    from calmplots import register_plotly_template

    name = register_plotly_template(name="calmplots_test", set_default=False)
    assert name == "calmplots_test"
