'''
Created on 9.4.2012

@author: xaralis
'''
from django.conf import settings

# Example asset format:
#
# ASSETS = {
#     'css': {
#         'css/main.css': {
#             'media': ('print', 'screen', 'projection'),
#             'files': ('css/main.css',),
#             'version': 1
#         }
#     },
#     'js': {
#         'js/main.js': {
#             'files': ('js/main.js',),
#             'version': 1
#         }
#     }
# }

ASSETS = settings.STATICS_ASSETS
ASSET_DIR = getattr(settings, 'STATICS_ASSET_DIR', settings.STATIC_ROOT)
USE_VERSIONING = getattr(settings, 'STATICS_USE_VERSIONING', not settings.DEBUG)
USE_MINIFIED = getattr(settings, 'STATICS_USE_MINIFIED', not settings.DEBUG)
