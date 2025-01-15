from decouple import Csv, config

from .base import *  # noqa F403 F401

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default=[])

SITE_TITLE = "NORA"
DJANGO_ADMIN_SITE_HEADER = "NOvel food Risk Assessment (NORA)"

# to use only https:
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Email settings
MAILGUN_API_KEY = config("MAILGUN_API_KEY", default="")
if MAILGUN_API_KEY:
    INSTALLED_APPS += ["anymail"]  # noqa: F405
    EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
    ANYMAIL = {
        "MAILGUN_API_KEY": MAILGUN_API_KEY,
        "MAILGUN_SENDER_DOMAIN": config("MAILGUN_SENDER_DOMAIN"),
        "MAILGUN_API_URL": config(
            "MAILGUN_API_URL", default="https://api.eu.mailgun.net/v3"
        ),
    }
