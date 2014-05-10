# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import

from datetime import datetime
#from django.http import Http404, HttpResponse
#from django.shortcuts import render_to_response, render, redirect, \
#    get_object_or_404, get_list_or_404
from django.conf import settings
from django.views import generic
from django.http import Http404
from django.core import validators
from ..utils.pagination import get_pagination
from .models import Article, ArticleTag, Category, Tag

validator_url = validators.URLValidator()


class BlogTemlateView(generic.TemplateView):
    def _get_categories(self):
        return {'categories': Category.objects.all()}

    def _classify_by_date(self):
        r = {}
        articles = Article.vobjects.all()
        for obj in articles:
            year = obj.created.year
            month = obj.created.month
            r.setdefault(year, [])
            if month not in r[year]:
                r[year].append(month)
        return {'dates': r}

    def _get_tags(self):
        return {'tags': Tag.objects.all()}

    def _get_lastest_articles(self):
        return {"lastest_articles": Article.vobjects.order_by('-created')[:10]}

    def _get_click_articles(self):
        return {"click_articles": Article.vobjects.order_by('-clicks')[:10]}

    def get_paginator(self, queryset):
        return get_pagination(queryset, self.request.REQUEST.get("page"))

    def get_context_data(self, *args, **kwargs):
        kwargs.update(self._get_categories())
        kwargs.update(self._get_tags())
        kwargs.update(self._classify_by_date())
        kwargs.update(self._get_lastest_articles())
        kwargs.update(self._get_click_articles())
        return super(BlogTemlateView, self).get_context_data(**kwargs)


class IndexView(BlogTemlateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        queryset = Article.vobjects.all()
        kwargs.update(self.get_paginator(queryset))
        return super(IndexView, self).get_context_data(**kwargs)


class CategoryView(BlogTemlateView):
    template_name = "blog/category.html"

    def get_context_data(self, **kwargs):
        queryset = Article.vobjects.filter(category_id=self.kwargs['pk'])
        kwargs.update(self.get_paginator(queryset))
        return super(CategoryView, self).get_context_data(**kwargs)


class YearView(BlogTemlateView):
    template_name = 'blog/year.html'

    def get_context_data(self, **kwargs):
        year = int(self.kwargs['year'].strip())
        start = datetime(year, 1, 1)
        end = datetime(year + 1, 1, 1)
        queryset = Article.vobjects.filter(created__gte=start).filter(created__lt=end)
        kwargs.update(self.get_paginator(queryset))
        return super(YearView, self).get_context_data(**kwargs)


class MonthView(BlogTemlateView):
    template_name = 'blog/month.html'

    def get_context_data(self, **kwargs):
        year = int(self.kwargs['year'].strip())
        month = int(self.kwargs['month'].strip())
        start = datetime(year, month, 1)
        if month < 1 or month > 12:
            raise Http404()
        elif month == 12:
            end = datetime(year + 1, 1, 1)
        else:
            end = datetime(year, month + 1, 1)
        queryset = Article.vobjects.filter(created__gte=start).filter(created__lt=end)
        kwargs.update(self.get_paginator(queryset))
        return super(YearView, self).get_context_data(**kwargs)


class TagView(BlogTemlateView):
    template_name = 'blog/tag.html'

    def get_context_data(self, **kwargs):
        article_tag_list = ArticleTag.objects.filter(tag_id=self.kwargs['tag_id'])
        queryset = []
        for i in article_tag_list:
            queryset.append(i.article_id)
        kwargs.update(self.get_paginator(queryset))
        return super(TagView, self).get_context_data(**kwargs)


class ArticleView(BlogTemlateView):
    template_name = 'blog/article.html'

    def get_context_data(self, **kwargs):
        try:
            article = Article.vobjects.filter(id=self.kwargs['id'])[0]
        except:
            raise Http404()
        article.click_once()
        kwargs['object'] = article
        kwargs['duoshuo'] = settings.DUOSHUO_SHORT_NAME
        return super(ArticleView, self).get_context_data(**kwargs)
