from core.models import Contribution
from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from util.admin_utils import duplicate_model

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
    extra = 1


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "publication_date",
        "adoption_date",
        "pdf_link",
        "responsible_person",
        "status",
    ]
    list_display_links = [
        "title",
        "publication_date",
        "adoption_date",
        "responsible_person",
        "status",
    ]
    search_fields = ["title", "doi"]
    list_filter = ["publication_date"]
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

    def pdf_link(self, obj):
        if obj.pdf:
            return format_html('<a href="{}" target="_blank">PDF</a>', obj.pdf.url)
        return "No PDF"

    pdf_link.short_description = "PDF File"

    def responsible_person(self, obj):
        contribution = Contribution.objects.filter(opinion=obj).first()
        if contribution:
            user = contribution.user
            return user.first_name

    responsible_person.short_description = "Responsible Person"

    def status(self, obj):
        contribution = Contribution.objects.filter(opinion=obj).first()
        if contribution:
            return contribution.status

    status.short_description = "Status"


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
