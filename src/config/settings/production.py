from .base import *  # noqa: F403
import os

DEBUG = False
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
