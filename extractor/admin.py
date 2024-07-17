from django.contrib import admin

from .models import FreqUsedVocabNode, VocabNodeField


@admin.register(FreqUsedVocabNode)
class FreqUsedVocabNodeAdmin(admin.ModelAdmin):
    list_display = ["field", "entity", "node"]
    list_display_links = ["field", "entity", "node"]
    list_filter = ["field__title"]
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
