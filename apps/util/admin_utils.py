from django.core.exceptions import ValidationError
from django.db import transaction


@transaction.atomic
def duplicate_model(modeladmin, request, queryset):
    """
    Duplicates selected records along with their related objects.
    """

    def handle_unique_true_fields(obj):
        """
        This method will prepend "DUPLICATE_" to the values of fields which have
        unique=True to avoid unique constraint violations.
        This method is used on the newly created duplicate, represented as parameter `obj`.
        """
        for field in obj._meta.get_fields():
            if (
                getattr(field, "unique", False) and field.name != "id"
            ):  # Ignore 'id' field
                field_value = field.value_from_object(obj)
                if not isinstance(field_value, str):
                    raise ValidationError(
                        f"Cannot duplicate because the field {field.name} is not string type."
                    )
                duplicated_value = f"DUPLICATE_{field_value}"
                if obj.__class__.objects.filter(
                    **{field.name: duplicated_value}
                ).exists():
                    raise ValidationError(
                        f"Cannot duplicate because the field '{field.name}' is "
                        "unique=True and there is already an instance with "
                        f"{field.name}={duplicated_value} in the database."
                    )
                setattr(obj, field.name, duplicated_value)

    def duplicate_related_objects(original_obj, duplicated_obj):
        """
        Duplicates the related objects of original_obj and links
        these duplicated related objects to the duplicated_obj.
        """
        if not hasattr(original_obj, "duplicate_related"):
            return

        if not isinstance(original_obj.duplicate_related, (list, tuple, set)):
            raise ValidationError(
                "Model attribute duplicate_related has to be of type list, tuple, or set."
            )

        for related_name in original_obj.duplicate_related:
            related_manager = getattr(original_obj, related_name)
            for related_obj in related_manager.all():
                original_related_obj = related_obj.__class__.objects.get(
                    pk=related_obj.pk
                )
                related_obj.id = None  # Reset ID to None to create a new instance
                for field in related_obj._meta.get_fields():
                    if (
                        field.many_to_one
                        and field.related_model == original_obj.__class__
                        and getattr(related_obj, field.name).pk == original_obj.pk
                    ):
                        setattr(related_obj, field.name, duplicated_obj)
                        handle_unique_true_fields(related_obj)
                        related_obj.save()  # Save the duplicated related object
                        duplicated_related_obj = related_obj.__class__.objects.get(
                            pk=related_obj.pk
                        )
                        # Recursively duplicate related objects
                        duplicate_related_objects(
                            original_related_obj, duplicated_related_obj
                        )

    for obj in queryset:
        # Re-fetch the original object to keep distinct object in
        # original_object and in the duplicated_object
        original_obj = obj.__class__.objects.get(pk=obj.pk)
        obj.id = None
        # following modifications is being made to what will become the
        # duplicated object, not the already-existing original_object in the database.
        handle_unique_true_fields(obj)
        # self.save() will make the self instance a new record in the database, because django
        # treats saving object with id=None as a creating of a new object rather than
        # updating an object
        obj.save()
        # obj represents the duplicated object now
        duplicated_obj = obj.__class__.objects.get(pk=obj.pk)
        duplicate_related_objects(original_obj, duplicated_obj)


duplicate_model.short_description = "Duplicate selected records"
