from django.contrib import admin

# Register your models here.
from taxonomies.models import (
    GuidelineQualifier,
    Population,
    Subgroup,
    Taxonomy,
    TaxonomyNode,
)


@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = [
        "subgroup",
        "sex",
        "population_age",
        "qualifier",
        "value",
        "upper_range_value",
        "unit",
    ]
    search_fields = ["subgroup__title", "sex__name", "population_age__name"]
    fields = [
        "subgroup",
        "sex",
        "population_age",
        "qualifier",
        "value",
        "upper_range_value",
        "unit",
    ]
    list_filter = [
        "subgroup",
    ]
    autocomplete_fields = ["sex", "population_age", "qualifier", "unit"]


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
