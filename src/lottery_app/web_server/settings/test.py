from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MEDIA_URL = 'media/'
DEVELOPMENT = True
KIIROO_BASE_URL = 'http://kiiroo.dev'

DEBUG = True
TEST = True

