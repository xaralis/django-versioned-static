django-versioned-static
------------------------

This little apps helps to manage your staticfiles when you need to minify
them for production use. Moreover, it is capable of versioning the assets
so that whenever you need to alter the static files, users won't be given
old file from the browser cache.

Installation
=============

Standard Django way::
    
    pip install django-versioned-static
    
Add to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ..
        ..,
        'versioned_static',
        ...
    )
    
Configure the assets themselves::

    STATICS_ASSETS = {
        'css': {
            'css/mycoolproject.css': {
                'media': ('screen', 'projection', 'tv'),
                'files': ('css/jquery-ui-1.8.18.custom.css', 'css/style.css',),
                'version': 1
            },
            'css/print.css': {
                'media': ('print',),
                'files': ('css/print.css',),
                'version': 1
            }
        },
        'js': {
            'js/mycoolproject.js': {
                'files': ('js/jquery-1.7.1.min.js',
                          'js/main.js'),
                'version': 1
            }
        }
    }

Done!

Usage in templates
==================

Very simple. Use the ``asset`` template tag. Give it the static type (css or js)
and the base css alias. It will generate all the necessary HTML for you directly:: 

    {% load versioned_statics_tags %}
    {% asset "css" "css/mycoolproject.css" %}
    {% asset "css" "css/print.css" %}
    {% asset "js" "js/mycoolproject.js" %}
    
It takes your settings in the account. In development (when ``DEBUG = True``),
you will be given unversioned and unminified static files. When you turn 
the debug off, you will be given versioned asset links.

**Result with DEBUG=True**::

    <link type="text/css" rel="stylesheet" href="/static/css/jquery-ui-1.8.18.custom.css" media="screen,projection,tv"/>
    <link type="text/css" rel="stylesheet" href="/static/css/style.css" media="screen,projection,tv"/>
    
    <link type="text/css" rel="stylesheet" href="/static/css/print.css" media="print"/>
    
    <script type="text/javascript" src="/static/js/jquery-1.7.1.min.js"></script>
    <script type="text/javascript" src="/static/js/main.js"></script>
    
**Result with DEBUG=False**::
    
    <link type="text/css" rel="stylesheet" href="/static/css/mycoolproject.1.css" media="screen,projection,tv"/>
    
    <link type="text/css" rel="stylesheet" href="/static/css/print.1.css" media="print"/>
    
    <script type="text/javascript" src="/static/js/mycoolproject.1.js"></script>
    
    
Minifying the files
===================

This app features simple management command which helps you create the minified
files for production. Usage goes like this::

    django-admin.py minifystatics (CSS/JS) ASSET_FILE
    
Real example for previous scenario::

    django-admin.py minifystatics css css/print.css
    
The command will look in your ``STATIC_ROOT`` by default (so be sure you
ran collectstatic before the minify command) and use it as the root path.