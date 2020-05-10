# -*- coding: utf-8 -*-
from base import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'Please setup environment variables'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;'
        }
    }
}
DEBUG = False
DEVELOPMENT = False

DEBUG_LOG_DIR = "/opt/python/log/dashboard.log"

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
            'maxBytes': 10000000,
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
            'handlers': ['log_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'dashboard': {
            'handlers': ['log_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'kiiroodashboard': {
            'handlers': ['log_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['log_file'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['log_file'],
            'level': 'WARN',
            'propagate': False,
        },
        'requests': {
            'handlers': ['log_file'],
            'level': 'WARN',
            'propagate': False,
        },
        '': {
            'handlers': ['log_file'],
            'level': 'INFO',
        },
    }
}
