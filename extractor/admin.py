from django.contrib import admin

from .models import FreqUsedVocabNode


@admin.register(FreqUsedVocabNode)
class FreqUsedVocabNodeAdmin(admin.ModelAdmin):
    list_display = ["node", "field", "remarks"]
    list_display_links = ["node", "field", "remarks"]
    list_filter = ["field"]
    search_fields = [
        "node__name",
        "node__code",
        "remarks",
    ]
    autocomplete_fields = ["node"]
