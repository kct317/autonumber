"""
Django development settings for autonumber project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ixay2#6e6mnfx7c86w)%nf&)xy275-+o%_95!sukzd%yj9!8@g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


#python manage.py createcachetable mycache
#进入mysql 可以看到一个新的数据库 mycache
CACHE_BACKEND = 'db://mycache'
#CACHE_BACKEND = 'file:// /tmp/django/cache'
#CACHE_BACKEND = 'memcache://127.0.0.1:12111'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
	'app.autonumber',  #app
    'app.templatetags',    #模板tags

    'bootstrap_toolkit',
]

#中间件
"""
    __init__
    process_request
    process_view
    process_response
    process_exception
"""
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware', #使用会话
    'django.middleware.common.CommonMiddleware', #
    'django.middleware.csrf.CsrfViewMiddleware', #防止csrf攻击
    'django.contrib.auth.middleware.AuthenticationMiddleware', #认证
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    #'django.middleware.http.SetRemoteAddrFromForwardedFor',

]

ROOT_URLCONF = 'pjsite.urls'

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

#TEMPLATE_DIRS

WSGI_APPLICATION = 'pjsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    #  mysql
    'default': {
        'ENGINE': 'django.db.backends.mysql', #数据库引擎
        'NAME': 'autonumber',                 #数据库名
        'USER': 'root',                       #用户名
        'PASSWORD': 'donotuseroot!@#123',  #密码
        'HOST': '127.0.0.1',                  #数据库主机 默认为localhost
        'PORT': 3306,                         #数据库端口 MySQL默认为3306
    }
}
'''
    #  sqlite3
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'app'), 'db.sqlite3'),
    }
'''
'''
MIGRATION_MODULES = {
    'autonumber': 'app.autonumber.migrations',
}
'''


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'zh-hans'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT,'css')),
    ("js", os.path.join(STATIC_ROOT,'js')),
    ("fonts", os.path.join(STATIC_ROOT,'fonts')),
    ("images", os.path.join(STATIC_ROOT,'img')),
    STATIC_URL
)
