# -*- coding: utf-8 -*-

import os
import ssl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zca#dogkiofb^#3+yu^$_6!rg$+^o*_#0r9((xkz_25^z_93zf'

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = ['*']

# Order update webhooks signature
SENTRY_DSN = os.getenv('SENTRY_DSN')

# OrderDashboard Fullfillment updater credentials
# Obtained from https://kiiroo-amsterdam.myshopify.com/admin/apps/private/67040179
SHOPIFY_API_KEY = os.getenv('SHOPIFY_API_KEY')
SHOPIFY_API_SECRET_KEY = os.getenv('SHOPIFY_API_SECRET_KEY')
SHOPIFY_SHOP_NAME = os.getenv('SHOPIFY_SHOP_NAME', "kiiroo-amsterdam")

# Application definition

INSTALLED_APPS = [
    'dashboard.apps.DashboardConfig',
    'partners.apps.PartnersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rangefilter',
    'storages',
    'captcha',
    'raven.contrib.django.raven_compat',
    'simple_history',
    'dashboard_app.two_factor_authentication'
]

RAVEN_CONFIG = {
    'dsn': SENTRY_DSN,
}
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',

]

########## Django Security Settings ##########

# Send cookie encryped, under an HTTPS connection to avoid packet sniffing.
# It is trivial for a packet sniffer (e.g. Firesheep) to hijack a user’s session, if the session cookie is sent unencrypted
SESSION_COOKIE_SECURE = True

# Send CSRF cookie encryped, under an HTTPS connection to avoid packet sniffing.
CSRF_COOKIE_SECURE = True

########## SECURITY provided by Middlewares ##########

# provided by the 'SecurityMiddleware'
# Serve with an 'x-content-type-options: nosniff' header to prevent the browser from identifying content types incorrectly
# see https://docs.djangoproject.com/en/1.11/ref/middleware/#x-content-type-options
# and https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True

# provided by the SecurityMiddleware
# serve pages with an 'x-xss-protection: 1; mode=block' header to activate the browser's XSS filtering and help prevent XSS attacks
# see https://docs.djangoproject.com/en/1.11/ref/middleware/#x-xss-protection
# and https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

# provided by 'django.middleware.clickjacking.XFrameOptionsMiddleware'
# Unless there is a good reason for your site to serve other parts of itself in a frame,
# you should have X_FRAME_OPTIONS = 'DENY' (Default in Django 1.11 is X_FRAME_OPTIONS = 'SAMEORIGIN')
# see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
X_FRAME_OPTIONS = 'DENY'



ROOT_URLCONF = 'kiiroodashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kiiroodashboard.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SOUTH_MIGRATION_MODULES = {
    'captcha': 'captcha.south_migrations',
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

APPEND_SLASH = False

# whenever the @login_required decorator is used and user is not logged in then there is a redirect to the below url
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

FLESHLIGHT_API_KEY = os.getenv('FLESHLIGHT_API_KEY', 'fleshlight-api-key')
FLESHLIGHT_API_SECRET = os.getenv('FLESHLIGHT_API_SECRET', 'fleshlight-api-secret')
FLESHLIGHT_API_BASE_URL = os.getenv('FLESHLIGHT_API_BASE_URL', 'fleshlight-api-url')

RAKUTEN_API_BASE_URL = os.getenv('RAKUTEN_API_BASE_URL', 'localhost')
RAKUTEN_NEW_ORDER_API_BASE_URL = os.getenv('RAKUTEN_NEW_ORDER_API_BASE_URL', 'localhost')
RAKUTEN_CUSTOMER_ID = os.getenv('RAKUTEN_CUSTOMER_ID', '9999')
RAKUTEN_PASSWORD = os.getenv('RAKUTEN_PASSWORD', 'secret')

WAREHOUSE_API_SECRET = os.getenv('WAREHOUSE_API_SECRET', '')
MAX_WAREHOUSE_ORDERS = os.getenv('MAX_WAREHOUSE_ORDERS', 50)

EU_COUNTRIES = [
    'BE',   # Belgium
    'BG',   # Bulgaria
    'CY',   # Cyprus
    'DK',   # Denmark
    'DE',   # Germany
    'EE',   # Estonia
    'FI',   # Finland
    'FR',   # France
    'GR',   # Greece
    'HU',   # Hungary
    'IE',   # Ireland
    'IT',   # Italy
    'HR',   # Croatia
    'LV',   # Latvia
    'LT',   # Lithuania
    'LU',   # Luxembourg
    'MT',   # Malta
    'NL',   # Netherlands
    'AT',   # Austria
    'PL',   # Poland
    'PT',   # Portugal
    'RO',   # Romania
    'SI',   # Slovenia
    'SK',   # Slovakia
    'ES',   # Spain
    'CZ',   # Czech Republic
    'GB',   # United Kingdom
    'UK',   # United Kingdom (unofficial)
    'SE'    # Sweden
]

VAT_PERCENTAGE = 21

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', 'dashboard.kiiroo.com')
AWS_S3_HOST = os.getenv('AWS_S3_HOST', 's3-eu-west-1.amazonaws.com')

IS_RAKUTEN_TEST = os.getenv('IS_RAKUTEN_TEST', None)

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

DEFAULT_PARTNER_COMMISSION = 25

KIIROO_AFFILIATE_API_KEY = os.getenv('KIIROO_AFFILIATE_API_KEY')
KIIROO_BASE_URL = 'https://www.kiiroo.com'
ZOHO_APPLICATION_KEY = os.getenv('ZOHO_APPLICATION_KEY')
ZOHO_BASE_URL = os.getenv('ZOHO_BASE_URL', 'https://crm.zoho.com/crm/private/xml')
ZOHO_SCOPE = 'crmapi'

DEFAULT_FROM_EMAIL = 'Kiiroo <noreply@kiiroo.com>'

STATIC_ROOT = "prodstatic/"

SHOPIFY_LOCATIONS = {
    'RK': int(os.getenv('RK_LOCATION', 0)),
    'JN': int(os.getenv('JN_LOCATION', 0)),
    'FL': int(os.getenv('FL_LOCATION', 0)),
    'DEFAULT': int(os.getenv('DEFAULT_LOCATION', 0)),
}

INVENCO_WEB_API_URL = os.getenv('INVENCO_WEB_API_URL')
INVENCO_API_KEY = os.getenv('INVENCO_API_KEY')
