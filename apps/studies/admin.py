from django.contrib import admin

from .models import (
    ADME,
    ADMEStudyType,
    Assessment,
    EndEndstudyOutcome,
    EndpointStudy,
    Genotox,
    GenotoxOutcome,
    Outcome,
    OutcomePopulation,
    SpecificToxicityStudy,
    StudySource,
    StudyType,
)

# Inline Admin Classes for managing relationships directly from the main model's admin interface


class EndpointStudyInline(admin.TabularInline):
    model = EndpointStudy
    extra = 1
    autocomplete_fields = ["novel_food", "testing_method", "test_type"]


class EndEndstudyOutcomeInline(admin.TabularInline):
    model = EndEndstudyOutcome
    extra = 1
    autocomplete_fields = ["qualifier", "unit", "sex"]


class OutcomeInline(admin.TabularInline):
    model = Outcome
    extra = 1
    autocomplete_fields = ["assessment_type", "risk_qualifier", "unit"]


class OutcomePopulationInline(admin.TabularInline):
    model = OutcomePopulation
    extra = 1
    autocomplete_fields = ["population"]


class ADMEStudyTypeInline(admin.TabularInline):
    model = ADMEStudyType
    extra = 1
    autocomplete_fields = ["study_type"]


class SpecificToxicityStudyInline(admin.TabularInline):
    model = SpecificToxicityStudy
    extra = 1
    autocomplete_fields = ["id_spec_tox"]


# Main model admin classes


@admin.register(EndpointStudy)
class EndpointStudyAdmin(admin.ModelAdmin):
    list_display = ["novel_food", "testing_method", "test_type", "species", "sex"]
    search_fields = ["novel_food__title", "testing_method__description"]
    autocomplete_fields = [
        "novel_food",
        "testing_method",
        "test_type",
        "species",
        "sex",
    ]
    inlines = [EndEndstudyOutcomeInline, SpecificToxicityStudyInline]


@admin.register(EndEndstudyOutcome)
class EndEndstudyOutcomeAdmin(admin.ModelAdmin):
    list_display = ["endpointstudy", "qualifier", "lovalue", "unit", "sex"]
    autocomplete_fields = ["endpointstudy", "qualifier", "unit", "sex"]


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


@admin.register(GenotoxOutcome)
class GenotoxOutcomeAdmin(admin.ModelAdmin):
    list_display = ["id_tox", "hazard"]
    autocomplete_fields = ["id_tox", "hazard"]


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


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ["assessment", "risk_qualifier", "value", "unit", "safety_factor"]
    search_fields = ["assessment__title", "risk_qualifier__description", "value"]
    autocomplete_fields = ["assessment", "assessment_type", "risk_qualifier", "unit"]
    inlines = [OutcomePopulationInline]


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ["title", "definition"]
    search_fields = ["title"]
    inlines = [OutcomeInline]


@admin.register(StudyType)
class StudyTypeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(StudySource)
class StudySourceAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(ADMEStudyType)
class ADMEStudyTypeAdmin(admin.ModelAdmin):
    list_display = ["adme", "study_type"]
    search_fields = ["adme__novel_food__title", "study_type__title"]
    autocomplete_fields = ["adme", "study_type"]


@admin.register(OutcomePopulation)
class OutcomePopulationAdmin(admin.ModelAdmin):
    list_display = ["outcome", "population"]
    search_fields = ["outcome__assessment__title", "population__description"]
    autocomplete_fields = ["outcome", "population"]


@admin.register(SpecificToxicityStudy)
class SpecificToxicityStudyAdmin(admin.ModelAdmin):
    list_display = ["id_tox", "id_spec_tox"]
    autocomplete_fields = [
        "id_tox",
        "id_spec_tox",
    ]  # Enables autocomplete for foreign key fields
    search_fields = ["id_tox__novel_food__title", "id_spec_tox__description"]
