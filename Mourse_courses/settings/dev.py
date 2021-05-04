from .base import *

SECRET_KEY = 'q1ui$9l5xtc*q^y!p8bh3egdhxtxn@vm&652mg^yctu4=$+w%t'

ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True

WSGI_APPLICATION = 'home.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
