# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from aldryn_newsblog.forms import AutoAppConfigFormMixin

from . import models

class NewsBlogTaggedArticlesPluginForm(AutoAppConfigFormMixin, forms.ModelForm):
    class Meta:
        model = models.NewsBlogTaggedArticlesPlugin
        fields = ['app_config', 'tag', 'style', 'article_count',]


class NewsBlogTagRelatedPluginForm(AutoAppConfigFormMixin, forms.ModelForm):
    class Meta:
        model = models.NewsBlogTagRelatedPlugin
        fields = ['exclude_tags', 'style', 'article_count',]
