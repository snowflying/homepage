# coding: utf-8
import os
import posixpath

from django.conf import settings
from django.http import Http404
from django.core import urlresolvers
from django.views import static
from django.contrib.staticfiles import finders


if settings.PY3:
    from urllib.parse import unquote
else:
    from urllib import unquote


# This function is copied from 'django.contrib.staticfiles.views'.
# But remove the settings.DEBUG.
def static_serve(request, path, document_root=None, insecure=False, **kwargs):
    """
    Serve static files below a given point in the directory structure or
    from locations inferred from the staticfiles finders.

    To use, put a URL pattern such as::

        (r'^(?P<path>.*)$', 'PATH_TO.utils.static_serve')

    in your URLconf.

    It uses the django.views.static view to serve the found files.
    """
    normalized_path = posixpath.normpath(unquote(path)).lstrip('/')
    absolute_path = finders.find(normalized_path)
    if not absolute_path:
        if path.endswith('/') or path == '':
            raise Http404("Directory indexes are not allowed here.")
        raise Http404("'%s' could not be found" % path)
    document_root, path = os.path.split(absolute_path)
    return static.serve(request, path, document_root=document_root, **kwargs)


# This function is copied form 'django.shortcuts' from django 1.5.
# Below 1.5, django hasn't this function.
def resolve_url(to, *args, **kwargs):
    """
    Return a URL appropriate for the arguments passed.

    The arguments could be:

        * A model: the model's `get_absolute_url()` function will be called.

        * A view name, possibly with arguments: `urlresolvers.reverse()` will
    be used to reverse-resolve the name.

        * A URL, which will be returned as-is.

    """
    # If it's a model, use get_absolute_url()
    if hasattr(to, 'get_absolute_url'):
        return to.get_absolute_url()

    # Next try a reverse URL resolution.
    try:
        return urlresolvers.reverse(to, args=args, kwargs=kwargs)
    except urlresolvers.NoReverseMatch:
        # If this is a callable, re-raise.
        if callable(to):
            raise
        # If this doesn't "feel" like a URL, re-raise.
        if '/' not in to and '.' not in to:
            raise

    # Finally, fall back and assume it's a URL
    return to
