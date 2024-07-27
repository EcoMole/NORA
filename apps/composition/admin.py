from core.models import Contribution
from django.contrib import admin
from django.utils.html import format_html

from utils.admin_utils import duplicate_model

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


class HasContributor(admin.SimpleListFilter):
    title = "Opinion Contributor"
    parameter_name = "has_opinion_contributor"

    def lookups(self, request, model_admin):
        return (
            Contribution.objects.filter(opinion__isnull=False).values_list(
                "user__id", "user__first_name"
            )
        ).distinct()

    def queryset(self, request, queryset):
        if self.value():
            # self.value() is the id of the selected contributor
            return queryset.filter(
                novel_food__opinion__contributions__user__id=self.value()
            )


class HasContributorStatus(admin.SimpleListFilter):
    title = "Opinion Contributor Status"
    parameter_name = "has_opinion_contributor_status"

    def lookups(self, request, model_admin):
        return (
            Contribution.objects.filter(opinion__isnull=False)
            .values_list("status", "status")
            .distinct()
        )

    def queryset(self, request, queryset):
        if self.value():
            # self.value() is the status of the selected contributor
            return queryset.filter(
                novel_food__opinion__contributions__status=self.value()
            )


@admin.register(NovelFoodVariant)
class NovelFoodVariantAdmin(admin.ModelAdmin):
    list_display = [
        "get_novel_food",
        "food_form",
        "get_question_numbers",
        "get_contributions",
    ]
    list_display_links = ["get_novel_food", "food_form"]
    readonly_fields = ("get_question_numbers",)
    list_filter = [HasContributor, HasContributorStatus, "food_form"]
    search_fields = ["novel_food__title", "novel_food__nf_code", "food_form__title"]
    autocomplete_fields = ["novel_food", "food_form"]
    inlines = [
        ProductionNovelFoodVariantInline,
        RiskAssessRedFlagNFVariantInline,
        CompositionInline,
        ProposedUseInline,
    ]

    def get_novel_food(self, obj):
        return str(obj.novel_food)

    get_novel_food.short_description = "Novel Food"
    get_novel_food.admin_order_field = "novel_food__title"

    def get_question_numbers(self, obj):
        questions = [oq.question for oq in obj.novel_food.opinion.questions.all()]

        if not questions:
            return ""

        question_numbers = ", ".join([str(q.number) for q in questions])
        return question_numbers

    get_question_numbers.short_description = "Question Number"
    get_question_numbers.admin_order_field = (
        "novel_food__opinion__questions__question__number"
    )

    def get_contributions(self, obj):
        contributions = Contribution.objects.filter(opinion=obj.novel_food.opinion)
        result = "<br>".join([str(contribution) for contribution in contributions])
        return format_html(result)

    get_contributions.short_description = "Opinion Contributions"

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
