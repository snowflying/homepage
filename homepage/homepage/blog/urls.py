# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import patterns, url
from .views import IndexView, CategoryView, TagView, YearView, MonthView, ArticleView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^articles/(?P<id>[1-9][0-9]*)', ArticleView.as_view(), name='article'),
    url(r'^category/(?P<pk>\w)', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>[1-9][0-9]*)', TagView.as_view(), name='tag'),
    url(r'^date/(?P<year>[1-9][0-9]{3})', YearView.as_view(), name='year'),
    url(r'^date/(?P<year>[1-9][0-9]{3})/(?P<month>[0-1][1-9])$', MonthView.as_view(), name="month"),
)
