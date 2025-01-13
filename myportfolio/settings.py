"""
Django settings for myportfolio project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1xmo9g0*$#3=3eh%=c#v-*__5!*#_ff(4$wpk*0p46ufbr#3!8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myportfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'myportfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Static files (CSS, JavaScript, images) configurations
STATIC_URL = '/static/'  # URL to access static files

# In development, Django will look for static files in the static directories of your apps as well as the global static directory
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Global static directory for custom/static files
]

# For production, the static files will be collected here when running `python manage.py collectstatic`
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where to collect static files (used in production)

# Media files (user-uploaded content) configurations
MEDIA_URL = '/media/'  # URL to access media files
MEDIA_ROOT = BASE_DIR / 'media'  # Location where media files will be stored on the filesystem

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





# # Example email settings for development (console backend)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# CONTACT_EMAIL = 'jaivishwa.dev@gmail.com'  # The email address to receive contact form submissions


# Example email settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or another SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'jaivishwa.dev@gmail.com'
EMAIL_HOST_PASSWORD = 'ijxq eowz sjdi ssjp'  # Ensure this is securely managed
CONTACT_EMAIL = 'jaivishwa.dev@gmail.com'  # Email address where you want to receive contact form messages
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


