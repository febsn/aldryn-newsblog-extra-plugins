# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
import six

def get_additional_styles(extra_name=False):
    """
    Get additional styles choices from settings

    Copied from aldryn-events.utils
    """
    choices = []
    if extra_name:
        raw = getattr(settings, extra_name,
            getattr(settings, 'ALDRYN_NEWSBLOG_PLUGIN_STYLES', False)
        )
    else:
        raw = getattr(settings, 'ALDRYN_NEWSBLOG_PLUGIN_STYLES', False)

    if raw:
        if isinstance(raw, six.string_types):
            raw = raw.split(',')
        for choice in raw:
            try:
                # Happened on aldryn to choice be a tuple with two
                # empty strings and this break the deployment. To avoid that
                # kind of issue if something fais we just ignore.
                clean = choice.strip()
                choices.append((clean.lower(), clean.title()))
            except Exception:
                pass

    return choices
