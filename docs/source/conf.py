# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'oscillo'
copyright = '2022, oscillo'
author = 'oscillo'

release = '0.1'
version = '0.1.0'

master_doc = 'index'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'oscillo': ('https://osc.finance', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'