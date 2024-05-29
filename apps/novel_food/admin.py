from django.contrib import admin
from django import forms

from novel_food.models import (
    NovelFood,
    FoodCategory,
    NutritionalDisadvantage,
    NovelFoodCategory,
    Category,
    NovelFoodChemical,
    NovelFoodOrganism,
    Organism,
    OrganismSyn,
    Chemical,
    BackgroundExposureAssessment,
    NovelFoodSyn,
    SynonymType,
    Allergenicity,
    AllergenicityNovelFood,
    SubstanceOfConcernNovelFood,
    ChemicalSyn,
    GenotoxFinalOutcome
)

#from allergenicity.models import  Allergenicity

class NovelFoodCategoryInline(admin.TabularInline):
    model =  NovelFoodCategory #NovelFood.categories.through
    extra = 1

class NovelFoodChemicalInline(admin.TabularInline):
    model = NovelFoodChemical
    extra = 1

class NovelFoodOrganismInline(admin.TabularInline):
    model = NovelFoodOrganism
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
    extra = 1

class OrganismSynInline(admin.TabularInline):
    model = OrganismSyn
    extra = 1

class ChemicalSynInline(admin.TabularInline):
    model = ChemicalSyn
    extra = 1

@admin.register(NovelFood)
class NovelFoodAdmin(admin.ModelAdmin):
    #form = NovelFoodForm
    fieldsets = [
        ('General Information', {
            'fields': ['opinion', 'title', 'nf_code', 'food_category']
        }),
        ('Toxicity', {
            'fields': ['is_mutagenic', 'genotox_final_outcome', 'is_carcinogenic']
        }),
        ('Nutrition', {
            'fields': ['protein_digestibility', 'antinutritional_factors', 'nutritional_disadvantage'],
        }),
        ('STABILITY', {
            'fields': ['sufficient_data', 'food_matrices', 'instability_concerns', ('shelflife_value', 'shelflife_unit')],
            'description': 'This section is for stability related fields'
        }),
        
        ('HAZARDS', {
            'fields': ['endocrine_disrupt_prop'],
        }),
        ('OUTCOME', {
            'fields': [('outcome', 'outcome_remarks')],
        }),
        ('Miscellaneous', {
            'fields': ['rms_efsa' ],
            'classes': ['collapse']
        }),

    ]
    list_display = ['nf_code', 'opinion', 'outcome', 'outcome_remarks']
    search_fields = ['nf_code', 'title']
    autocomplete_fields = ['opinion']
    inlines = [NovelFoodCategoryInline, NovelFoodChemicalInline, NovelFoodOrganismInline, BackgroundExposureAssessmentInline, NovelFoodSynInline, AllergenicityNovelFoodInline, 
               SubstanceOfConcernNovelFoodInline]
    list_filter = ['is_carcinogenic', 'is_mutagenic']

@admin.register(Organism)
class OrganismAdmin(admin.ModelAdmin):
    list_display = ['organism_node']
    inlines = [OrganismSynInline]

@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ['catalogue_identity']
    inlines = [ChemicalSynInline]

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'definition'
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'definition',
        'regulation_id'
    ]

@admin.register(NutritionalDisadvantage)
class NutritionalDisadvantageAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(SynonymType)
class SynonymAdmin(admin.ModelAdmin):
    list_display = ['synonym_type']

@admin.register(Allergenicity)
class AllergenicityAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(GenotoxFinalOutcome)
class GenotoxFinalOutcomeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
