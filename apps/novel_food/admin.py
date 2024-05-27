from django.contrib import admin

from novel_food.models import (
    NovelFood,
    FoodCategory,
    NutritionalDisadvantage,
    NovelFoodCategory,
    Category
)

from allergenicity.models import AllergenicityNovelFood

class NovelFoodCategoryInline(admin.TabularInline):
    model =  NovelFoodCategory #NovelFood.categories.through
    extra = 1

class AllergenicityNovelFoodInline(admin.StackedInline):
    model = AllergenicityNovelFood
    extra = 1
    autocomplete_fields = ['allergenicity']

@admin.register(NovelFood)
class NovelFoodAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Information', {
            'fields': ['opinion', 'nf_code']
        }),
        ('Toxicity', {
            'fields': [('is_mutagenic', 'is_genotoxic', 'is_carcinogenic')]
        }),
        ('Nutrition', {
            'fields': ['protein_digestibility', 'antinutritional_factors']
        }),
        ('STABILITY', {
            'fields': ['sufficient_data', 'food_matrices', 'shelflife_value', 'shelflife_unit'],
            'description': 'This section is for stability related fields'
        }),
        ('Miscellaneous', {
            'fields': ['rms_efsa', 'endocrine_disrupt_prop', 'outcome', 'outcome_remarks'],
            'classes': ['collapse']
        })
    ]
    list_display = ['nf_code', 'opinion', 'outcome', 'outcome_remarks']
    search_fields = ['nf_code']
    inlines = [NovelFoodCategoryInline, AllergenicityNovelFoodInline]
    list_filter = ['is_carcinogenic', 'is_genotoxic', 'is_mutagenic']


""" class NovelFoodAdmin(admin.ModelAdmin):
    list_display = [
        'nf_code',
        'opinion',
        'outcome',
        'outcome_remarks'
    ]

    inlines = [NovelFoodCategoryInline, AllergenicityNovelFoodInline] """

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
    list_display = [
        'outcome',
        'explanation',
        'novel_food'
    ]