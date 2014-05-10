# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.conf import settings
from filebrowser.sites import site
from homepage.utils.sitemap import sitemaps
from homepage.utils.rss import BlogFeed
from homepage.views import LoginView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('homepage.views',
    url(r'^$', 'index', name='index'),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^logout', 'my_logout', name="logout"),
)

urlpatterns += patterns('',
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)

# App urls.
urlpatterns += patterns('',
    url(r'^blog/', include('homepage.blog.urls')),
    url(r'^about/', include('homepage.about.urls')),
    url(r'^message/', include('homepage.message.urls')),
    url(r'^website/', include('homepage.website.urls')),
)

# Defaultly, We serve static files or media files, but it's not a good idea.
# You have better use a static file server to serve them, such as Apache, Nginx.
# When you use a static file server, the following URLConf should be invalid.
urlpatterns += patterns('', url(r'^static/(?P<path>.*)$', 'homepage.utils.static_serve'))
urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps},
        name='sitemap'),
    url(r'^rss$', BlogFeed()),
)
