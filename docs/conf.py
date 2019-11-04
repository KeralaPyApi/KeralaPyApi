import os
import sys

sys.path.insert(0, os.path.abspath("../.."))


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

version = "0.2.0"
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

html_logo = "_imgs/KeralaPyApi.jpg"
html_favicon = "_images/KeralaPyApi.ico"

latex_engine = "xelatex"
latex_logo = "_imgs/KeralaPyApi.jpg"

latex_elements = {
    "pointsize": "12pt",
    "fontpkg": r"""
        \setmainfont{Open Sans}
        \setsansfont{Bitter}
        \setmonofont{Ubuntu Mono}
        """
}
