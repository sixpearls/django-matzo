django-matzo
============

An app to use ``django-bakery`` with the ``FlatPage`` built-in app. Also compatible with ``django-textify``.

To use:

    0. Add ``matzo`` to your ``INSTALLED_APPS``
    1. Remove ``django.contrib.flatpages.middleware.FlatpageFallbackMiddleware`` from your ``MIDDLEWARE_CLASSES``
    2. Add ``matzo.urls.urlpatterns`` to your urls, like so: ::
        # project urls.py
        import matzo.urls

        urlpatterns += matzo.urls.urlpatterns
