from core.models import Contribution
from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Applicant,
    Mandate,
    OPAuthor,
    Opinion,
    OPQuestion,
    OPScientificOfficer,
    Panel,
    Question,
    ScientificOfficer,
)


class OPAuthorInline(admin.TabularInline):
    model = OPAuthor
    extra = 1


class OPQuestionInline(admin.TabularInline):
    model = OPQuestion
    extra = 1


class OPScientificOfficerInline(admin.TabularInline):
    model = OPScientificOfficer
    extra = 1


class MandateInline(admin.TabularInline):
    model = Mandate
    extra = 1


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
        "outcome",
        "pdf_link",
    ]
    search_fields = ["title", "doi"]
    list_filter = ["outcome", "publication_date"]
    autocomplete_fields = ["id_op_type"]
    inlines = [
        ContributionInline,
        OPAuthorInline,
        OPQuestionInline,
        OPScientificOfficerInline,
    ]

    def pdf_link(self, obj):
        if obj.pdf:
            return format_html('<a href="{}" target="_blank">PDF</a>', obj.pdf.url)
        return "No PDF"

    pdf_link.short_description = "PDF File"


@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    list_display = ["panel"]
    search_fields = ["panel"]


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(Mandate)
class MandateAdmin(admin.ModelAdmin):
    list_display = ["title", "mandate_parent"]
    search_fields = ["title"]
    autocomplete_fields = ["regulation"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question", "mandate"]
    search_fields = ["question"]
    list_filter = ["mandate"]


@admin.register(ScientificOfficer)
class ScientificOfficerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "middle_name", "last_name"]
    search_fields = ["first_name", "middle_name", "last_name"]
    list_filter = ["last_name"]
