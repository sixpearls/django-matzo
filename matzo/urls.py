#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(regex=r'^(?P<url>.*)$', view=FlatpageView.as_view(), name="FlatPage"),
)