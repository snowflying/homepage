# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models


class About(models.Model):
    order = models.SmallIntegerField(verbose_name="顺序")
    content = models.TextField(verbose_name="内容")

    class Meta:
        verbose_name = "关于"
        verbose_name_plural = "关于"
        ordering = ['order']

    def __unicode__(self):
        return "{0}".format(self.order)

    def save(self):
        if self.order < 1:
            self.order = 1
        return super(About, self).save()
