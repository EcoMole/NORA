from allauth.account.admin import EmailAddressAdmin as BaseEmailAddressAdmin
from allauth.account.models import EmailAddress
from core import models
from django.contrib import admin  # noqa: F401
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from import_export import fields
from import_export.admin import ExportActionMixin
from import_export.resources import ModelResource

from .forms import CustomEmailAddressAdminForm
from .models import Contribution, User


class UserResource(ModelResource):
    """
    This is used by django-import-export to facilitate CSV export in Django admin
    """

    email_verified = fields.Field()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "last_login",
            "is_active",
            "is_staff",
        )
        export_order = fields

    def dehydrate_email_verified(self, user):
        return user._email_verified


class HasEmailVerified(admin.SimpleListFilter):
    title = "has verified email"
    parameter_name = "email_verified"

    def lookups(self, request, model_admin):
        return (("Yes", "Yes"), ("No", "No"))

    def queryset(self, request, queryset):
        if self.value() == "Yes":
            return queryset.filter(_email_verified=True)
        if self.value() == "No":
            return queryset.filter(_email_verified=False)


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ("get_opinion", "user", "status", "remarks")
    list_filter = ("status", "user")
    search_fields = ("opinion__title", "remarks")
    autocomplete_fields = ("opinion", "user")

    def get_opinion(self, obj):
        """displays the opinion title in multiple lines if the title is too long"""
        return obj.opinion.title

    get_opinion.short_description = "Opinion"
    get_opinion.admin_order_field = "opinion__title"


@admin.register(models.User)
class TheUserAdmin(ExportActionMixin, UserAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "get_groups",
        "is_superuser",
        "is_staff",
        "email_verified",
    ]

    list_filter = (HasEmailVerified,) + UserAdmin.list_filter

    resource_class = UserResource  # for django-import-export

    def get_groups(self, obj):
        return format_html("<br>".join([group.name for group in obj.groups.all()]))

    get_groups.short_description = "Groups"
    get_groups.admin_order_field = "groups__name"

    def get_queryset(self, request):
        return User.objects.annotate_email_verified()

    def email_verified(self, user):
        return user.email_verified

    email_verified.boolean = True
    email_verified.admin_order_field = "_email_verified"


class CustomEmailAddressAdmin(BaseEmailAddressAdmin):
    form = CustomEmailAddressAdminForm


admin.site.unregister(EmailAddress)
admin.site.register(EmailAddress, CustomEmailAddressAdmin)
