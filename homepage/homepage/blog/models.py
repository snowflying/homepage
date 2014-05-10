# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime
from django.db import models
from django.contrib.auth.admin import User
from django.core.urlresolvers import reverse
#from django.contrib.contenttypes import generic
#from django.contrib.contenttypes.models import ContentType
from ..utils.pagebreak import get_pagebreak
from .managers import VisiableArticleManager


class Category(models.Model):
    name = models.CharField(verbose_name="分类名", max_length=50, unique=True)
    slug = models.SlugField(blank=True)
    order = models.IntegerField(verbose_name="顺序", blank=True, null=True)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"
        ordering = ['order', 'name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        print('-'*30, reverse('category', kwargs={'id': self.id}))
        return reverse('category', kwargs={'id': self.id})

    def url(self):
        return self.get_absolute_url()

    def save(self):
        self.name = self.name.strip()
        if not self.slug:
            self.slug = self.name
        if not self.order:
            cates = Category.objects.all()
            if cates:
                max_order = cates.order_by('-order')[0].order
                self.order = max_order + 1
            else:
                self.order = 1
        super(Category, self).save()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="标签")
    slug = models.SlugField(blank=True)
    articles = models.ManyToManyField("Article", through="ArticleTag", verbose_name="文章")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"
        ordering = ['?']

    def __unicode__(self):
        return self.name

    def save(self):
        self.name = self.name.strip()
        if not self.slug:
            self.slug = self.name
        super(Tag, self).save()

    def get_absolute_url(self):
        return reverse('tag', kwargs={'id': self.id})

    def url(self):
        return self.get_absolute_url()


class Article(models.Model):
    # Field
    title = models.CharField(max_length=100, verbose_name="标题")
    slug = models.SlugField(max_length=100, blank=True)
    content = models.TextField(verbose_name="内容")
    # created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    created = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    modified = models.DateTimeField(default=datetime.now, verbose_name="修改时间")
    is_always_above = models.BooleanField(default=False, verbose_name="置顶")
    is_shared = models.BooleanField(default=False, verbose_name="分享到社交网络")
    is_visible = models.BooleanField(default=True, verbose_name="可见")
    clicks = models.IntegerField(default=0, editable=False, verbose_name="点击次数")
    category_id = models.ForeignKey(Category, verbose_name="分类", db_column="category_id")
    author_id = models.ForeignKey("BlogUser", verbose_name="作者", db_column='author_id')
    tags = models.ManyToManyField("Tag", through="ArticleTag", blank=True, verbose_name="标签")

    # Manager
    objects = models.Manager()
    vobjects = VisiableArticleManager()

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"
        ordering = ['-is_always_above', '-created']

    def __unicode__(self):
        return self.title

    def __getattr__(self, name):
        if name == "pagebreak":
            return get_pagebreak(self.content)
        else:
            return super(Article, self).__getattr__(name)

    def save(self):
        self.title = self.title.strip()
        if not self.slug:
            self.slug = self.title
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('article', kwargs={'id': self.id})

    def url(self):
        return self.get_absolute_url()

    def click_once(self):
        self.clicks += 1
        super(Article, self).save()


class ArticleTag(models.Model):
    article_id = models.ForeignKey(Article, db_column='article_id')
    tag_id = models.ForeignKey(Tag, db_column='tag_id')

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = "文章标签"

    def __unicode__(self):
        return "{0}: {1}".format(self.tag_id, self.article_id)


class BlogUser(models.Model):
    #small_avatar = models.FileField()
    description = models.TextField(verbose_name="描述")
    user = models.OneToOneField(User, db_column='user_id')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __unicode__(self):
        return self.user.username


class BlackList(models.Model):
    ip = models.GenericIPAddressField(unpack_ipv4=True, verbose_name="IP")

    class Meta:
        verbose_name = "黑名单"
        verbose_name_plural = "黑名单"

    def __unicode__(self):
        return self.ip

    def save(self):
        self.ip = self.ip.strip()
        super(BlackList, self).save()
