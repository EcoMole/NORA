from django.contrib import admin
from util.admin_utils import duplicate_model

from .models import (
    Composition,
    FoodForm,
    NovelFoodVariant,
    Parameter,
    ParameterType,
    ProductionNovelFoodVariant,
    ProposedUse,
    RiskAssessRedFlag,
    RiskAssessRedFlagNFVariant,
)


class CompositionInline(admin.TabularInline):
    model = Composition
    extra = 1
    autocomplete_fields = ["parameter", "unit", "qualifier"]


class ProposedUseInline(admin.TabularInline):
    model = ProposedUse
    extra = 1
    autocomplete_fields = ["population"]


class ProductionNovelFoodVariantInline(admin.TabularInline):
    model = ProductionNovelFoodVariant
    extra = 1
    autocomplete_fields = ["process"]


class RiskAssessRedFlagNFVariantInline(admin.TabularInline):
    model = RiskAssessRedFlagNFVariant
    extra = 1
    autocomplete_fields = ["risk_assess_red_flag"]


@admin.register(NovelFoodVariant)
class NovelFoodVariantAdmin(admin.ModelAdmin):
    autocomplete_fields = ["novel_food", "food_form"]
    inlines = [
        ProposedUseInline,
        CompositionInline,
        ProductionNovelFoodVariantInline,
        RiskAssessRedFlagNFVariantInline,
    ]
    actions = [duplicate_model]


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
    ]
    search_fields = ["title"]
    list_filter = ["type"]
    actions = [duplicate_model]
    autocomplete_fields = ["vocab_id"]


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


@admin.register(RiskAssessRedFlag)
class RiskAssessRedFlagAdmin(admin.ModelAdmin):
    search_fields = ["title"]

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
