# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from aldryn_newsblog.models import Article, PluginEditModeMixin, NewsBlogCMSPlugin
from aldryn_newsblog.utils.utilities import get_valid_languages_from_request
from taggit.models import Tag

from .utils import get_additional_styles

STANDARD = 'standard'

@python_2_unicode_compatible
class NewsBlogTaggedArticlesPlugin(PluginEditModeMixin, NewsBlogCMSPlugin):
    STYLE_CHOICES = [
        (STANDARD, _('Standard')),
    ]

    tag = models.ForeignKey(Tag, verbose_name=_('tag'))
    style = models.CharField(
        verbose_name=_('Style'),
        choices=STYLE_CHOICES + get_additional_styles(),
        default=STANDARD,
        max_length=50
    )
    article_count = models.PositiveIntegerField(
        default=10,
        help_text=_('The maximum number of tagged articles to display (0 for all).')
    )

    def __str__(self):
        if not self.pk:
            return 'tagged articles'
        return "%(count)s articles tagged by %(tag)s" % {
            'count': self.article_count,
            'tag': self.tag.__str__(),
        }

    def get_articles(self, request):
        queryset = Article.objects
        if not self.get_edit_mode(request):
            queryset = queryset.published()
        languages = get_valid_languages_from_request(
            self.app_config.namespace, request)
        if self.language not in languages:
            return queryset.none()
        queryset = queryset.translated(*languages).filter(
            app_config=self.app_config,
            tags=self.tag)
        if self.article_count > 0:
            queryset = queryset[:self.article_count]
        return queryset