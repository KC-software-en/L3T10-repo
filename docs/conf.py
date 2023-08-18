# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# ensure that Sphinx reads from the root folder of the project
# import the os, sys and django modules to set up the Django framework for the project 
import os
import sys
import django
# The sys.path.insert() function call inserts a new path at the beginning of the Python module search path. 
# insert the parent directory of the current directory into the search path. 
# This allows Python to find and import modules from the parent directory.
sys.path.insert(0, os.path.abspath('..'))
# The os.environ dictionary is used to access and modify the environment variables in Python. 
# set the DJANGO_SETTINGS_MODULE environment variable to the value 'Your_project_name.settings'. 
# This variable specifies the settings module for the Django project.
# set the settings module for the project followed by each app in the project
os.environ['DJANGO_SETTINGS_MODULE'] = 'Django_website.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'catalogue.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'polls.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'user_auth.settings'
# the django.setup() function call initializes the Django settings and sets up the necessary configurations for the project. 
# This function needs to be called before using any Django functionality
django.setup()

project = 'Cold Meats'
copyright = '2023, Kisha'
author = 'Kisha'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# configure our documentation generator
# edit extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    ]

templates_path = ['_templates']

########################
# Please do not exclude the generated documentation for this project
# because you want the audience of your repo to have easier access to your documentation.
# comment out the exclude_patterns
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
###########################


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# change the theme to sphinx_rtd_theme
# comment out previous theme
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
