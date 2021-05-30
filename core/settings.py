"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from decouple import config

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',

    'account',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

gettext = lambda s: s

EXTRA_LANG_INFO = {
    'ky': {
        'bidi': False, # right-to-left
        'code': 'ky',
        'name': 'Kyrgyz',
        'name_local': 'Кыргыз тили', #unicode codepoints here
    },
    'ug': {
        'bidi': False, # right-to-left
        'code': 'ug',
        'name': 'Uighur',
        'name_local': 'Uygurçi', #unicode codepoints here
    },
    'ba': {
        'bidi': False, # right-to-left
        'code': 'ba',
        'name': 'Bashkir',
        'name_local': 'Bashkir', #unicode codepoints here
    },
    'cv': {
        'bidi': False, # right-to-left
        'code': 'cv',
        'name': 'Chuvash',
        'name_local': 'Chuvash', #unicode codepoints here
    },
    'kaa': {
        'bidi': False, # right-to-left
        'code': 'kaa',
        'name': 'Kara-Kalpak',
        'name_local': 'Kara-Kalpak', #unicode codepoints here
    },
    'krc': {
        'bidi': False, # right-to-left
        'code': 'krc',
        'name': 'Karachay-Balkar',
        'name_local': 'Karachay-Balkar', #unicode codepoints here
    },
    'sah': {
        'bidi': False, # right-to-left
        'code': 'sah',
        'name': 'Yakut',
        'name_local': 'Yakut', #unicode codepoints here
    },
    'alt': {
        'bidi': False, # right-to-left
        'code': 'alt',
        'name': 'Altaic',
        'name_local': 'Altaic', #unicode codepoints here
    },
    'ash': {
        'bidi': False, # right-to-left
        'code': 'ash',
        'name': 'Avshar',
        'name_local': 'Avshar', #unicode codepoints here
    },
    'ctt': {
        'bidi': False, # right-to-left
        'code': 'ctt',
        'name': 'Crimean-Tatar',
        'name_local': 'Кырым татар теле', #unicode codepoints here
    },
    'ksk': {
        'bidi': False, # right-to-left
        'code': 'ksk',
        'name': 'Kashkay',
        'name_local': 'Kashkay', #unicode codepoints here
    },
    'uz': {
        'bidi': False, # right-to-left
        'code': 'uz',
        'name': 'Uzbek',
        'name_local': "O'zbek tili", #unicode codepoints here
    },
    'tk': {
        'bidi': False,  # right-to-left
        'code': 'tk',
        'name': 'Turkmen',
        'name_local': 'Türkmen dili',  # unicode codepoints here
    },
}

import django.conf.locale
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO


LANGUAGES = (
    ('tr', gettext('Turkish')),
    ('az', gettext('Azeri')),
    ('uz', gettext('Uzbek')),
    ('kk', gettext('Kazakh')),
    ('ug', gettext('Uighur')),
    ('tk', gettext('Turkmen')),
    ('tt', gettext('Tatar')),
    ('ky', gettext('Kyrgyz')),
    ('ksk', gettext('Kashkay')),
    ('ba', gettext('Bashkir')),
    ('cv', gettext('Chuvash')),
    ('ash', gettext('Avshar')),
    ('kaa', gettext('Kara-Kalpak')),
    ('krc', gettext('Karachay-Balkar')),
    ('sah', gettext('Yakut')),
    ('ctt', gettext('Crimean-Tatar')),
    ('alt', gettext('Altaic')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'tr'

MODELTRANSLATION_TRANSLATION_FILES = (
    'app.translation',
)


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

AUTH_USER_MODEL = 'account.MyUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_COMPACT = True
JET_CHANGE_FORM_SIBLING_LINKS = True
JET_INDEX_DASHBOARD  = 'jet.dashboard.dashboard.DefaultIndexDashboard'
JET_APP_INDEX_DASHBOARD  = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'

