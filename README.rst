django-matzo
============

An app to use ``django-bakery`` with the ``FlatPage`` built-in app. Also compatible with ``django-textify``.

To configure:

1. Add ``matzo`` to your ``INSTALLED_APPS``

2. Remove ``django.contrib.flatpages.middleware.FlatpageFallbackMiddleware`` from your ``MIDDLEWARE_CLASSES``

3. Add ``matzo.urls.urlpatterns`` to your urls, to dynamically view the flatpages without the middleware

4. Add ``matzo.BakedFlatpageView`` to your ``BAKERY_VIEWS``
