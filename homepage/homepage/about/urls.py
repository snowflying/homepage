# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import patterns, url
from .views import AboutView

urlpatterns = patterns('',
    url(r'^$', AboutView.as_view(), name="index"),
)
