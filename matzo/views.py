#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from textify.models import TextifyPage
from django.contrib.flatpages.views import DEFAULT_TEMPLATE
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.views.generic.detail import DetailView
from django.core import serializers
import os
import re

from bakery.views import BuildableDetailView

class FlatPageView(DetailView):
    model = FlatPage
    context_object_name = 'flatpage'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_queryset(self):
        qs = super(FlatpageView, self).get_queryset().filter(sites__id__exact=settings.SITE_ID)

        if 'user' not in self.request or not self.request.user.is_authenticated:
            self.queryset = qs.filter(registration_required=False)
        else:
            self.queryset = qs
        return self.queryset._clone()

    def get_object(self,queryset=None):
        obj = super(FlatpageView,self).get_object(queryset)
        # mark fields as safe
        obj.content = mark_safe(obj.content)
        obj.title = mark_safe(obj.title)
        return obj
 
    def dispatch(self, request, *args, **kwargs):
        # fix URL if needed
        if kwargs['url'] == '':
            pass
        elif not kwargs['url'].endswith('/') and settings.APPEND_SLASH:
            return HttpResponseRedirect("%s/" % request.path)
        if not kwargs['url'].startswith('/'):
            kwargs['url'] = "/" + kwargs['url']
        # continue dispatch
        return super(FlatpageView, self).dispatch(request, *args, **kwargs)
 
    def get_template_names(self):
        template_names = super(FlatpageView, self).get_template_names()
        if self.object.template_name:
            template_names.insert(0, self.object.template_name)
        template_names.append(DEFAULT_TEMPLATE)
        return template_names

class BakedFlatpageView(BuildableDetailView,FlatpageView):
    queryset = FlatPage.objects.filter(sites__id__exact=settings.SITE_ID,registration_required=False) 