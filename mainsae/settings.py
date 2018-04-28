"""
Django settings for mainsae project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f+p!f5iw*60(9)!4)25kym#ac)1w@wps3dl%wjnjgh!f=2h095'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['2403ae27.ngrok.io','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainserver',
    'rest_framework',
    # 'paytm',
    'rest_framework.authtoken',
]

# ASGI_APPLICATION = "mainsae.routing.application"

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'asgi_redis.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [('localhost', 6379)],
#         },
#         'ROUTING': 'mainsae.routing.channel_routing',
#     }
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mainsae.urls'

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
      'rest_framework.authentication.TokenAuthentication',
    )
}

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

WSGI_APPLICATION = 'mainsae.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# https://github.com/harishbisht/paytm
PAYTM_MERCHANT_COMPANY_NAME = "<YOUR-COMPANY-NAME>"
PAYTM_CHANNEL_ID = "WEB"
PAYTM_EMAIL  = "<YOUR-EMAIL-ID>"
PAYTM_MOBILE = "<YOUR-MOBILE-NUMBER>"
PAYTM_STAGING = True
if PAYTM_STAGING:
    PAYTM_MERCHANT_KEY = "bKMfNxPPf_QdZppa"
    PAYTM_INDUSTRY_TYPE_ID = "Retail"
    PAYTM_MERCHANT_ID = "DIY12386817555501617"
    PAYTM_CALLBACK_URL = "http://localhost:8000/wallet/response/" if DEBUG else "http://www.yourwebsite.com/wallet/response/"
    PAYTM_WEBSITE = "DIYtestingweb"
    PAYTM_TRANSACTION_STATUS_URL = "https://pguat.paytm.com/oltp/HANDLER_INTERNAL/TXNSTATUS"
    PAYTM_PAYMENT_GATEWAY_URL = "https://pguat.paytm.com/oltp-web/processTransaction"
else:
    PAYTM_MERCHANT_KEY = "<YOUR-LIVE-MERCHANT-KEY>"
    PAYTM_MERCHANT_ID = "<YOUR-LIVE-MERCHANT-ID>"
    PAYTM_CALLBACK_URL = "<YOUR-LIVE-CALLBACK-URL>"
    PAYTM_INDUSTRY_TYPE_ID = "Retail92"
    PAYTM_WEBSITE = "<PAYTM-WEBSITE-ID>"
    PAYTM_TRANSACTION_STATUS_URL = "https://secure.paytm.in/oltp/HANDLER_INTERNAL/TXNSTATUS"
    PAYTM_PAYMENT_GATEWAY_URL = "https://secure.paytm.in/oltp-web/processTransaction"

