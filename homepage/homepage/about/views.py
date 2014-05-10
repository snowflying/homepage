# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.views import generic as view
from .models import About


class AboutView(view.TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        objs = About.objects.all().order_by('-id')
        if objs:
            kwargs['object'] = objs[0]
        else:
            kwargs['object'] = None
        return super(AboutView, self).get_context_data(**kwargs)
