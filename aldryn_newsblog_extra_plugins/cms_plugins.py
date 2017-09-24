# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _

from aldryn_newsblog.models import Article
from aldryn_newsblog.cms_plugins import NewsBlogRelatedPlugin
from . import forms, models

class StyleTemplateMixin(object):
    def get_render_template(self, context, instance, placeholder):
        template = select_template((
            self.TEMPLATE_NAME.format(instance.style),
            self.TEMPLATE_NAME.format(self.TEMPLATE_DEFAULT),
        ))
        return template

@plugin_pool.register_plugin
class NewsBlogTaggedArticlesPlugin(StyleTemplateMixin, CMSPluginBase):
    name = _('Tagged Articles')
    module = _('News & Blog')
    model = models.NewsBlogTaggedArticlesPlugin
    form = forms.NewsBlogTaggedArticlesPluginForm

    TEMPLATE_NAME = 'aldryn_newsblog/plugins/{}.html'
    TEMPLATE_DEFAULT = 'tagged_articles'

    def render(self, context, instance, placeholder):
        request = context.get('request')
        context['instance'] = instance
        context['article_list'] = instance.get_articles(request)
        return context


@plugin_pool.register_plugin
class NewsBlogTagRelatedPlugin(StyleTemplateMixin, NewsBlogRelatedPlugin):
    name = _('Similarly tagged Articles')
    module = _('News & Blog')
    model = models.NewsBlogTagRelatedPlugin
    form = forms.NewsBlogTagRelatedPluginForm

    TEMPLATE_NAME = 'aldryn_newsblog/plugins/{}.html'
    TEMPLATE_DEFAULT = 'related_articles'
