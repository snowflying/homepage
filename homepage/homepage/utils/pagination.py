# coding: utf-8
from django.conf import settings
from django.core.paginator import Paginator


def get_pagination(queryset, page, num_per_page=settings.HOMEPAGE_NUM_PER_PAGE,
                   display_page_num=settings.HOMEPAGE_DISPLAY_PAGE_NUM):
    paginator = Paginator(queryset, num_per_page)

    try:
        page = int(page)
        if page < 1:
            page = 1
    except:
        page = 1

    try:
        objects = paginator.page(page)
    except:
        objects = paginator.page(paginator.num_pages)

    if display_page_num >= paginator.num_pages:
        start = 0
        end = paginator.num_pages
    else:
        _tmp = display_page_num // 2
        if page <= _tmp:
            start = 0
            end = display_page_num
        elif page + _tmp >= paginator.num_pages:
            start = paginator.num_pages - display_page_num
            end = paginator.num_pages
        else:
            start = page - _tmp - 1
            end = page + _tmp

    page_range = paginator.page_range[start:end]
    page_count = paginator.num_pages
    return {"page_object": objects, "page_range": page_range,
            "page_count": page_count, "object_list": objects.object_list}
