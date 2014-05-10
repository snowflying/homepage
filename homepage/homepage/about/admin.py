# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib import admin
from .models import About


class AboutManager(admin.ModelAdmin):
    list_display = ['order']
    search_fields = ['order', 'content']

    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/grappelli/tinymce_setup/tinymce_setup.js',)
admin.site.register(About, AboutManager)
