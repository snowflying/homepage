# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import patterns, url
from .views import LinkView

urlpatterns = patterns('',
    url(r'^$', LinkView.as_view(), name="index"),
)
