aldryn-newsblog-extra-plugins
=============================

This projects contains extra plugins for the `aldryn-newsblog` blogging system
for DjangoCMS. It requires `aldryn-newsblog` to be installed and setup correctly.

# Configuration
Plugins that show a list of articles can be configured to show template choices,
inspired by `aldryn-events`. To add, for example, a template named `list`, save
it at `templates/aldryn-newsblog/plugins/(template name)` and add the following
to your `settings.py`:

```` Python
ALDRYN_NEWSBLOG_PLUGIN_STYLES = (
    'list',
)
````

# Plugins
## NewsBlogTaggedArticlesPlugin
Show `n` or all articles that are tagged with a certain tag.
This plugin shows style choices as described in "Configuration".

## NewsBlogTagRelatedPlugin
Show `n`or all articles that are similarly tagged as the currently displayed
article.

This plugin only works correctly in a static placeholder on the aldryn_newsblog
detail view.

# Changelog
## 0.1.0
NewsBlogTaggedArticlesPlugin now uses a separate template
(`aldryn_newsblog/plugins/tagged_articles.html`).
