from __future__ import annotations

import sys
from importlib.metadata import version as pkg_version
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

project = "calmplots"
author = "Kunal K. Sarkhel"
release = pkg_version("calmplots")
version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "bysource"

templates_path = ["_templates"]
exclude_patterns = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

html_theme = "furo"
html_static_path = ["_static"]
