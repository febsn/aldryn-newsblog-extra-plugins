# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers
import aldryn_newsblog.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('cms', '0016_auto_20160608_1535'),
        ('aldryn_newsblog_extra_plugins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsBlogTagRelatedPlugin',
            fields=[
                ('cache_duration', models.PositiveSmallIntegerField(default=0, help_text="The maximum duration (in seconds) that this plugin's content should be cached.")),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', on_delete=models.CASCADE, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('exclude_tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=(aldryn_newsblog.models.PluginEditModeMixin, 'cms.cmsplugin', models.Model),
        ),
        migrations.AlterField(
            model_name='newsblogtaggedarticlesplugin',
            name='style',
            field=models.CharField(default='list', max_length=50, verbose_name='Style', choices=[('list', 'Standard'), (b'list', b'List'), (b'slider', b'Slider'), (b'comprehensive list', b'Comprehensive List')]),
        ),
    ]
