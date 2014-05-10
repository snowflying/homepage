# -*- coding: utf-8 -*-
from __future__ import absolute_import, division

from django.views import generic as view
from .models import Link


class LinkView(view.TemplateView):
    template_name = "website/index.html"

    def get_context_data(self, *args, **kwargs):
        tmp = []
        objs = Link.objects.all()
        count = objs.count()
        row_num = 2
        if count <= row_num:
            tmp.append(objs)
        else:
            for i in range(count//row_num):
                start = i * row_num
                tmp.append(objs[start:start+row_num])
            _count = (i+1)*row_num
            if count > _count:
                tmp.append(objs[_count:])
        kwargs['object_list'] = tmp
        return super(LinkView, self).get_context_data(*args, **kwargs)
