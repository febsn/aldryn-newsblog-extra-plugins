# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from aldryn_newsblog.models import Article
from . import forms, models

@plugin_pool.register_plugin
class NewsBlogTaggedArticlesPlugin(CMSPluginBase):
    model = models.NewsBlogTaggedArticlesPlugin
    name = _('Tagged Articles')
    module = _('News & Blog')
    form = forms.NewsBlogTaggedArticlesPluginForm
    
    TEMPLATE_NAME = 'aldryn_newsblog/plugins/%s.html'
    TEMPLATE_DEFAULT = 'list'
    render_template = TEMPLATE_NAME % TEMPLATE_DEFAULT
    
    def render(self, context, instance, placeholder):
        request = context.get('request')
        if instance.style:
            self.render_template = self.TEMPLATE_NAME % instance.style
        context['instance'] = instance
        context['article_list'] = instance.get_articles(request)
        return context