# -*- coding: utf-8 -*-
"""
"""
import logging
import os

from .version import __version__

from cookielib import CookieJar as cj

log = logging.getLogger(__name__)

PARENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

POPULAR_URLS = os.path.join(PARENT_DIRECTORY, 'data/popular_sources.txt')
USERAGENTS = os.path.join(PARENT_DIRECTORY, 'data/useragents.txt')
STOPWORDS_EN = os.path.join(PARENT_DIRECTORY, 'data/stopwords_en.txt')
STOPWORDS_EN_FN_2 = os.path.join(PARENT_DIRECTORY, 'data/stopwords_en2.txt')

DATA_DIRECTORY = '.newspaper_scraper'

TOP_DIRECTORY = os.path.join(os.path.expanduser("~"), DATA_DIRECTORY)
if not os.path.exists(TOP_DIRECTORY):
    os.mkdir(TOP_DIRECTORY)

# Error log
LOGFILE = os.path.join(TOP_DIRECTORY, 'newspaper_errors_%s.log' % __version__)
MONITOR_LOGFILE =  os.path.join(TOP_DIRECTORY, 'newspaper_monitors_%s.log' % __version__)

# Memo directory (same for all concur crawlers)
MEMO_FILE = 'memoized'
MEMO_DIR = os.path.join(TOP_DIRECTORY, MEMO_FILE)

if not os.path.exists(MEMO_DIR):
    os.mkdir(MEMO_DIR)

# category and feed cache
CF_CACHE_DIRECTORY = 'feed_category_cache'
ANCHOR_DIRECTORY = os.path.join(TOP_DIRECTORY, CF_CACHE_DIRECTORY)

if not os.path.exists(ANCHOR_DIRECTORY):
    os.mkdir(ANCHOR_DIRECTORY)

TRENDING_URL = 'http://www.google.com/trends/hottrends/atom/feed?pn=p1'

