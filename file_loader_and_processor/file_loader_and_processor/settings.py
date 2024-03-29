"""
Django settings for file_loader_and_processor project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-o(dd1olm6*!9h1m=4i28b7fq^d!l3r0zth)m!awt4(y^0^x&+^')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost']

if os.environ.get('ALLOWED_HOSTS') is not None:
    try:
        ALLOWED_HOSTS += os.environ.get('ALLOWED_HOSTS').split(',')
    except Exception as e:
        print('Cant set ALLOWED_HOSTS, using default instead')


# Application definition

INSTALLED_APPS = [
    # core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local
    'main.apps.MainConfig',

    # 3-rd party
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'file_loader_and_processor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'file_loader_and_processor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DB_SQLITE = 'sqlite'
DB_POSTGRESQL = 'postgresql'

DATABASES_ALL = {
    DB_SQLITE: {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    DB_POSTGRESQL: {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'NAME': os.environ.get('POSTGRES_NAME', 'picaso_postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'picaso_postgres_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'picaso_postgres_password'),
        'PORT': int(os.environ.get('POSTGRES_PORT', '5432')),
    },
}

DATABASES = {'default': DATABASES_ALL[os.environ.get('DJANGO_DB', DB_SQLITE)]}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/django_static/'
STATIC_ROOT = BASE_DIR / 'django_static'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# celery
CELERY_BROKER_URL = os.environ.get("BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("RESULT_BACKEND", "redis://localhost:6379/0")
