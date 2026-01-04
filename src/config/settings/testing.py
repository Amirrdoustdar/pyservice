from .base import *  # noqa: F403

DEBUG = False
SECRET_KEY = 'test-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
