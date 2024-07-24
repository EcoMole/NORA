from django.contrib import admin

from .models import FreqUsedVocabNode, VocabNodeField


class FieldTitleFilter(admin.SimpleListFilter):
    title = "Field"
    parameter_name = "field__title"

    def lookups(self, request, model_admin):
        return [(field.id, field.title) for field in VocabNodeField.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(field__id=self.value())
        return queryset


@admin.register(FreqUsedVocabNode)
class FreqUsedVocabNodeAdmin(admin.ModelAdmin):
    list_display = ["field", "entity", "node"]
    list_display_links = ["field", "entity", "node"]
    list_filter = [FieldTitleFilter]
    search_fields = [
        "node__short_name",
        "node__extended_name",
        "node__code",
        "entity",
    ]
    autocomplete_fields = ["node"]


@admin.register(VocabNodeField)
class VocabNodeFieldAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = [
        "title",
    ]
