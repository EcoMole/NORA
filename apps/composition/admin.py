from django.contrib import admin
from util.admin_utils import duplicate_model

from .models import (
    Composition,
    FoodForm,
    FoodFormNovelFoodVariant,
    NovelFoodVariant,
    Parameter,
    ParameterType,
    ProductionNovelFoodVariant,
    ProposedUse,
    ProposedUseType,
    RiskAssessmentRedFlags,
    RiskAssessmentRedFlagsNFVariant,
)


class FoodFormNFVariantInline(admin.TabularInline):
    model = FoodFormNovelFoodVariant  # TODO change the name of the model
    extra = 1


class CompositionInline(admin.TabularInline):
    model = Composition
    extra = 1
    autocomplete_fields = ["unit", "qualifier"]


class ProposedUseInline(admin.TabularInline):
    model = ProposedUse
    extra = 1
    autocomplete_fields = ["population"]


class ProductionNovelFoodVariantInline(admin.TabularInline):
    model = ProductionNovelFoodVariant
    extra = 1
    autocomplete_fields = ["process"]


class RiskAssessmentRedFlagsNFVariantInline(admin.TabularInline):
    model = RiskAssessmentRedFlagsNFVariant
    extra = 1


@admin.register(NovelFoodVariant)
class NovelFoodVariantAdmin(admin.ModelAdmin):
    autocomplete_fields = ["novel_food"]
    inlines = [
        FoodFormNFVariantInline,
        ProposedUseInline,
        CompositionInline,
        ProductionNovelFoodVariantInline,
        RiskAssessmentRedFlagsNFVariantInline,
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
    actions = [duplicate_model]


@admin.register(RiskAssessmentRedFlags)
class RiskAssessmentRedFlagsAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
