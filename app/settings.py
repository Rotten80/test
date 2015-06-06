#encoding: UTF-8
"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kye%8taq%oqtx^+8c#1w1!3@(6cvl!1&==8fayyq3x0+cq(d9f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEV_SERVER = True
CELERY = False

TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (
    'app.mod',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if DEBUG:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'test',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'db_admin',
            'PASSWORD': '4621229',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            # TODO УСТАНОВЛЕН ДРУГОЙ ПОРТ ДЛЯ ЛОКАЛЬНОГО СЕРВЕРА!!!!
            'PORT': '5433',                      # !!!! Set to empty string for default. !!!!
            'CONN_MAX_AGE': None
            #'ATOMIC_REQUESTS': True
            #'AUTOCOMMIT': False
        },
    }

    ALLOWED_HOSTS = ["localhost","127.0.0.1"]

    TIME_ZONE = 'Asia/Yekaterinburg'

    MEDIA_ROOT = '/var/www/media/'
    MEDIA_URL = ''
    STATIC_ROOT = '/var/www/static/'
    STATIC_URL = '/static/'

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'test',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'db_admin',
            'PASSWORD': 'd_4621229RU*',
            'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            # TODO УСТАНОВЛЕН ДРУГОЙ ПОРТ ДЛЯ ЛОКАЛЬНОГО СЕРВЕРА!!!!
            'PORT': '',                      # !!!! Set to empty string for default. !!!!
            'CONN_MAX_AGE': 180
        },
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

APP_SETTINGS = {"a":1,"b":2}