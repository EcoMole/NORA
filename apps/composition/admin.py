from django.contrib import admin

from .models import (
    NovelFoodVariant,
    Parameter,
    ParameterType,
    FoodFormNovelFoodVariant,
    Composition,
    FoodForm,
    ProposedUse,
    ProposedUseType,
    ProductionNovelFoodVariant,
)

class FoodFormNFVariantInline(admin.TabularInline):
    model = FoodFormNovelFoodVariant #TODO change the name of the model
    extra = 1 

class CompositionInline(admin.TabularInline):
    model = Composition
    extra = 1

class ProposedUseInline(admin.TabularInline):
    model = ProposedUse
    extra = 1

class ProductionNovelFoodVariantInline(admin.TabularInline):
    model = ProductionNovelFoodVariant
    extra = 1

@admin.register(NovelFoodVariant)
class NovelFoodVariantAdmin(admin.ModelAdmin):
    autocomplete_fields = ['novel_food']
    inlines = [FoodFormNFVariantInline, ProposedUseInline, CompositionInline, ProductionNovelFoodVariantInline]


@admin.register(FoodForm)
class FoodFormAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
    search_fields = ["title"]


@admin.register(ParameterType)
class ParameterTypeAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
    search_fields = ["title"]


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "type",
        "tax_node",
    ]
    search_fields = ["title"]
    list_filter = ["type"]

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
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(ProposedUseType)
class ProposedUseTypeAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]