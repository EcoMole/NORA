from django.conf import settings
from django.contrib.admin import AdminSite
from django.urls import path

from utils.admin_utils import reorder_models

from .views import test_error_email_reporting


class CustomAdminSite(AdminSite):
    site_header = settings.DJANGO_ADMIN_SITE_HEADER  # default: "Django Administration"
    index_title = "Administration"  # default: "Site administration"
    site_title = settings.SITE_TITLE  # default: "Django site admin"
    # url for link "View site" in the top right corner of Django admin
    site_url = (
        "http://" + settings.FRONTEND_DOMAIN if settings.FRONTEND_DOMAIN else "/"
    )  # default: "/"

    # Override the admin presentation order of the apps and models
    def get_app_list(self, request, app_label=None):
        # Apps are automatically ordered in django admin by
        # order they are registered in INSTALLED_APPS
        # The order of the apps is set here (use the app_label name):
        app_order = [
            "core",
            "administrative",
            "novel_food",
            "composition",
            "studies",
            "taxonomies",
            "extractor",
            "auth",  # Authentication and Authorization
            "account",  # Accounts
            "django_celery_beat",  # Periodic Tasks
            "django_celery_results",  # Celery Results
            "sites",  # Sites
            "authtoken",  # Auth Token
            "socialaccount",  # Social Accounts
        ]

        app_order_dict = dict(zip(app_order, range(len(app_order))))
        app_list = list(self._build_app_dict(request, app_label).values())
        app_list.sort(key=lambda x: app_order_dict.get(x["app_label"], 0))

        # Iterate down the app list and set the presentation order of the models:
        # For models created by yourself, you can set the order of these models simply by
        # ordering them in the admin.py accordingly.
        for app in app_list:
            if app["app_label"] == "django_celery_beat":  # Periodic Tasks
                model_order = [
                    "IntervalSchedule",
                    "CrontabSchedule",
                    "ClockedSchedule",
                    "PeriodicTask",
                    "SolarSchedule",
                ]
                reorder_models(app, model_order)

            elif app["app_label"] == "django_celery_results":  # Celery Results
                model_order = ["TaskResult", "GroupResult"]
                reorder_models(app, model_order)

            elif app["app_label"] == "studies":
                model_order = [
                    "ADME",
                    "Genotox",
                    "Endpointstudy",
                    "Endpoint",
                    "FinalOutcome",
                ]
                reorder_models(app, model_order)

        return app_list

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "test-error/",
                self.admin_view(test_error_email_reporting),
                name="test_error_email_reporting",
            ),
        ]

        return custom_urls + urls
