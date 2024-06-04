# encoding: utf-8

from django.db import models
from model_utils import Choices


class SyncMixin(models.Model):
    seen_during_synchronization = models.BooleanField(default=False)

    SYNC_STATUS = Choices(
        ("A", "AUTO", "Imported automatically"),
        ("a", "ADDED_MANUALLY", "Added manually"),
        ("r", "REMOVED_MANUALLY", "Removed manually"),
    )
    user_synchronization_status = models.CharField(
        max_length=1, choices=SYNC_STATUS, default=SYNC_STATUS.AUTO
    )

    @classmethod
    def before_synchronization(cls, _filter):
        if _filter:
            cls.objects.filter(_filter).update(seen_during_synchronization=False)
        else:
            cls.objects.all().update(seen_during_synchronization=False)

    @classmethod
    def after_synchronization(cls, remove_unsynchronized, on_delete, _filter):
        obj = cls.objects.all()
        if _filter:
            obj = obj.filter(_filter)

        if remove_unsynchronized:
            if on_delete is None:
                obj.filter(
                    seen_during_synchronization=False,
                    user_synchronization_status=SyncMixin.SYNC_STATUS.AUTO,
                ).delete()
            else:
                for x in obj.filter(
                    seen_during_synchronization=False,
                    user_synchronization_status=SyncMixin.SYNC_STATUS.AUTO,
                ):
                    on_delete(x)

    @classmethod
    def synchronization(cls, remove_unsynchronized, on_delete=None, filter=None):
        return _Sync(cls, remove_unsynchronized, on_delete, filter)

    def mark_not_synchronized(self):
        self.seen_during_synchronization = False

    class Meta:
        abstract = True


class _Sync:
    def __init__(self, cls, remove_unsynchronized, on_delete, filter):
        self.cls = cls
        self.remove_unsynchronized = remove_unsynchronized
        self.on_delete = on_delete
        self.filter = filter

    def __enter__(self):
        self.cls.before_synchronization(self.filter)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cls.after_synchronization(
            self.remove_unsynchronized, self.on_delete, self.filter
        )

    def __getattr__(self, name):
        def method(*args, **kwargs):
            return getattr(self.cls.objects, name)(*args, **kwargs)

        return method

    def get_or_create(self, *args, **kwargs):
        obj, created = self.cls.objects.get_or_create(*args, **kwargs)
        obj.seen_during_synchronization = True
        return obj, created
