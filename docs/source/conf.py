
import os, sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------

from mysnap import __version__

project = 'mysnap'
copyright = '2021, Nuno Ramos Carvalho'
author = 'Nuno Ramos Carvalho'
release = __version__

# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

