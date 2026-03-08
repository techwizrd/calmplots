from __future__ import annotations

from pathlib import Path

import pytest


def test_readme_and_docs_include_user_install_commands():
    readme = Path("README.md").read_text(encoding="utf-8")
    quickstart = Path("docs/source/quickstart.rst").read_text(encoding="utf-8")

    for text in (readme, quickstart):
        assert "pip install calmplots" in text
        assert 'pip install "calmplots[all]"' in text
        assert "git+https://github.com/techwizrd/calmplots.git" in text
        assert (
            'uv add "calmplots @ git+https://github.com/techwizrd/calmplots.git"'
            in text
        )


def test_quickstart_python_calls_work_when_extras_are_installed():
    pytest.importorskip("matplotlib")
    pytest.importorskip("seaborn")
    pytest.importorskip("plotly")
    pytest.importorskip("altair")

    import calmplots

    calmplots.apply_matplotlib_theme()
    calmplots.set_seaborn_theme(context="notebook")
    assert calmplots.register_plotly_template(set_default=True) == "calmplots"
    assert calmplots.enable_altair_theme() == "calmplots"
