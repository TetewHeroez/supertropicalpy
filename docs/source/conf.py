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
nbsphinx_execute = 'never'  # Don't execute notebooks during build (run manually)
nbsphinx_allow_errors = True  # Allow errors to not break the build

# nbsphinx kernel name
nbsphinx_kernel_name = 'python3'

# Google Colab badge for notebooks
nbsphinx_prolog = r"""
.. raw:: html

    <div style="text-align: center; margin-bottom: 20px; padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 8px;">
        <a href="https://colab.research.google.com/github/TetewHeroez/supertropical-algebra/blob/main/{{ env.doc2path(env.docname, base=None) }}" 
           target="_blank" 
           style="display: inline-flex; align-items: center; gap: 8px; padding: 10px 20px; background-color: white; color: #333; text-decoration: none; border-radius: 6px; font-weight: 500; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" style="fill: #F9AB00;">
                <path d="M12 0C5.37 0 0 5.37 0 12s5.37 12 12 12 12-5.37 12-12S18.63 0 12 0zm0 22C6.48 22 2 17.52 2 12S6.48 2 12 2s10 4.48 10 10-4.48 10-10 10z"/>
                <path d="M12 6c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm0 10c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4z"/>
                <circle cx="12" cy="12" r="2"/>
            </svg>
            <span>Open in Google Colab</span>
        </a>
    </div>
"""

# -- Options for sphinx-thebe (interactive code) -----------------------------
thebe_config = {
    "repository_url": "https://github.com/TetewHeroez/supertropical-algebra",
    "repository_branch": "main",
}
