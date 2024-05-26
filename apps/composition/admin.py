from django.contrib import admin

from .models import (
    FootNote,
    NovelFoodVariant,
    Parameter,
    ParameterType,
    FoodFormNovelFoodVariant,
    Composition,
    FoodForm
)

class FoodFormNFVariantInline(admin.TabularInline):
    model = FoodFormNovelFoodVariant #TODO change the name of the model
    extra = 1 

@admin.register(FootNote)
class FootNoteAdmin(admin.ModelAdmin):
    list_display = [
        "footnote",
    ]
    search_fields = ["footnote"]

@admin.register(FoodForm)
class FoodFormAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
    search_fields = ["title"]

@admin.register(NovelFoodVariant)
class NovelFoodVariantAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
    search_fields = ["title"]
    inlines = [FoodFormNFVariantInline]

@admin.register(ParameterType)
class ParameterTypeAdmin(admin.ModelAdmin):
    list_display = [
        "parameter_type",
    ]
    search_fields = ["parameter_type"]


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = [
        "parameter_title",
        "parameter_type",
        "parameter_tax_node",
    ]
    search_fields = ["title"]
    list_filter = ["parameter_type"]

@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = [
        "parameter",
        "value",
        "upper_range_value",
        "unit",
        "novel_food_variant",
        "qualifier",
        "type",
        "footnote",
    ]

