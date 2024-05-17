"""
Django settings for nora project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import sys
from datetime import timedelta
from pathlib import Path

from celery.schedules import crontab
from decouple import Csv, config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR / "apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool, default=False)

# reassigned in devel settings, where it is needed for reset password email
FRONTEND_DOMAIN = ""


ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default=[])

# ADMINS - technical personel responsible for running the application
# - receives technical notifications via mail_admins()
# MANAGER - non-technical personel responsible for running the application
# - receives non-technical notifications via mail_managers()
ADMINS = config(
    "ADMINS", cast=Csv(cast=Csv(post_process=tuple), delimiter=";"), default=""
)
MANAGERS = config(
    "MANAGERS", cast=Csv(cast=Csv(post_process=tuple), delimiter=";"), default=""
)

AUTH_USER_MODEL = "core.User"
DJANGO_ADMIN_PATH = config("DJANGO_ADMIN_PATH", default="admin/")

# Application definition

INSTALLED_APPS = [
    # Custom apps
    "core.apps.CoreConfig",  # contains the custom user model
    "admin.apps.CustomAdminConfig",
    "api.apps.ApiConfig",
    "authentication.apps.AuthenticationConfig",
    "administrative.apps.AdministrativeConfig",
    # Django's built-in apps
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party apps
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",  # this is django-allauth
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework_simplejwt",
    "django_celery_results",
    "django_celery_beat",
    "import_export",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        # if the above is used, then the user must be authenticated to
        # access any endpoint which means even for the registration endpoint.?
        # use for those endpoints:
        # permission_classes = [AllowAny]
    ],
}

AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
)


# DJANGO-ALLAUTH
# email should be used for authentication instead of the username
ACCOUNT_AUTHENTICATION_METHOD = "email"
# e-mail address must be provided by the user in order to register
ACCOUNT_EMAIL_REQUIRED = True
# to ensure mandatory verification by email for the user to complete the registration process
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# to allow the website to verify the user when the user opens the link received in the email
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# then we want the user to be redirected to the LOGIN_URL after verification,
# so we specified our LOGIN_URL:
LOGIN_URL = "https://localhost:5173/"
# ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
# needed for custom email templates (password reset email etc.)
ACCOUNT_ADAPTER = "authentication.account.CustomAccountAdapter"


# DJ-REST-AUTH
REST_AUTH = {
    # so that the POST request to create new user returns 201 with token and not only 204
    "SESSION_LOGIN": False,
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "access-token",
    "JWT_AUTH_REFRESH_COOKIE": "refresh-token",
    "JWT_AUTH_COOKIE_USE_CSRF": True,
    # thanks to the line bellow all API endpoints of the app
    # (even those public ones without authorization) require CSRF token
    "JWT_AUTH_COOKIE_ENFORCE_CSRF_ON_UNAUTHENTICATED": True,
    "REST_USE_JWT": True,
    "REST_SESSION_LOGIN": False,
    # if True, `old_password` is required in password change post request
    "OLD_PASSWORD_FIELD_ENABLED": True,
    # if True, user is logged out after password change
    "LOGOUT_ON_PASSWORD_CHANGE": False,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=5),
    "AUTH_HEADER_TYPES": (
        # this is whats will be prepended to the token itself
        "Bearer",
    ),
}

# The number of seconds a password reset link is valid for.
PASSWORD_RESET_TIMEOUT = config(
    "PASSWORD_RESET_TIMEOUT", cast=int, default=259200
)  # 3 days


ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        # will look into root/app1/templates and root/app2/templates directories for templates.
        # I use root/app1/templates/app1 so I can use a template.html as 'app1/template.html'
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": config("DB_NAME", default=""),
        "USER": config("DB_USER", default=""),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", cast=int, default=5432),
        "ATOMIC_REQUESTS": True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Email
ADMINS = config(
    "ADMINS", cast=Csv(cast=Csv(post_process=tuple), delimiter=";"), default=""
)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = config("EMAIL_HOST", default="localhost")
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
EMAIL_PORT = config("EMAIL_PORT", default="")
EMAIL_SUBJECT_PREFIX = config("EMAIL_SUBJECT_PREFIX", default="")
# email address that Django uses for
# sending error messages or internal notifications to administrators
SERVER_EMAIL = config(
    "SERVER_EMAIL",
    default="Notifications from My Localhost <notifications@mylocalhost.com>",
)
# email address that Django uses for sending messages to users and is public facing
DEFAULT_FROM_EMAIL = config(
    "DEFAULT_FROM_EMAIL", default="My Localhost <noreply@mylocalhost.com>"
)


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Prague"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# In a production environment, you need to tell your web server (e.g., Nginx or Apache) to
# serve the static files stored in the `STATIC_ROOT` directory when requests are made to
# URLs that match the `STATIC_URL` prefix.

# base URL (URL prefix) used to refer to static files
STATIC_URL = "/static/"

# `collectstatic`` copies all static files from your apps and any other
# directories specified in `STATICFILES_DIRS` into the `STATIC_ROOT` directory
STATIC_ROOT = config("STATIC_ROOT", default=BASE_DIR / "static_compiled")

MEDIA_URL = "/media/"
MEDIA_ROOT = config("MEDIA_ROOT", default=str(BASE_DIR / "media/"))

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# represents the unique identifier for the current site in a multi-site setup
SITE_ID = 1


# Celery
CELERY_BROKER_URL = "amqp://localhost"
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "django-cache"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_DEFAULT_QUEUE = "celery"
CELERY_TASK_ROUTES = {
    "core.tasks.delete_notverified_email_users": {"queue": "celery"},
}

CELERY_BEAT_SCHEDULE = {
    # crontab schedules - tasks performed once a day
    "delete_notverified_email_users": {
        "task": "core.tasks.delete_notverified_email_users",
        "schedule": crontab(hour=23, minute=0),  # every day at 23:00
        "options": {"expires": 24 * 60 * 60},
    }
}

# Users settings

PERIOD_TO_VERIFY_EMAIL = timedelta(days=30)