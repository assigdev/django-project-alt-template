# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
]

PROJECT_APPS = [
    'apps.main',
]


INSTALLED_APPS = [
    'django_extensions',
]

DEV_APPS = [
    'debug_toolbar'
]

PROD_APPS = [
    'raven.contrib.django.raven_compat',
]

INSTALLED_APPS = DJANGO_APPS + INSTALLED_APPS + PROJECT_APPS
