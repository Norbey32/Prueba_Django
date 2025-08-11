import os
from pathlib import Path
import app.base_datos as crm

BASE_DIR = Path(__file__).resolve().parent.parent


SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crm',
        'USER': 'postgres',
        'PASSWORD': '0987',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}