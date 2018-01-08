#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Vincent Zaballa'
SITENAME = 'Data Science and Medical Devices'
SITESUBTITLE = 'Move It or Park It'
SITEDESCRIPTION = 'Insights and Analyses'
SITEURL = u'http://localhost:8000'
SITELOGO = SITEURL + '/images/profpic.jpeg'
FAVICON = SITEURL + '/imags/profpic_copy_kFg_icon.ico'
BROWSER_COLOR = '#333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = './Flex'
PATH = 'content'
TIMEZONE = 'America/Denver'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
LINKS = (('CV', 'https://drive.google.com/file/d/1pRjyokARMZtAsxSTWn0cuGcnJCXP5RtF/view?usp=sharing'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/vincentzaballa/'),
          ('github', 'https://github.com/vz415'),
          ('twitter', 'https://twitter.com/VZaballa?lang=en'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

DEFAULT_PAGINATION = 10

# from plugins import sitemap, post_stats, i18n_subsites
PLUGIN_PATHS = ['./plugins', ]
PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites', 'ipynb.markup', ]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

COPYRIGHT_YEAR = 2018

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

## TODO: download sitemap, post_states, and i18n_substitutes plugins
## TODO: Look into why Jinja environment is needed for flex theme

DISQUS_SITENAME = 'Data Science and Medical Devices'

STATIC_PATHS = ['images', 'figures']

CUSTOM_CSS = 'static/custom.css'

# Look up: use_less, add_this_id, and I think that's it...