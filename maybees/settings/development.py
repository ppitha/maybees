# -*- coding: utf-8 -*-
from .base import *

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': get_env_variable ('MAYBEES_DB_HOST'),
        'PORT': '',
        'USER': get_env_variable ('MAYBEES_DB_USER'),
        'NAME': get_env_variable ('MAYBEES_DB_USER'),
        'PASSWORD':  get_env_variable ('MAYBEES_DB_PASSWORD')
    }
}