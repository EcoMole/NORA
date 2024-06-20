from core.models import Contribution
from django.contrib import admin
from django.utils.html import format_html

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

    def pdf_link(self, obj):
        if obj.pdf:
            return format_html('<a href="{}" target="_blank">PDF</a>', obj.pdf.url)
        return "No PDF"

    pdf_link.short_description = "PDF File"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ["number"]
    list_display = ["number"]
    search_fields = ["number"]
    inlines = [QuestionApplicantInline, MandateInline]


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

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(MandateType)
class MandateTypeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(ScientificOfficer)
class ScientificOfficerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "middle_name", "last_name"]
    search_fields = ["first_name", "middle_name", "last_name"]
    list_filter = ["last_name"]
