#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_reveals documentation build configuration file, created by
# sphinx-quickstart on Sun May 21 12:00:01 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinxjp.themes.revealjs'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'test_reveals'
copyright = '2017, Patrick'
author = 'Patrick'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1'
# The full version, including alpha/beta/rc tags.
release = '1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set 'language' from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'revealjs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # Set the lang attribute of the html tag. Defaults to 'ja'
    'lang': 'en',

    # The 'normal' size of the presentation, aspect ratio will be preserved
    # when the presentation is scaled to fit different resolutions
    'width': 960,
    'height': 700,

    # Factor of the display size that should remain empty around the content
    'margin': 0.1,

    # Bounds for smallest/largest possible scale to apply to content
    'min_scale': 0.2,
    'max_scale': 1.0,

    # Display controls in the bottom right corner
    'controls': True,

    # Display a presentation progress bar
    'progress': True,

    # Set default timing of 2 minutes per slide
    'default_timing': 120,

    # Display the page number of the current slide
    'slide_number': False,

    # Push each slide change to the browser history
    'history': True,

    # Enable keyboard shortcuts for navigation
    'keyboard': True,

    # Enable the slide overview mode
    'overview': True,

    # Vertical centering of slides
    'center': True,

    # Enables touch navigation on devices with touch input
    'touch': True,

    # Loop the presentation
    'loop': False,

    # Change the presentation direction to be RTL
    'rtl': False,

    # Randomizes the order of slides each time the presentation loads
    'shuffle': False,

    # Turns fragments on and off globally
    'fragments': True,

    # Flags if the presentation is running in an embedded mode,
    # i.e. contained within a limited portion of the screen
    'embedded': False,

    # Flags if we should show a help overlay when the questionmark
    # key is pressed
    'help': True,

    # Flags if speaker notes should be visible to all viewers
    'show_notes': False,

    # Global override for autolaying embedded media (video/audio/iframe)
    # - : Media will only autoplay if data-autoplay is present
    # - True: All media will autoplay, regardless of individual setting
    # - False: No media will autoplay, regardless of individual setting
    #'autoPlayMedia': '',

    # Number of milliseconds between automatically proceeding to the
    # next slide, disabled when set to 0, this value can be overwritten
    # by using a data-autoslide attribute on your slides
    'auto_slide': 0,

    # Stop auto-sliding after user input
    'auto_slide_stoppable': True,

    # Use this method for navigation when auto-sliding
    'auto_slide_method': 'Reveal.navigateNext',

    # Enable slide navigation via mouse wheel
    'mouse_wheel': False,

    # Hides the address bar on mobile devices
    'hide_address_bar': True,

    # Opens links in an iframe preview overlay
    'preview_links': False,

    # Transition style (default(=convex)/none/fade/slide/concave/zoom)
    'transition': 'default',

    # Transition speed (default/fast/slow)
    'transition_speed': 'default',

    # Transition style for full page slide backgrounds (default(=convex)/none/fade/slide/concave/zoom)
    'background_transition': 'default',

    # Theme (black/white/league/beige/sky/night/serif/simple/solarized)
    'theme': 'night',

    # Parallax background image
    # CSS syntax, e.g. 'a.jpg'
    #'parallax_background_image': '_static/bg.jpg',

    # Parallax background size
    # CSS syntax, e.g. '3000px 2000px'
    #'parallax_background_size': '2000px 900px',

    # Number of pixels to move the parallax background per slide
    # - Calculated automatically unless specified
    # - Set to 0 to disable movement along an axis
    #'parallax_background_horizontal': None,
    #'parallax_background_vertical': None,

    # The display mode that will be used to show slides
    'display': 'block'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']


html_use_index = False

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'test_revealsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'test_reveals.tex', 'test\\_reveals Documentation',
     'Patrick', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'test_reveals', 'test_reveals Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'test_reveals', 'test_reveals Documentation',
     author, 'test_reveals', 'One line description of project.',
     'Miscellaneous'),
]


def setup(app):
    app.add_javascript("js/jquery.min.js")
    app.add_javascript("js/orange-reveal.js")
    app.add_stylesheet('css/colors.css')
    app.add_stylesheet('css/orange-reveal-override.css')


# http://www.sphinx-doc.org/en/stable/config.html#confval-rst_prolog
rst_prolog = '''
.. include:: /_ext/special.rst
'''

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
