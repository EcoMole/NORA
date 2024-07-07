from django.contrib import admin
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q

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
        (
            "value",
            "upper_range_value",
            "unit",
        ),
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
    search_fields = [
        "code",
        "short_name",
        "extended_name",
        "scientific_names",
        "chem_descriptors",
    ]
    fields = ["code", "short_name", "extended_name", "taxonomy"]
    list_filter = ["taxonomy"]
    actions = [duplicate_model]

    def get_queryset(self, request):
        # annotating TaxnonomyNode queryset with scientific_names and chem_descriptors so
        # that the user can search for TaxonomyNode instance by scientific name or
        # chem descriptor(molecular formula or CAS number), if available.
        return (
            super()
            .get_queryset(request)
            .annotate(
                scientific_names=ArrayAgg(
                    "implicit_attributes__value",
                    filter=Q(implicit_attributes__code="A01"),
                    distinct=True,
                ),
                chem_descriptors=ArrayAgg(
                    "implicit_attributes__value",
                    filter=Q(implicit_attributes__code="CAS")
                    | Q(implicit_attributes__code="MOLECULAR_FORMULA"),
                    distinct=True,
                ),
            )
        )
