from django.contrib import admin

# Register your models here.
from taxonomies.models import (
    GuidelineQualifier,
    Population,
    Subgroup,
    Taxonomy,
    TaxonomyNode,
)
from util.admin_utils import duplicate_model


@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = [
        "subgroup",
        "qualifier",
        "value",
        "upper_range_value",
        "unit",
    ]
    search_fields = [
        "subgroup__title",
    ]
    fields = [
        "subgroup",
        "qualifier",
        "value",
        "upper_range_value",
        "unit",
    ]
    list_filter = [
        "subgroup",
    ]
    autocomplete_fields = ["qualifier", "unit"]
    actions = [duplicate_model]


@admin.register(GuidelineQualifier)
class GuidelineQualifierAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
    search_fields = [
        "title",
    ]


@admin.register(Subgroup)
class SubgroupAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    fields = ["title"]


@admin.register(Taxonomy)
class TaxonomyAdmin(admin.ModelAdmin):
    search_fields = ["code"]


@admin.register(TaxonomyNode)
class TaxonomyNodeAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "taxonomy"]
    search_fields = ["code", "short_name", "extended_name"]
    fields = ["code", "short_name", "extended_name", "taxonomy"]
    list_filter = ["taxonomy"]
    actions = [duplicate_model]
