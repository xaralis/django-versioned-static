'''
Created on 9.4.2012

@author: xaralis
'''
from os.path import join
import subprocess

from django.core.management.base import BaseCommand

from versioned_static.conf import ASSETS, ASSET_DIR
from versioned_static.templatetags.versioned_static_tags import versioned


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not len(args) == 2:
            print "Usage: django-admin.py minifystatics [css/js] [BASE_ASSET]"
            return

        atype, aname = args

        if atype not in ('css', 'js'):
            print "Invalid asset type %r, asset type can be css or js." % atype
            return

        if aname not in ASSETS[atype]:
            print "Asset %r not found in settings. Did you misspell it?" % aname

        meta = ASSETS[atype][aname]
        pth = join(ASSET_DIR, versioned(aname, meta['version']))
        files = ' '.join([join(ASSET_DIR, f) for f in meta['files']])

        cmd = 'yui-compressor --type %s %s > %s' % (atype, files, pth)
        subprocess.call(cmd, shell=True)
