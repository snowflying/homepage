# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import patterns, url
from .views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name="index"),
)