# -*- coding: utf-8 -*-
from base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kiiroo_dashboard',
        'USER': 'root',
        'PASSWORD': 'local',
        'HOST': 'mysql',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=INNODB'
        }
    }
}


MEDIA_URL = 'media/'
DEVELOPMENT = True
KIIROO_BASE_URL = 'http://kiiroo.dev'

DEBUG = True

DEBUG_LOG_DIR = BASE_DIR + "-django.log"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # How to format the output
    'formatters': {
        'standard': {
            'format': "[%(asctime)s.%(msecs)03d] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S:"
        },
    },
    # Log handlers (where to go)
    'handlers': {
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': DEBUG_LOG_DIR,
            'maxBytes': 50000,
            'backupCount': 10,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    # Loggers (where does the log come from)
    'loggers': {
        'api': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'dashboard': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'kiiroodashboard': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console', 'log_file'],
            'level': 'WARN',
            'propagate': False,
        },
        'requests': {
            'handlers': ['console', 'log_file'],
            'level': 'WARN',
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
        },
    }
}

try:
    from local import *
    print "Overwrintting with local.py"
except ImportError:
    pass
