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

from novel_food.models import NovelFood
from allergenicity.models import AllergenicityNovelFood

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

""" class NovelFoodInline(admin.TabularInline):
    model = NovelFood
    extra = 1 """

class AllergenicityNovelFoodInline(admin.StackedInline):
    model = AllergenicityNovelFood
    extra = 1
    autocomplete_fields = ['allergenicity']


class NovelFoodInline(admin.StackedInline):
    model = NovelFood
    extra = 1  # Number of extra forms to show
    verbose_name = "Novel food"
    verbose_name_plural = "Novel foods"
    show_change_link = True
    """ fieldsets = [
        ('General Information', {
            'fields': ['nf_code']
        }),
        ('Toxicity', {
            'fields': [('is_mutagenic', 'is_genotoxic', 'is_carcinogenic')]
        }),
        ('Nutrition', {
            'fields': ['protein_digestibility', 'antinutritional_factors']
        }),
        ('STABILITY', {
            'fields': ['sufficient_data', 'food_matrices', 'shelflife_value', 'shelflife_unit'],
            'description': 'This section is for stability related fields'
        }),
        ('Miscellaneous', {
            'fields': ['rms_efsa', 'endocrine_disrupt_prop', 'outcome', 'outcome_remarks'],
            'classes': ['collapse']
        })
    ]
 """

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    #fields = ['title', 'doi']
    def novel_foods(self, obj):
        novel_foods = obj.novel_food.all()
        url = f"/admin/novel_food/novelfood/{novel_foods[0].id_study}/change/"
        return f'<a href="{url}">{novel_foods[0].nf_code}</a>'

    list_display = [
        "title",
        "doi",
        "publication_date",
        "adoption_date",
        "outcome",
        'novel_foods'
    ]
    search_fields = ["title", "doi"]
    list_filter = ["outcome", "publication_date"]
    inlines = [OPAuthorInline, OPQuestionInline, OPScientificOfficerInline, NovelFoodInline]


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
