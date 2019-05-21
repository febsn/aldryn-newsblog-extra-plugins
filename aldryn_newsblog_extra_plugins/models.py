# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext, ugettext_lazy as _

from aldryn_categories.fields import CategoryForeignKey, CategoryManyToManyField
from aldryn_newsblog.models import Article, PluginEditModeMixin, NewsBlogCMSPlugin, AdjustableCacheModelMixin
from aldryn_newsblog.utils.utilities import get_valid_languages_from_request
from cms.models.pluginmodel import CMSPlugin
from taggit.models import Tag
from taggit.managers import TaggableManager

from .utils import get_additional_styles


class PluginStyleMixin(models.Model):
    STANDARD = 'list'
    STYLE_CHOICES = [
        (STANDARD, _('Standard')),
    ]
    style = models.CharField(
        verbose_name=_('Style'),
        choices=STYLE_CHOICES + get_additional_styles(),
        default=STANDARD,
        max_length=50,
    )

    class Meta:
        abstract = True


@python_2_unicode_compatible
class NewsBlogTaggedArticlesPlugin(PluginEditModeMixin, PluginStyleMixin, NewsBlogCMSPlugin):
    tag = models.ForeignKey(
        Tag,
        verbose_name=_('tag'),
        on_delete=models.CASCADE,
    )
    article_count = models.PositiveIntegerField(
        default=10,
        help_text=_('The maximum number of tagged articles to display (0 for all).'),
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


@python_2_unicode_compatible
class NewsBlogTagRelatedPlugin(PluginEditModeMixin, PluginStyleMixin, AdjustableCacheModelMixin,
                            CMSPlugin):
    # NOTE: This one does NOT subclass NewsBlogCMSPlugin. This is because this
    # plugin can really only be placed on the article detail view in an apphook.
    exclude_tags = TaggableManager(verbose_name=_('excluded tags'), blank=True)
    article_count = models.PositiveIntegerField(
        default=10,
        help_text=_('The maximum number of tagged articles to display (0 for all).'),
    )

    def get_articles(self, article, request):
        """
        Returns a queryset of articles that have common tags with the given article.
        """
        languages = get_valid_languages_from_request(
            article.app_config.namespace, request)
        if self.language not in languages:
            return Article.objects.none()
        filter_tags = article.tags.exclude(
            pk__in=models.Subquery(self.exclude_tags.values('pk'))
        )
        queryset = Article.objects.filter(
            tags__in=article.tags.all()).exclude(
            tags__in=self.exclude_tags.all()).exclude(
            pk=article.pk).translated(*languages)
        if not self.get_edit_mode(request):
            queryset = queryset.published()
        queryset = queryset.distinct()
        if self.article_count > 0:
            queryset = queryset[:self.article_count]
        return queryset

    def __str__(self):
        return ugettext('Tag-related articles')


@python_2_unicode_compatible
class NewsBlogCategoryRelatedPlugin(PluginEditModeMixin,
                                    PluginStyleMixin,
                                    AdjustableCacheModelMixin,
                                    CMSPlugin):
    # NOTE: This one does NOT subclass NewsBlogCMSPlugin. This is because this
    # plugin can really only be placed on the article detail view in an apphook.

    exclude_categories = CategoryManyToManyField(verbose_name=_('excluded categories'), blank=True)
    article_count = models.PositiveIntegerField(
        default=10,
        help_text=_('The maximum number of related articles to display (0 for all).'),
    )


    def get_queryset(self, article, request):
        """
        Returns a queryset of articles that have common categories with the given article.
        """
        languages = get_valid_languages_from_request(
            article.app_config.namespace, request)
        if self.language not in languages:
            return Article.objects.none()
        filter_categories = article.categories.exclude(
            pk__in=models.Subquery(self.exclude_categories.values('pk'))
        )
        queryset = Article.objects.filter(
            categories__in=filter_categories
        ).exclude(
            pk=article.pk
        ).translated(
            *languages
        )
        if not self.get_edit_mode(request):
            queryset = queryset.published()
        return queryset.distinct()


    def get_articles(self, article, request):
        queryset = self.get_queryset(article, request)
        if self.article_count > 0:
            queryset = queryset[:self.article_count]
        return queryset

    def __str__(self):
        return ugettext('Category-related articles')


@python_2_unicode_compatible
class NewsBlogLatestArticlesByCategoryPlugin(PluginEditModeMixin,
                                             PluginStyleMixin,
                                             AdjustableCacheModelMixin,
                                             NewsBlogCMSPlugin):
    category = CategoryForeignKey(
        verbose_name=_('category'),
    )
    article_count = models.IntegerField(
        default=10,
        verbose_name=_('count'),
        help_text=_("The maximum number of latest articles to display."),
    )

    def get_articles(self, request):
        """
        Return a queryset of the latest articles, filtered by the category set in the plugin
        settings and sliced to the desired count.
        """
        queryset = Article.objects
        if not self.get_edit_mode(request):
            queryset = queryset.published()
        languages = get_valid_languages_from_request(
            self.app_config.namespace, request)
        if self.language not in languages:
            return queryset.none()
        queryset = queryset.translated(*languages).filter(
            app_config=self.app_config).filter(
            categories=self.category)
        if self.article_count > 0:
            queryset = queryset[:self.article_count]
        return queryset

    def __str__(self):
        return ugettext("{app_title}'s {article_count} latest articles with category {category}".format(
            app_title=self.app_config.get_app_title(),
            article_count=self.article_count,
            category=self.category,
        ))
