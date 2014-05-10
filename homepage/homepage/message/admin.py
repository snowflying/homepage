# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    """ Deprecation but retained. """
    search_fields = ('usename', 'email', 'ip')
    list_display = ['username', 'email', 'site', 'post_date', 'is_visible', 'ip']
admin.site.register(Message, MessageAdmin)
