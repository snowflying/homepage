# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class Link(models.Model):
    name = models.CharField(max_length=50, verbose_name="网站名")
    slug = models.SlugField(max_length=100, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="网站描述")
    picture = models.URLField(blank=True, null=True, verbose_name="图片")
    site = models.URLField(verbose_name="网站地址")

    class Meta:
        verbose_name = "网站收藏"
        verbose_name_plural = "网站收藏"

    def __unicode__(self):
        return self.name

    def save(self):
        self.name = self.name.strip()
        self.site = self.site.strip()
        self.slug = self.slug.strip()
        self.picture = self.picture.strip()
        self.description = self.description.strip()[:200]
        if not self.description:
            self.description = self.name
        if not self.picture:
            self.picture = settings.STATIC_URL+"website/images/default.jpg"
        super(Link, self).save()
