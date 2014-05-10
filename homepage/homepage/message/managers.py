# -*- coding: utf-8 -*-
from django.db import models


class VisiableMessageManager(models.Manager):
    """ Deprecation but retained. """
    def get_query_set(self):
        return super(VisiableMessageManager, self).get_query_set().filter(is_visible=True)
