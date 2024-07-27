from core.models import Contribution
from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from utils.admin_utils import duplicate_model

from .models import (
    Applicant,
    Mandate,
    MandateType,
    Opinion,
    OpinionPanel,
    OpinionQuestion,
    OpinionSciOfficer,
    Panel,
    Question,
    QuestionApplicant,
    ScientificOfficer,
)


class AdminURLWidget(forms.URLInput):
    """Widget that shows an input field and a clickable URL next to it."""

    def render(self, name, value, attrs=None, renderer=None):
        if value:
            link_html = mark_safe(f'<a href="{value}" target="_blank">{value}</a>')
        else:
            link_html = ""
        input_html = super().render(name, value, attrs, renderer)
        return mark_safe(f"{input_html}<p>{link_html}</p>")


class MandateInline(admin.TabularInline):
    model = Mandate
    extra = 1
    autocomplete_fields = ["regulation", "question"]


class OPAuthorInline(admin.TabularInline):
    model = OpinionPanel
    extra = 1
    autocomplete_fields = ["panel"]


class QuestionApplicantInline(admin.TabularInline):
    model = QuestionApplicant
    extra = 1
    autocomplete_fields = ["question", "applicant"]


class OpinionQuestionInline(admin.TabularInline):
    model = OpinionQuestion
    extra = 1
    autocomplete_fields = ["question"]


class OPScientificOfficerInline(admin.TabularInline):
    model = OpinionSciOfficer
    extra = 1
    autocomplete_fields = ["sci_officer"]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class ContributionInline(admin.TabularInline):
    model = Contribution
    extra = 0


class HasContributor(admin.SimpleListFilter):
    title = "Contributor"
    parameter_name = "has_contributor"

    def lookups(self, request, model_admin):
        return (
            Contribution.objects.filter(opinion__isnull=False).values_list(
                "user__id", "user__first_name"
            )
        ).distinct()

    def queryset(self, request, queryset):
        if self.value():
            # self.value() is the id of the selected contributor
            return queryset.filter(contributions__user__id=self.value())


class HasContributorStatus(admin.SimpleListFilter):
    title = "Contributor Status"
    parameter_name = "has_contributor_status"

    def lookups(self, request, model_admin):
        return (
            Contribution.objects.filter(opinion__isnull=False)
            .values_list("status", "status")
            .distinct()
        )

    def queryset(self, request, queryset):
        if self.value():
            # self.value() is the status of the selected contributor
            return queryset.filter(contributions__status=self.value())


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "publication_date",
        "adoption_date",
        "url",
        "get_contributions",
    ]
    list_display_links = [
        "title",
        "publication_date",
        "adoption_date",
    ]
    search_fields = ["title", "doi"]
    list_filter = [HasContributor, HasContributorStatus]
    autocomplete_fields = ["document_type"]
    inlines = [
        ContributionInline,
        OPAuthorInline,
        OpinionQuestionInline,
        OPScientificOfficerInline,
    ]
    actions = [duplicate_model]

    def formfield_for_dbfield(self, db_field, **kwargs):
        """uses AdminURLWidget for the `url` field"""
        if db_field.name == "url":
            kwargs["widget"] = AdminURLWidget
        return super().formfield_for_dbfield(db_field, **kwargs)

    def get_contributions(self, obj):
        result = "<br>".join(
            [str(contribution) for contribution in obj.contributions.all()]
        )
        return format_html(result)

    get_contributions.short_description = "Contributions"
    get_contributions.admin_order_field = "contributions__user__first_name"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ["number"]
    list_display = ["number"]
    search_fields = ["number"]
    inlines = [QuestionApplicantInline, MandateInline]
    actions = [duplicate_model]


@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(Mandate)
class MandateAdmin(admin.ModelAdmin):
    list_display = ["question", "mandate_type", "regulation"]
    search_fields = ["question", "mandate_type", "regulation"]
    actions = [duplicate_model]

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(MandateType)
class MandateTypeAdmin(admin.ModelAdmin):
    list_display = ["title", "definition"]
    search_fields = ["title", "definition"]


@admin.register(ScientificOfficer)
class ScientificOfficerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "middle_name", "last_name"]
    search_fields = ["first_name", "middle_name", "last_name"]
    list_filter = ["last_name"]
