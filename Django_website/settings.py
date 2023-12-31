"""
Django settings for Django_website project.

Generated by 'django-admin startproject' using Django 3.2.20.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
# import os for static root
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

##############################################################
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = removed and stored as an environment variable
# retrieve it
# Create a .env file in your project's root directory and add your SECRET_KEY there.
# You should also add this file to your .gitignore to ensure it's not committed to your repository
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
################################################################

# SECURITY WARNING: don't run with debug turned on in production!
# comment out true when in development
# note: when false, remember to include whitenoise in middleware to serve static files
DEBUG = True
#DEBUG = False

# when debug=false,set to '*'
# to allow requests from any host/domain name.
# This is useful during development
# or when you don't know the exact host/domain name that will be used to access your application.
# NOTE: only do this in development environments or when certain the application is not exposed to the internet
ALLOWED_HOSTS = ['*']


# Application definition
# add the names of the apps created in cmd
INSTALLED_APPS = [
    'user_auth',
    'catalogue',
    'blog',
    'polls',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Django does not have a built-in solution for serving static files, when DEBUG has to be False in production
# use WhiteNoise, which is a Python library, built for serving static files
# do pip install whitenoise in cmd

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # To make Django aware of you wanting to run WhitNoise, you have to specify it in the MIDDLEWARE list 
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Django_website.urls'

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

WSGI_APPLICATION = 'Django_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
# tell django to look where for the static files you have added write this above STATIC_URL = ‘/static/’
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    ]

STATIC_URL = '/static/'

## make Django know that you have created a static folder so now add this line in settings.py file
# ERRORS:?: (staticfiles.E002) The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.
# comment out the STATICFILES_DIRS when using the command collectstatic.py and
# then comment out STATIC_ROOT + remove '#' from STATICFILES_DIRS

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
