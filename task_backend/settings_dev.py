import os
from .settings import *

DEBUG = True
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or '1234'
DATABASES = {
        'default':{
            'ENGINE': 'django.bd.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3'
            }
        }
