'''
Created on 9.4.2012

@author: xaralis
'''
from django import template
from django.conf import settings
from django.templatetags.static import static

from versioned_static.conf import ASSETS, USE_MINIFIED, USE_VERSIONING

register = template.Library()


@register.inclusion_tag('versioned_static/render_asset.html')
def asset(atype, aname):
    """
    Renders CSS/JS asset with it's enclosing HTML tag (link/script). If asset
    is composed from multiple files, this will be preserved (unless minifyed).
    Respects settings if versioning should be incorporated or not.
    """
    if atype not in ('css', 'js'):
        raise template.TemplateSyntaxError('Type can only be one of css or js.')

    if aname not in ASSETS[atype]:
        raise ValueError('Invalid asset: %r' % aname)

    meta = ASSETS[atype][aname]

    return {
        'USE_MINIFIED': USE_MINIFIED,
        'type': atype,
        'asset': aname,
        'meta': meta,
    }


@register.simple_tag
def versioned(filename, version, force_version=False, full_path=True):
    """
    Returns filename enriched with version given as second argument.
    """
    if not '.' in filename:
        return None

    if USE_VERSIONING or force_version:
        dotindex = filename.rindex('.')
        filename = u'%s.%s%s' % (filename[:dotindex], version, filename[dotindex:])

    if full_path:
        return static(filename)

    return filename
