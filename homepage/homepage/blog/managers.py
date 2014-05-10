# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models


class VisiableArticleManager(models.Manager):
    def get_query_set(self):
        return super(VisiableArticleManager, self).get_query_set().filter(is_visible=True)
