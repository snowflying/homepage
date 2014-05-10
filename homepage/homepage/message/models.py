# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from datetime import datetime
from django.db import models
from .managers import VisiableMessageManager


class Message(models.Model):
    """ Don't Use but retained. """
    #id = models.IntegerField(primary_key=True, editable=True)
    username = models.CharField(max_length=50, verbose_name="用户名")
    email = models.EmailField(verbose_name="邮箱")
    site = models.URLField(blank=True, verbose_name="站点")
    avatar = models.URLField(blank=True, verbose_name="头像")
    content = models.TextField(verbose_name="内容")
    post_date = models.DateTimeField(editable=False, auto_now_add=True, verbose_name="评论时间")
    is_visible = models.BooleanField(default=True, verbose_name="可见")
    ip = models.GenericIPAddressField(unpack_ipv4=True, null=True, blank=True, verbose_name="IP")
    reply_to_major_message = models.ForeignKey("self", blank=True, null=True, related_name="children")
    reply_to_minor_message = models.ForeignKey("self", blank=True, null=True)

    # Manager
    #objects = TreeManager()
    objects = models.Manager()
    vobjects = VisiableMessageManager()

    class Meta:
        verbose_name = "留言板"
        verbose_name_plural = "留言板"
        ordering = ["-post_date"]

    def __getattr__(self, name):
        if name == "reply_name":
            print('='*100, self.reply_to_minor_message.username, '='*100, sep='\n')
            return self.reply_to_minor_message.username
        super(Message, self).__getattr__(name)

    def __unicode__(self):
        return "Message(username={0}, email={1})".format(self.username, self.email)

    def save(self):
        self.username = self.username.strip()
        self.email = self.email.strip()
        self.site = self.site.strip()
        self.avatar = self.avatar.strip()
        self.ip = self.ip.strip()
        super(Message, self).save()
