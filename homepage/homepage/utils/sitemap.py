# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
from django.contrib.sitemaps import Sitemap
from homepage.blog.models import Article


class BlogSitemap(Sitemap):
    changfreq = 'weekly'
    priority = 0.5

    def items(self):
        return Article.vobjects.all()

    def lastmod(self, obj):
        return obj.modified

sitemaps = {'blog': BlogSitemap}
