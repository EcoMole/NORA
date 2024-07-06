def duplicate_related_objects(copied_object, copy_object):
    if hasattr(copied_object, "duplicate_related"):
        for related_name in copied_object.duplicate_related:
            related_manager = getattr(copied_object, related_name)
            for related_object in related_manager.all():
                copied_obj = related_object.__class__.objects.get(pk=related_object.pk)
                related_object.id = None
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
        self.save()
        copy_object = self.__class__.objects.get(pk=self.pk)
        duplicate_related_objects(copied_object, copy_object)
