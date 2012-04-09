import os
import versioned_static

# helper for building absolute paths
PROJECT_ROOT = os.path.abspath(os.path.dirname(versioned_static.__file__))
p = lambda x: os.path.join(PROJECT_ROOT, x)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'versioned_static',
        'USER': 'root',
        'PASSWORD': '',
    },
}

# media serving
MEDIA_ROOT = p('media')
MEDIA_URL = '/media/'

STATIC_ROOT = p('staticc')
STATIC_URL = '/static/' 

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# cache conf
CACHE_BACKEND = 'dummy://'

