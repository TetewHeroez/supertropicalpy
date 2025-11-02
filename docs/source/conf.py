"""
Configuration file for the Sphinx documentation builder.
"""
import os
import sys

# Point Sphinx to the package root (../../src/)
sys.path.insert(0, os.path.abspath('../../src'))

# -- Project information -----------------------------------------------------
project = 'Supertropical Algebra'
copyright = '2025, Supertropical Team'
author = 'Supertropical Team'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',       # Support for Google/NumPy style docstrings
    'sphinx.ext.viewcode',       # Add links to source code
    'sphinx.ext.mathjax',        # Render LaTeX math
    'sphinx.ext.intersphinx',    # Link to other project docs
    'nbsphinx',                  # Jupyter notebook support
    'myst_parser',               # Markdown support
]

# Add any paths that contain templates here
templates_path = ['_templates']

# List of patterns to exclude
exclude_patterns = []

# The master doc (main page)
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # ReadTheDocs theme
html_static_path = ['_static']

# -- Options for autodoc -----------------------------------------------------
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

# -- Options for intersphinx -------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
}

# -- Options for nbsphinx ---------------------------------------------------
nbsphinx_execute = 'never'  # Don't execute notebooks (use saved outputs)
nbsphinx_allow_errors = True  # Allow errors in notebooks during build

# Disable ipykernel requirement for static documentation
nbsphinx_requirejs_path = ''