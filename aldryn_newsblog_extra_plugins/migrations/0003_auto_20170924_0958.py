# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog_extra_plugins', '0002_auto_20170711_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsblogtagrelatedplugin',
            name='article_count',
            field=models.PositiveIntegerField(help_text='The maximum number of tagged articles to display (0 for all).', default=10),
        ),
        migrations.AddField(
            model_name='newsblogtagrelatedplugin',
            name='style',
            field=models.CharField(choices=[('list', 'Standard')], verbose_name='Style', max_length=50, default='list'),
        ),
        migrations.AlterField(
            model_name='newsblogtaggedarticlesplugin',
            name='style',
            field=models.CharField(choices=[('list', 'Standard')], verbose_name='Style', max_length=50, default='list'),
        ),
        migrations.AlterField(
            model_name='newsblogtagrelatedplugin',
            name='exclude_tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='excluded tags', to='taggit.Tag', help_text='A comma-separated list of tags.', blank=True),
        ),
    ]
