from decouple import Csv, config

from .base import *  # noqa F403 F401

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default=[])

SITE_TITLE = "NORA"
DJANGO_ADMIN_SITE_HEADER = "NOvel food Risk Assessment (NORA)"

# to use only https:
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
