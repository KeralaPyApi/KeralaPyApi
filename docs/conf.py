import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

from keralabot import __version__

from pygments.styles.friendly import FriendlyStyle

FriendlyStyle.background_color = "#f3f2f1"

project = "KeralaPyApi"
copyright = "2019-2021, Mario"
author = "Mario"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary"
]

master_doc = "index"
source_suffix = ".rst"
autodoc_member_order = "bysource"

version = __version__
release = version

templates_path = ["_templates"]

napoleon_use_rtype = False

pygments_style = "friendly"

html_title = "KeralaPyApi Documentation"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_show_sourcelink = True
html_show_copyright = False
html_theme_options = {
    "canonical_url": "https://keralapyapi.readthedocs.io/",
    "collapse_navigation": True,
    "sticky_navigation": False,
    "logo_only": True,
    "display_version": True,
    "style_external_links": True
}

html_logo = "_images/pyrogram.png"
html_favicon = "_images/favicon.ico"

latex_engine = "xelatex"
latex_logo = "_images/pyrogram.png"

latex_elements = {
    "pointsize": "12pt",
    "fontpkg": r"""
        \setmainfont{Open Sans}
        \setsansfont{Bitter}
        \setmonofont{Ubuntu Mono}
        """
}
