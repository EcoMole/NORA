from django.contrib import admin

from .models import (
    Applicant,
    Dossier,
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


class DossierInline(admin.TabularInline):
    model = Dossier
    extra = 1


class MandateInline(admin.TabularInline):
    model = Mandate
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "doi",
        "publication_date",
        "adoption_date",
        "outcome",
    ]
    search_fields = ["title", "doi"]
    list_filter = ["outcome", "publication_date"]
    inlines = [OPAuthorInline, OPQuestionInline, OPScientificOfficerInline]


@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    list_display = ["panel"]
    search_fields = ["panel"]


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    inlines = [DossierInline]


@admin.register(Mandate)
class MandateAdmin(admin.ModelAdmin):
    list_display = ["title", "mandate_parent"]
    search_fields = ["title"]


""" @admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    list_display = ["number", "applicant"]
    search_fields = ["number"]
    list_filter = ["applicant"]
    inlines = [QuestionInline] """


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question", "dossier", "mandate"]
    search_fields = ["question"]
    list_filter = ["dossier", "mandate"]


@admin.register(ScientificOfficer)
class ScientificOfficerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "middle_name", "last_name"]
    search_fields = ["first_name", "middle_name", "last_name"]
    list_filter = ["last_name"]
