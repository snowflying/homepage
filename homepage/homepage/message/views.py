# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division
import socket
from django.views import generic as view
from django.shortcuts import redirect
from django.core import validators
from django.conf import settings
from .. import utils
from .models import Message

validator_url = validators.URLValidator()


class IndexView(view.TemplateView):
    template_name = 'message/message.html'

    def get_context_data(self, **kwargs):
        kwargs['duoshuo'] = settings.DUOSHUO_SHORT_NAME
        return super(IndexView, self).get_context_data(**kwargs)

    def _get_context_data(self, **kwargs):
        """ Deprecation but retained. """
        queryset = Message.vobjects.filter(reply_to_major_message=None)
        page = self.request.GET.get('page')
        tmp = utils.get_pagination(queryset, page, settings.HOMEPAGE_MESSAGE_NUM_PER_PAGE)
        for i in tmp["object_list"]:
            i.reply = Message.vobjects.filter(reply_to_major_message=i).order_by('post_date')
        kwargs.update(tmp)
        return super(IndexView, self).get_context_data(**kwargs)

    def _post(self, *args, **kwargs):
        """ Deprecation but retained. """
        major_message_id = self.request.POST.get('major_id', '').strip()
        minor_message_id = self.request.POST.get('minor_id', '').strip()
        if major_message_id:
            try:
                major_message = Message.vobjects.filter(id=major_message_id)[0]
            except:
                major_message = None
            if not major_message:
                return redirect(self.request.path)
        else:
            major_message = None

        if minor_message_id:
            try:
                minor_message = Message.vobjects.filter(id=minor_message_id)[0]
            except:
                minor_message = None
            if not minor_message:
                return redirect(self.request.path)
        else:
            minor_message = None

        data = self.request.POST
        username = data['username']
        email = data['email']
        site = data['site']
        #avatar = ''
        content = data['content']
        #post_date = datetime.now()
        is_visible = True
        ip = self.request.META.get('REMOTE_ADDR')
        if not ip:
            try:
                hostname = self.request.META.get("REMOTE_HOST")
                # gethostbyname doesn't support IPv6.
                ip = socket.gethostbyname(hostname)
            except:
                ip = None

        if not username or len(username) > 50 or not content:
            return redirect(self.request.path)

        try:
            validators.validate_email(email)
        except:
            return redirect(self.request.path)

        if site:
            try:
                validator_url(site)
            except:
                return redirect(self.request.path)

        c = Message(username=username, email=email, site=site, content=content,
                    is_visible=is_visible, ip=ip, reply_to_major_message=major_message,
                    reply_to_minor_message=minor_message)
        c.save()

        return redirect(self.request.path)
