#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

COPYRIGHT_YEAR = time.strftime("%Y")

AUTHOR = 'Yuta Nishino'
SITENAME = 'Yuta Nishino'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = ()

# Social widget
#SOCIAL = 

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
