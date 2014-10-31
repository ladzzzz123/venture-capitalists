"""
Django settings for webapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'ENTER'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
DJANGORESIZED_DEFAULT_SIZE = [500, 500]
MAX_UPLOAD_SIZE = "5242880"  # about 5MB

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'company_directory',
    'home',
    'django_extensions',
    'pipeline',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'webapp.urls'

WSGI_APPLICATION = 'webapp.wsgi.application'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE_CSS = {
    'styles': {
        'source_filenames': (
            'home/style.scss',
        ),
        'output_filename': 'css/style.css',
    },
}

PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
            'home/static/js/global.js',
        ),
        'output_filename': 'js/scripts.js',
    }
}

if os.environ['DJANGO_ENV'] == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_app_default',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '127.0.0.1',
            'PORT': 3306,
        }
    }
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = (
    )
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
elif os.environ['DJANGO_ENV'] == 'staging':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django_app_default',
            'USER': 'ENTER',
            'PASSWORD': 'ENTER',
            'HOST': 'ENTER',
            'PORT': 'ENTER',
        }
    }
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
elif os.environ['DJANGO_ENV'] == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
