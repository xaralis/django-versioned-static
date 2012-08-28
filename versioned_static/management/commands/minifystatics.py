'''
Created on 9.4.2012

@author: xaralis
'''
from os import path
from os.path import join
import subprocess

from django.core.management.base import BaseCommand

from versioned_static.conf import ASSETS, ASSET_DIR
from versioned_static.templatetags.versioned_static_tags import versioned


class Command(BaseCommand):
    def minify_asset(self, atype, aname):
        if atype not in ('css', 'js'):
            print "Invalid asset type %r, asset type can be css or js." % atype
            return

        if aname not in ASSETS[atype]:
            print "Asset %r not found in settings. Did you misspell it?" % aname

        meta = ASSETS[atype][aname]
        pth = join(ASSET_DIR, versioned(aname, meta['version'], True))
        files = [join(ASSET_DIR, f) for f in meta['files']]
        files_ok = True

        if not files:
            print "Warning: Empty file list."
            return

        for f in files:
            if not path.exists(f):
                print "Error: File doesn't exist: %r" % f
                files_ok = False

        if not files_ok:
            return

        if files:
            cmd = 'cat %s | yuicompressor --type %s > %s' % (' '.join(files), atype, pth)
            subprocess.call(cmd, shell=True)

    def handle(self, *args, **options):
        if len(args) == 0:
            for atype in ASSETS.keys():
                for aname in ASSETS[atype].keys():
                    print "Minifying %s ..." % aname
                    self.minify_asset(atype, aname)

            return

        if not len(args) == 2:
            print "Usage: django-admin.py minifystatics [[css/js] [BASE_ASSET]]"
            return

        self.minify_asset(**args)

