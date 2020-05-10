#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    if '--dev' in sys.argv:
        del sys.argv[sys.argv.index('--dev')]
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kiiroodashboard.settings.dev")
    elif '--production' in sys.argv:
        del sys.argv[sys.argv.index('--production')]
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kiiroodashboard.settings.production")
    elif '--local' in sys.argv:
        print "See README on how to overwrite 'dev' settings with 'local'"
        sys.exit(1)
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kiiroodashboard.settings.test")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
