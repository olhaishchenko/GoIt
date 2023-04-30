import sys
import os

sys.path.append(os.path.abspath('../..'))

project = 'Contacts Rest Api'
copyright = '2023, oishchenko'
author = 'oishchenko'


extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'nature'
html_static_path = ['_static']
