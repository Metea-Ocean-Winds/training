# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ocean Winds Training repository'
copyright = '2025, Ocean Winds'
author = 'Ocean Winds'

extensions = [
    "myst_parser",  # Enables Markdown support
    "nbsphinx",      # Enables Jupyter notebook support
    "sphinx_rtd_theme"
]


templates_path = ['_templates']
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

nbsphinx_execute = 'never'
