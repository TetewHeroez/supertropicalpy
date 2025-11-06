"""
Configuration file for the Sphinx documentation builder.
"""
import os
import sys

# Point Sphinx to the package root (../../src/)
sys.path.insert(0, os.path.abspath('../../src'))

# -- Project information -----------------------------------------------------
project = 'SupertropicalPy'
copyright = '2025, Supertropical Team'
author = 'Supertropical Team'
release = '0.1.2'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',       # Support for Google/NumPy style docstrings
    'sphinx.ext.viewcode',       # Add links to source code
    'sphinx.ext.mathjax',        # Render LaTeX math
    'sphinx.ext.intersphinx',    # Link to other project docs
    'nbsphinx',                  # Jupyter notebook support
    'myst_parser',               # Markdown support
    'sphinx_thebe',              # Interactive code execution
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

# Add custom CSS for better styling
html_css_files = [
    'custom.css',
]

# -- Options for autodoc -----------------------------------------------------
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

# -- Options for intersphinx -------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
}

# -- Options for nbsphinx ---------------------------------------------------
nbsphinx_execute = 'auto'  # Execute notebooks during build to show outputs
nbsphinx_allow_errors = True  # Allow errors to not break the build

# nbsphinx kernel name
nbsphinx_kernel_name = 'python3'

# Google Colab badge for notebooks
nbsphinx_prolog = r"""
.. raw:: html

    <div style="text-align: center; margin: 10px 0;">
        <a href="https://colab.research.google.com/github/TetewHeroez/supertropicalpy/blob/main/docs/source/{{ env.doc2path(env.docname, base=None) }}" 
           target="_blank" 
           style="display: inline-flex; align-items: center; gap: 8px; padding: 8px 16px; background-color: #f5f5f5; color: #333; text-decoration: none; border: 1px solid #ddd; border-radius: 4px; font-size: 14px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Google_Colab_pic.png/250px-Google_Colab_pic.png" 
                 alt="Colab" 
                 style="height: 20px;">
            Open in Google Colab
        </a>
    </div>
"""

# -- Options for sphinx-thebe (interactive code) -----------------------------
thebe_config = {
    "repository_url": "https://github.com/TetewHeroez/supertropicalpy",
    "repository_branch": "main",
}
