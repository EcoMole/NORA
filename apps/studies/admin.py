from django.contrib import admin
from util.admin_utils import duplicate_model

from .models import (
    ADME,
    ADMEInvestigationType,
    Endpoint,
    Endpointstudy,
    FinalOutcome,
    FinalOutcomePopulation,
    Genotox,
    InvestigationType,
    StudySource,
)


class EndpointInline(admin.TabularInline):
    model = Endpoint
    extra = 1
    autocomplete_fields = [
        "qualifier",
        "unit",
        "subpopulation",
        "reference_point",
    ]


class FinalOutcomePopulationInline(admin.TabularInline):
    model = FinalOutcomePopulation
    extra = 1
    autocomplete_fields = ["population"]


class ADMEInvestigationTypeInline(admin.TabularInline):
    model = ADMEInvestigationType
    extra = 1
    autocomplete_fields = ["investigation_type"]


# Main model admin classes


@admin.register(Endpointstudy)
class EndpointstudyAdmin(admin.ModelAdmin):
    list_display = ["get_novel_food", "test_type", "species", "study_source"]
    list_display_links = ["test_type", "species", "study_source"]
    search_fields = [
        "novel_food__title",
        "novel_food__nf_code",
        "test_type__short_name",
        "test_type__extended_name",
        "test_type__code",
        "guideline__short_name",
        "guideline__extended_name",
        "guideline__code",
        "species__short_name",
        "species__extended_name",
        "species__code",
        "study_source__title",
        "remarks",
        "test_material",
    ]
    list_filter = [
        "study_source",
    ]
    autocomplete_fields = [
        "novel_food",
        "test_type",
        "test_type",
        "species",
        "sex",
        "duration_unit",
        "guideline_qualifier",
        "guideline",
    ]
    inlines = [EndpointInline]
    actions = [duplicate_model]

    def get_novel_food(self, obj):
        return str(obj.novel_food)

    get_novel_food.short_description = "Novel Food"


@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    list_display = [
        "get_endpointstudy",
        "reference_point",
        "qualifier",
        "lovalue",
        "unit",
        "subpopulation",
    ]
    list_display_links = [
        "reference_point",
        "qualifier",
        "lovalue",
        "unit",
        "subpopulation",
    ]
    search_fields = [
        "endpointstudy__novel_food__title",
        "endpointstudy__novel_food__nf_code",
        "endpointstudy__test_type__short_name",
        "endpointstudy__test_type__extended_name",
        "endpointstudy__test_type__code",
        "endpointstudy__species__short_name",
        "endpointstudy__species__extended_name",
        "endpointstudy__species__code",
        "reference_point__short_name",
        "reference_point__extended_name",
        "reference_point__code",
        "lovalue",
        "subpopulation__short_name",
        "subpopulation__extended_name",
        "subpopulation__code",
    ]
    autocomplete_fields = [
        "reference_point",
        "endpointstudy",
        "qualifier",
        "unit",
        "subpopulation",
    ]
    actions = [duplicate_model]

    def get_endpointstudy(self, obj):
        return str(obj.endpointstudy)

    get_endpointstudy.short_description = "Endpoint Study"


@admin.register(Genotox)
class GenotoxAdmin(admin.ModelAdmin):
    list_display = ["get_novel_food", "test_type", "study_source", "guideline"]
    list_display_links = ["test_type", "study_source", "guideline"]
    search_fields = [
        "novel_food__title",
        "novel_food__nf_code",
        "guideline__short_name",
        "guideline__extended_name",
        "guideline__code",
        "test_type__short_name",
        "test_type__extended_name",
        "test_type__code",
        "test_material",
        "remarks",
    ]
    list_filter = ["outcome", "study_source"]

    autocomplete_fields = [
        "novel_food",
        "test_type",
        "guideline_qualifier",
        "test_type",
        "guideline",
    ]
    actions = [duplicate_model]

    def get_novel_food(self, obj):
        return str(obj.novel_food)

    get_novel_food.short_description = "Novel Food"


