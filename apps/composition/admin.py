from core.models import Contribution
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
    readonly_fields = ("get_vocab_path",)

    def get_vocab_path(self, obj):
        path = ""
        if descendants := obj.process.get_significant_descendants():
            for descendant in descendants:
                path = descendant.name + " , " + path
            path = path.rstrip(" , ") + " < "
        path += obj.process.name.upper()
        if ancestors := obj.process.get_significant_ancestors():
            while len(ancestors) > 0 and ancestors[-1].code in [
                "A0B95",  # <TaxonomyNode: Process (A0B95)>
                "A0B8V",  # <TaxonomyNode: Facets (A0B8V)>
                "A0C5X",  # <TaxonomyNode: All Lists (A0C5X)>
                "root",
            ]:
                ancestors = ancestors[:-1]
            for ancestor in ancestors:
                path += " < " + ancestor.name
        return path

    get_vocab_path.short_description = "Vocab Path"


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
    list_display = ["nf_variant_str", "food_form", "responsible_person"]

    def nf_variant_str(self, obj):
        return str(obj)

    nf_variant_str.short_description = "NF Variant"

    def food_form(self, obj):
        return obj.food_form.title

    food_form.short_description = "Food form"

    def responsible_person(self, obj):
        # Get novel food for this variant
        novel_food = obj.novel_food
        # Get opinion for this novel food
        opinion = novel_food.opinion
        # Get contribution for this opinion
        contribution = Contribution.objects.filter(opinion=opinion).first()
        if contribution:
            user = contribution.user
            return user.first_name

    responsible_person.short_description = "Responsible Person"

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
        "nf_variant",
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
