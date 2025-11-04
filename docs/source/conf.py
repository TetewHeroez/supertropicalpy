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
release = '0.1.1'

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
nbsphinx_execute = 'always'  # Execute notebooks to show live code
nbsphinx_allow_errors = False  # Don't allow errors in notebooks

# nbsphinx kernel name
nbsphinx_kernel_name = 'python3'

# Add Google Colab and GitHub links for interactive notebooks
nbsphinx_prolog = """
.. raw:: html

    <div class="interactive-banner">
        <p><strong>Run this notebook interactively:</strong></p>
        <a href="https://colab.research.google.com/github/TetewHeroez/supertropical-algebra/blob/main/docs/source/examples/tutorial.ipynb" 
           target="_blank">
           <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
        </a>
        <a href="https://github.com/TetewHeroez/supertropical-algebra/blob/main/docs/source/examples/tutorial.ipynb" 
           target="_blank" class="github-btn">
           <svg width="16" height="16" viewBox="0 0 16 16" fill="white" style="vertical-align: middle; margin-right: 5px;">
             <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
           </svg>
           View on GitHub
        </a>
    </div>
"""

# -- Options for sphinx-thebe (interactive code) -----------------------------
thebe_config = {
    "repository_url": "https://github.com/TetewHeroez/supertropical-algebra",
    "repository_branch": "main",
}