@admin.register(ADME)
class ADMEAdmin(admin.ModelAdmin):
    list_display = [
        "get_novel_food",
        "test_type",
        "study_source",
        "investigation_types",
    ]
    list_display_links = ["test_type", "study_source", "investigation_types"]
    search_fields = [
        "novel_food__title",
        "novel_food__nf_code",
        "test_type__short_name",
        "test_type__extended_name",
        "test_type__code",
        "guideline__short_name",
        "guideline__extended_name",
        "guideline__code",
        "test_material",
        "remarks",
    ]
    list_filter = [
        "study_source",
    ]
    autocomplete_fields = [
        "novel_food",
        "test_type",
        "guideline",
        "guideline_qualifier",
    ]
    inlines = [ADMEInvestigationTypeInline]
    actions = [duplicate_model]

    def investigation_types(self, obj):
        investigation_types = ADMEInvestigationType.objects.filter(adme=obj)
        types = [i.investigation_type.title for i in investigation_types]
        return ", ".join(types)

    investigation_types.short_description = "Investigation Type"

    def get_novel_food(self, obj):
        return str(obj.novel_food)

    get_novel_food.short_description = "Novel Food"


@admin.register(InvestigationType)
class InvestigationTypeAdmin(admin.ModelAdmin):
    search_fields = ["title"]

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(StudySource)
class StudySourceAdmin(admin.ModelAdmin):
    search_fields = ["title"]

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(FinalOutcome)
class FinalOutcomeAdmin(admin.ModelAdmin):
    list_display = [
        "get_endpointstudy",
        "get_endpoint",
        "get_outcome",
        "qualifier",
        "value",
        "unit",
        "uncertainity_factor",
    ]
    list_display_links = [
        "get_outcome",
        "qualifier",
        "value",
        "unit",
        "uncertainity_factor",
    ]

    search_fields = [
        "endpoint__endpointstudy__novel_food__title",
        "endpoint__endpointstudy__novel_food__nf_code",
        "endpoint__endpointstudy__test_type__short_name",
        "endpoint__endpointstudy__test_type__extended_name",
        "endpoint__endpointstudy__test_type__code",
        "endpoint__endpointstudy__species__short_name",
        "endpoint__endpointstudy__species__extended_name",
        "endpoint__endpointstudy__species__code",
        "endpoint__reference_point__short_name",
        "endpoint__reference_point__extended_name",
        "endpoint__reference_point__code",
        "endpoint__subpopulation__short_name",
        "endpoint__subpopulation__extended_name",
        "endpoint__subpopulation__code",
        "outcome__short_name",
        "outcome__extended_name",
        "outcome__code",
        "value",
        "uncertainity_factor",
        "remarks",
    ]
    autocomplete_fields = ["outcome", "qualifier", "unit", "endpoint"]
    inlines = [FinalOutcomePopulationInline]
    actions = [duplicate_model]

    def get_endpointstudy(self, obj):
        return str(obj.endpoint.endpointstudy)

    get_endpointstudy.short_description = "Endpoint Study"

    def get_endpoint(self, obj):
        reference_point_part = (
            obj.endpoint.reference_point.name if obj.endpoint.reference_point else ""
        )
        qualifier_part = (
            f" {obj.endpoint.qualifier.name}" if obj.endpoint.qualifier else ""
        )
        lovalue_part = f" {obj.endpoint.lovalue}" if obj.endpoint.lovalue else ""
        unit_part = f" {obj.endpoint.unit}" if obj.endpoint.unit else ""
        subpopulation_part = (
            f" {obj.endpoint.subpopulation.name}" if obj.endpoint.subpopulation else ""
        )
        return (
            reference_point_part
            + qualifier_part
            + lovalue_part
            + unit_part
            + subpopulation_part
        )

    get_endpoint.short_description = "Endpoint"

    def get_outcome(self, obj):
        return str(obj.outcome)

    get_outcome.short_description = "Outcome"
