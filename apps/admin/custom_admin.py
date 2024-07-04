from django.conf import settings
from django.contrib.admin import AdminSite


class CustomAdminSite(AdminSite):
    site_header = (
        "NOvel food Risk Assessment (NORA)"  # default: "Django Administration"
    )
    index_title = "Administration"  # default: "Site administration"
    site_title = "NORA"  # default: "Django site admin"
    # url for link "View site" in the top right corner of Django admin
    site_url = (
        "https://" + settings.FRONTEND_DOMAIN if settings.FRONTEND_DOMAIN else "/"
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
            "auth",  # Authentication and Authorization
            "account",  # Accounts
            "django_celery_beat",  # Periodic Tasks
            "django_celery_results",  # Celery Results
            "sites",  # Sites
            "authtoken",  # Auth Token
            "socialaccount",  # Social Accounts
            "extractor",
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
                    "Intervals",
                    "Crontabs",
                    "Clocked",
                    "Periodic tasks",
                    "Solar events",
                ]
                model_order_dict = dict(zip(model_order, range(len(model_order))))
                app["models"].sort(key=lambda x: model_order_dict.get(x["name"], 0))

            elif app["app_label"] == "django_celery_results":  # Celery Results
                model_order = [
                    "Task results",
                    "Group results",
                ]
                model_order_dict = dict(zip(model_order, range(len(model_order))))
                app["models"].sort(key=lambda x: model_order_dict.get(x["name"], 0))

        return app_list
