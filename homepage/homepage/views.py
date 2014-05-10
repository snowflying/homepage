# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import

# from django.http import Http404, HttpResponse
# from django.shortcuts import render_to_response, render, redirect,\
#     get_object_or_404, get_list_or_404
from django.conf import settings
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from homepage.blog.models import Article


def index(request):
    #return render(request, "base.html")
    return redirect('/blog')


def search(request):
    c = {}
    try:
        key = ''
        key = request.POST['q'].strip()
    except:
        pass

    keys = key.split()
    if not keys:
        return render(request, 'search.html', {"object_list": c})

    c['article'] = []
    for k in keys:
        c['article'] += Article.vobjects.filter(content__contains=k)

    return render(request, 'search.html', {"object_list": c})


#def my_login(request):
class LoginView(generic.TemplateView):
    template_name = "login.html"

    def post(self, *args, **kwargs):
        username = self.request.POST.get("username", '')
        password = self.request.POST.get("password", '')
        next = self.request.REQUEST.get("next", '/')
        if not next:
            next = "/"
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(self.request, user)
                return redirect(next)
            else:
                return redirect(settings.LOGIN_URL)
        else:
            return redirect(settings.LOGIN_URL)


def my_logout(request):
    logout(request)
    next = request.REQUEST.get("next", '/')
    if not next:
        next = "/"
    return redirect(next)
