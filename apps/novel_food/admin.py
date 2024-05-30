from django.contrib import admin
from novel_food.models import (
    HBGV,
    Allergenicity,
    AllergenicityNovelFood,
    BackgroundExposureAssessment,
    Category,
    Chemical,
    ChemicalSyn,
    FoodCategory,
    GenotoxFinalOutcome,
    NovelFood,
    NovelFoodCategory,
    NovelFoodChemical,
    NovelFoodOrganism,
    NovelFoodSyn,
    NutritionalDisadvantage,
    Organism,
    OrganismSyn,
    SubstanceOfConcernNovelFood,
    SynonymType,
)

# from allergenicity.models import  Allergenicity


class NovelFoodCategoryInline(admin.TabularInline):
    model = NovelFoodCategory  # NovelFood.categories.through
    extra = 1


class NovelFoodChemicalInline(admin.TabularInline):
    model = NovelFoodChemical
    extra = 1


class NovelFoodOrganismInline(admin.TabularInline):
    model = NovelFoodOrganism
    autocomplete_fields = ["org_part", "variant"]
    extra = 1


class HBGVInline(admin.TabularInline):
    model = HBGV
    autocomplete_fields = ["type", "novel_food", "exceeded_for_population", "substance"]
    extra = 1


class NutritionalDisadvantageInline(admin.TabularInline):
    model = NutritionalDisadvantage
    extra = 1


class BackgroundExposureAssessmentInline(admin.TabularInline):
    model = BackgroundExposureAssessment
    extra = 1


class NovelFoodSynInline(admin.TabularInline):
    model = NovelFoodSyn
    extra = 1


class AllergenicityNovelFoodInline(admin.TabularInline):
    model = AllergenicityNovelFood
    extra = 1


class SubstanceOfConcernNovelFoodInline(admin.TabularInline):
    model = SubstanceOfConcernNovelFood
    autocomplete_fields = ["substance_of_concern"]
    extra = 1


class OrganismSynInline(admin.TabularInline):
    model = OrganismSyn
    extra = 1


class ChemicalSynInline(admin.TabularInline):
    model = ChemicalSyn
    extra = 1


@admin.register(NovelFood)
class NovelFoodAdmin(admin.ModelAdmin):
    # form = NovelFoodForm
    fieldsets = [
        (
            "General Information",
            {"fields": ["opinion", "title", "nf_code", "food_category"]},
        ),
        (
            "Toxicity",
            {
                "fields": [
                    "tox_study_required",
                    "mutagenicity",
                    "carcinogenicity",
                    "genotox_final_outcome",
                ]
            },
        ),
        (
            "Nutrition",
            {
                "fields": [
                    "protein_digestibility",
                    "antinutritional_factors",
                    "nutritional_disadvantage",
                ],
            },
        ),
        (
            "STABILITY",
            {
                "fields": [
                    "sufficient_data",
                    "food_matrices",
                    "instability_concerns",
                    ("shelflife_value", "shelflife_unit"),
                ],
                "description": "This section is for stability related fields",
            },
        ),
        (
            "HAZARDS",
            {
                "fields": ["endocrine_disrupt_prop"],
            },
        ),
        (
            "OUTCOME",
            {
                "fields": [("outcome", "outcome_remarks")],
            },
        ),
        ("Miscellaneous", {"fields": ["catalogue_identity"], "classes": ["collapse"]}),
    ]
    list_display = ["nf_code", "opinion", "outcome", "outcome_remarks"]
    search_fields = ["nf_code", "title"]
    autocomplete_fields = ["opinion", "shelflife_unit", "catalogue_identity"]
    inlines = [
        NovelFoodSynInline,
        NovelFoodCategoryInline,
        NovelFoodChemicalInline,
        NovelFoodOrganismInline,
        BackgroundExposureAssessmentInline,
        HBGVInline,
        AllergenicityNovelFoodInline,
        SubstanceOfConcernNovelFoodInline,
    ]
    list_filter = ["carcinogenicity", "mutagenicity"]


@admin.register(Organism)
class OrganismAdmin(admin.ModelAdmin):
    list_display = ["organism_node"]
    autocomplete_fields = ["organism_node"]
    inlines = [OrganismSynInline]


@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ["catalogue_identity"]
    autocomplete_fields = ["catalogue_identity"]
    inlines = [ChemicalSynInline]


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "definition"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "definition", "regulation"]


@admin.register(NutritionalDisadvantage)
class NutritionalDisadvantageAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(SynonymType)
class SynonymAdmin(admin.ModelAdmin):
    list_display = ["synonym_type"]


@admin.register(Allergenicity)
class AllergenicityAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(GenotoxFinalOutcome)
class GenotoxFinalOutcomeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
