# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_newsblog.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('cms', '0016_auto_20160608_1535'),
        ('aldryn_newsblog', '0015_auto_20161208_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsBlogTaggedArticlesPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', on_delete=models.CASCADE, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('style', models.CharField(default='standard', max_length=50, verbose_name='Style', choices=[('standard', 'Standard')])),
                ('article_count', models.PositiveIntegerField(default=10, help_text='The maximum number of tagged articles to display (0 for all).')),
                ('app_config', models.ForeignKey(verbose_name='Apphook configuration', to='aldryn_newsblog.NewsBlogConfig', on_delete=models.CASCADE)),
                ('tag', models.ForeignKey(verbose_name='tag', to='taggit.Tag', on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(aldryn_newsblog.models.PluginEditModeMixin, 'cms.cmsplugin'),
        ),
    ]
