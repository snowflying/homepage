# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    search_fields = ('name', 'site', 'description')
    list_display = ['name', 'site', 'description']
    prepopulated_fields = {'slug': ['name']}
admin.site.register(Link, LinkAdmin)
