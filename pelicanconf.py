#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Weezer Su'
SITENAME = u"Weezer's BXJ"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud", "render_math"]

#tag-cloud setting
TAG_CLOUD_STEPS = 2
TAG_CLOUD_MAX_ITEMS = 10
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = False

TAGS_URL = 'tags.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/weezersu'),
          ('github', 'https://github.com/weezer'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "themes/pelican-bootstrap3"
FAVICON = 'images/favicon.ico'
DISPLAY_CATEGORIES_ON_MENU = True
SHOW_ARTICLE_CATEGORY = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_TAGS_INLINE = False
DISPLAY_TAGS_ON_SIDEBAR = True
BOOTSTRAP_NAVBAR_INVERSE = True
BOOTSTRAP_THEME = "darkly"
MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight, linenums=True)', 'extra']
# tell pelican where your custom.css file is in your content folder
STATIC_PATHS = ['images',
		'images/favicon.ico',
		'pdfs']
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}
}
