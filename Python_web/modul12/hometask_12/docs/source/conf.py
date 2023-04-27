import sys
import os
# sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../..'))
# sys.path.append(os.path.abspath('../static'))
# sys.path.append(os.path.abspath('../../static'))
# sys.path.insert(0, os.path.abspath('..'))
# sys.path.append(os.path.abspath('/Users/olha/Documents/GitHub/goit_course/Python_web/modul12/hometask_12'))
# sys.path.insert(0, os.path.abspath('../..'))
project = 'Contacts Rest Api'
copyright = '2023, oishchenko'
author = 'oishchenko'


extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'nature'
html_static_path = ['_static']
