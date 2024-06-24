def duplicate_model(modeladmin, request, queryset):
    for object in queryset:
        # When a Django model instance's id (or primary key) is set to None and then saved,
        # Django recognizes that this is a new record and
        # automatically assigns it a new ID upon saving.
        object.id = None
        object.save()


duplicate_model.short_description = "Duplicate selected records"
