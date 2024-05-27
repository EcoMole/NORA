from django.contrib import admin

from allergenicity.models import Allergenicity


@admin.register(Allergenicity)
class AllergenictyAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
    search_fields = ["title"]