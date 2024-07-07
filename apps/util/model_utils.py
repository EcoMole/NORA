from django.core.exceptions import ValidationError


def handle_unique_true_fields(obj):
    # Iterate over all fields in the model class
    for field in obj._meta.get_fields():
        # Check if the field has the attribute 'unique' set to True
        if getattr(field, "unique", False) and field.name != "id":
            field_value = field.value_from_object(obj)
            if type(field_value) == str:
                if obj.__class__.objects.filter(
                    **{field.name: "DUPLICATE_" + field_value}
                ).exists():
                    raise ValidationError(
                        f"Cannt duplicate because the field '{field.name}' is "
                        "unique=True and there is already an instance with "
                        f"{field.name}=DUPLICATE_{field_value} in the database."
                    )
                else:
                    setattr(obj, field.name, "DUPLICATE_" + field_value)
            else:
                raise ValidationError(
                    f"Cannt duplicate bacause the field {field.name} is not string type."
                )


def duplicate_related_objects(copied_object, copy_object):
    if hasattr(copied_object, "duplicate_related"):
        for related_name in copied_object.duplicate_related:
            related_manager = getattr(copied_object, related_name)
            for related_object in related_manager.all():
                copied_obj = related_object.__class__.objects.get(pk=related_object.pk)
                related_object.id = None
                handle_unique_true_fields(related_object)
                # Find the correct ForeignKey field dynamically
                fk_field = None
                for field in related_object._meta.get_fields():
                    if (
                        field.is_relation
                        and field.many_to_one
                        and field.related_model == copied_object.__class__
                    ):
                        fk_field = field.name
                        break
                if fk_field:
                    setattr(related_object, fk_field, copy_object)
                    related_object.save()
                    copy_obj = related_object.__class__.objects.get(
                        pk=related_object.pk
                    )
                    duplicate_related_objects(copied_obj, copy_obj)


class DuplicateRelatedMixin:
    duplicate_related = []

    def duplicate(self):
        copied_object = self.__class__.objects.get(pk=self.pk)
        self.id = None
        handle_unique_true_fields(self)
        self.save()
        copy_object = self.__class__.objects.get(pk=self.pk)
        duplicate_related_objects(copied_object, copy_object)
