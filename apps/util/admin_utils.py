from django.db import transaction


@transaction.atomic
def duplicate_model(modeladmin, request, queryset):
    for object in queryset:
        object.duplicate()


duplicate_model.short_description = "Duplicate selected records"
