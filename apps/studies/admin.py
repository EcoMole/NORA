from django.contrib import admin

from .models import (
    ADME,
    ADMEStudyType,
    Endpoint,
    Endpointstudy,
    FinalOutcome,
    FinalOutcomePopulation,
    Genotox,
    StudySource,
    StudyType,
)


def duplicate_model(modeladmin, request, queryset):
    for object in queryset:
        # When a Django model instance's id (or primary key) is set to None and then saved,
        # Django recognizes that this is a new record and
        # automatically assigns it a new ID upon saving.
        object.id = None
        object.save()


duplicate_model.short_description = "Duplicate selected records"


class EndpointstudyInline(admin.TabularInline):
    model = Endpointstudy
    extra = 1
    autocomplete_fields = ["novel_food", "testing_method", "test_type"]


class EndpointInline(admin.TabularInline):
    model = Endpoint
    extra = 1
    autocomplete_fields = ["qualifier", "unit"]


class FinalOutcomePopulationInline(admin.TabularInline):
    model = FinalOutcomePopulation
    extra = 1
    autocomplete_fields = ["population"]


class ADMEStudyTypeInline(admin.TabularInline):
    model = ADMEStudyType
    extra = 1
    autocomplete_fields = ["study_type"]


# Main model admin classes


@admin.register(Endpointstudy)
class EndpointstudyAdmin(admin.ModelAdmin):
    list_display = ["novel_food", "testing_method", "test_type", "species", "sex"]
    search_fields = ["novel_food__title", "testing_method__description"]
    autocomplete_fields = [
        "novel_food",
        "testing_method",
        "test_type",
        "species",
        "sex",
        "duration_unit",
        "guideline_qualifier",
        "guideline",
    ]
    inlines = [EndpointInline]
    actions = [duplicate_model]


@admin.register(Endpoint)
class EndpointAdmin(admin.ModelAdmin):
    list_display = [
        "reference_point",
        "endpointstudy",
        "qualifier",
        "lovalue",
        "unit",
    ]
    autocomplete_fields = [
        "reference_point",
        "endpointstudy",
        "qualifier",
        "unit",
    ]


@admin.register(Genotox)
class GenotoxAdmin(admin.ModelAdmin):
    list_display = ["novel_food", "testing_method", "guideline_qualifier"]
    search_fields = ["novel_food__title", "testing_method__description"]
    autocomplete_fields = [
        "novel_food",
        "testing_method",
        "guideline_qualifier",
        "test_type",
        "genotox_guideline",
    ]


@admin.register(ADME)
class ADMEAdmin(admin.ModelAdmin):
    list_display = ["novel_food", "testing_method", "guideline_qualifier", "guideline"]
    autocomplete_fields = [
        "novel_food",
        "testing_method",
        "guideline_qualifier",
        "guideline",
    ]
    search_fields = ["novel_food__title", "testing_method__description"]
    inlines = [ADMEStudyTypeInline]


@admin.register(StudyType)
class StudyTypeAdmin(admin.ModelAdmin):
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
        "outcome",
        "qualifier",
        "value",
        "unit",
        "uncertainty_factor",
    ]
    search_fields = [
        "qualifier__description",
        "value",
    ]
    autocomplete_fields = [
        "outcome",
        "qualifier",
        "unit",
    ]
    inlines = [FinalOutcomePopulationInline]
