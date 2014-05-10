# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.contrib import admin
#from django import forms
from .models import *
#from django.contrib.contenttypes import generic
from .models import Category, Tag, Article, ArticleTag, BlogUser


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {"slug": ('name',)}
admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ('name', 'articles')
    prepopulated_fields = {"slug": ('name',)}
admin.site.register(Tag, TagAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author_id', 'category_id', 'clicks',
                    'created', 'modified', 'is_shared', 'is_always_above',
                    'is_visible']
    search_fields = ('title', 'content')
    date_hierarchy = 'created'
    prepopulated_fields = {"slug": ('title',)}
    # readonly_fields = ['created']
    inlines = [ArticleTagInline]
    ordering = ['-created']
    fieldsets = [
        ('文章编辑', {'fields': ('title', 'slug', 'content')}),
        ('日期', {'fields': ('created', 'modified')}),
        ('信息', {'fields': ('category_id', 'author_id', 'is_always_above', 'is_shared', 'is_visible')})
    ]

    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/static/grappelli/tinymce_setup/tinymce_setup.js',)
admin.site.register(Article, ArticleAdmin)


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['article_id', 'tag_id']
admin.site.register(ArticleTag, ArticleTagAdmin)


class BlogUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'description']
admin.site.register(BlogUser, BlogUserAdmin)


class BlackListAdmin(admin.ModelAdmin):
    search_fields = ('ip',)
    list_display = ['ip']
admin.site.register(BlackList, BlackListAdmin)
