"""
Django settings for studingsite project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

from django.conf.global_settings import STATICFILES_DIRS, MEDIA_ROOT, MEDIA_URL, LOGIN_REDIRECT_URL, \
    LOGOUT_REDIRECT_URL, AUTHENTICATION_BACKENDS, EMAIL_BACKEND, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT, \
    EMAIL_HOST_USER, EMAIL_USE_SSL, DEFAULT_FROM_EMAIL, SERVER_EMAIL, AUTH_USER_MODEL, CACHE_MIDDLEWARE_ALIAS, \
    CACHE_MIDDLEWARE_SECONDS, CACHE_MIDDLEWARE_KEY_PREFIX

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u=b_*pxsm6+2zmi98g0rp$*o2f(p61(%%e!z!2@k&zvw6z_@(r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'sitewomen.ru']

INTERNAL_IPS = [
    "127.0.0.1"
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'women.apps.WomenConfig',
    'users',
    'social_django',
    'debug_toolbar',
    'captcha',
    'django.contrib.sites',
    'django.contrib.sitemaps'
]



MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
#    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
#    "django.middleware.cache.FetchFromCacheMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CACHE_MIDDLEWARE_ALIAS = 'default'
# CACHE_MIDDLEWARE_SECONDS = 10
# CACHE_MIDDLEWARE_KEY_PREFIX = 'sitewomen'


ROOT_URLCONF = 'studingsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.get_women_context'
            ],
        },
    },
]

WSGI_APPLICATION = 'studingsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sitewomen_db',
        'USER': 'sitewomen',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

CACHES = {
    "default": {
         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#        "BACKEND": "django.core.cache.backends.redis.RedisCache",
#        "LOCATION": "redis://127.0.0.1:6379",
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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'users:login'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'users.authentication.EmailAuthBackend'
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'mikemalyshkin@yandex.ru'
# EMAIL_HOST_PASSWORD = 'pcissqigfkaajkqf'
# EMAIL_USE_SSL = True
#
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# SERVER_EMAIL = EMAIL_HOST_USER
# EMAIL_ADMIN = EMAIL_HOST_USER

AUTH_USER_MODEL = 'users.User'
DEFAULT_USER_IMAGE = MEDIA_URL + 'users/default.png'

SOCIAL_AUTH_GITHUB_KEY = 'Ov23liIc9K1IIsRhPdZ8'
SOCIAL_AUTH_GITHUB_SECRET = 'df3186463902f0c821935f965d473529773265ea'
SOCIAL_AUTH_VK_OAUTH2_KEY = '52967723'
SOCIAL_AUTH_VK_OAUTH2_SECRET = '9GAvx3goclkgKlZkdITL'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'users.pipeline.new_users_handler',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SITE_ID = 1