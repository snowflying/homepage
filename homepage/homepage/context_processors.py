# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import
from datetime import datetime
from django.conf import settings
#from django.http import HttpResponseServerError


def title_suffix(request):
    return {'title_suffix': settings.HOMEPAGE_TITLE_SUFFIX}


def home_page(request):
    return {'home_page': settings.DOMAIN.strip('/')}


def current_year(request):
    return {'year': datetime.today().year}


def current_page(request):
    page = request.path.split('/', 2)[1]
    if page == '':
        rtn = [page, "首页"]
    elif page == "blog":
        rtn = [page, "博客"]
    elif page == "message":
        rtn = [page, "留言板"]
    elif page == "about":
        rtn = [page, "关于我"]
    elif page == "search":
        rtn = [page, "搜索结果"]
    elif page == "website":
        rtn = [page, "网站收藏"]
    else:
        rtn = page

    return {'current_page': rtn}


def current_path(request):
    return {"current_path": request.path}
