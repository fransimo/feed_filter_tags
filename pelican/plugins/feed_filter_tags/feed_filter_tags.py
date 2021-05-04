from datetime import datetime
from fnmatch import fnmatch
import logging
from logging import warning
from urllib.parse import urlparse

from pelican import signals
from pelican.settings import DEFAULT_CONFIG

FEED_FILTER_TAGS_VERSION = "0.1"

log = logging.getLogger(__name__)

def register():
    """Signal registration."""
    signals.initialized.connect(initialized)
    signals.feed_generated.connect(filter_feeds)

def initialized(pelican):
    DEFAULT_CONFIG.setdefault("FEED_FILTER", {})
    if pelican:
        pelican.settings.setdefault("FEED_FILTER", {})


def format_tag(s):
    return "#" + s.lower().replace(" ", "")


def filter_feeds(context, feed):
    if len(feed.items) == 0:
        return

    new_items = []

    for f in feed.items:
        f['title'] = f['title'] + " " + " ".join([format_tag(x) for x in f['categories']])
        new_items.append(f)

    feed.items = new_items

