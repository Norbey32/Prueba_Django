import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


POSTGRES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crm',
        'USER': 'postgres',
        'PASSWORD': '0987',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}