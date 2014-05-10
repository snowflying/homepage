# -*- coding: utf-8 -*-

import os
import sys

if sys.version_info[0] < 3:
    PY3 = False
else:
    PY3 = True

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DOMAIN = '/'

_DB_DIR = os.path.join(ROOT_PATH, "db")
if not os.path.isdir(_DB_DIR):
    os.mkdir(_DB_DIR)

if not DOMAIN:
    DOMAIN = '/'
elif DOMAIN[-1] != '/':
    DOMAIN = DOMAIN + '/'

sys.path.insert(0, os.path.join(ROOT_PATH, 'django_packages'))

DEBUG = True
#DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('xgfone', 'xgfone@126.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(_DB_DIR, "data.db"),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'en'

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = DOMAIN

MEDIA_ROOT = os.path.join(ROOT_PATH, "..", "media")
MEDIA_URL = ''.join((DOMAIN, 'media/'))
if not os.path.isdir(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)

STATIC_ROOT = os.path.join(ROOT_PATH, '..', "static")
STATIC_URL = ''.join((DOMAIN, 'static/'))
STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, "static"),
)
if not os.path.isdir(STATIC_ROOT):
    os.mkdir(STATIC_ROOT)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'homepage.context_processors.title_suffix',
    'homepage.context_processors.home_page',
    'homepage.context_processors.current_year',
    'homepage.context_processors.current_page',
    'homepage.context_processors.current_path',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'south',
    'grappelli',
    'filebrowser',  # django-filebrowser -- Media-Management with Grappelli
    'django.contrib.admin',
    'django.contrib.admindocs',
    # 'tinymce',  # django-tinymce -- tinymce for Django

    'homepage.blog',
    'homepage.about',
    'homepage.message',
    'homepage.website',
)

# This project's configuration
HOMEPAGE_TITLE_SUFFIX = '三界的站点'
HOMEPAGE_DISPLAY_PAGE_NUM = 9
HOMEPAGE_NUM_PER_PAGE = 10
HOMEPAGE_MESSAGE_NUM_PER_PAGE = 20

# duoshuo
DUOSHUO_SHORT_NAME = 'xgfone'
DUOSHUO_SECRET = 'db59d6c6a7d55519aa2179b83f1b0dd2'
# DUOSHUO_SHORT_NAME = 'test123'
# DUOSHUO_SECRET = '6f37e009f6c99bc38db6ec95ef29572a'
