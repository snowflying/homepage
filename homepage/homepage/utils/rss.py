# -*- coding: utf-8 -*_
from __future__ import absolute_import

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.conf import settings
from homepage.blog.models import Article


class BlogFeed(Feed):
    title = settings.HOMEPAGE_TITLE_SUFFIX
    link = settings.DOMAIN
    description = "Blog"

    def items(self):
        return Article.vobjects.order_by('-modified')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.pagebreak

    def item_link(self, item):
        return reverse('article', kwargs={"id": item.id})
