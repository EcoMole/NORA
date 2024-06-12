from django.contrib import admin
from novel_food.models import (
    HBGV,
    Allergenicity,
    AllergenicityNovelFood,
    BackgroundExposureAssessment,
    Category,
    Chemical,
    ChemicalSyn,
    Family,
    FoodCategory,
    GenotoxFinalOutcome,
    Genus,
    NovelFood,
    NovelFoodCategory,
    NovelFoodChemical,
    NovelFoodOrganism,
    NovelFoodSyn,
    NutritionalDisadvantage,
    Organism,
    OrganismSyn,
    OrgModification,
    SubstanceOfConcernNovelFood,
    SynonymType,
    Type,
)

# from allergenicity.models import  Allergenicity


class NovelFoodCategoryInline(admin.TabularInline):
    model = NovelFoodCategory  # NovelFood.categories.through
    extra = 1


class NovelFoodChemicalInline(admin.TabularInline):
    model = NovelFoodChemical
    extra = 1


class NovelFoodOrganismInline(admin.TabularInline):
    model = NovelFoodOrganism
    autocomplete_fields = ["org_part", "organism"]
    extra = 1


class HBGVInline(admin.TabularInline):
    model = HBGV
    autocomplete_fields = ["type", "novel_food", "exceeded_for_population", "substance"]
    extra = 1


class NutritionalDisadvantageInline(admin.TabularInline):
    model = NutritionalDisadvantage
    extra = 1


class BackgroundExposureAssessmentInline(admin.TabularInline):
    model = BackgroundExposureAssessment
    extra = 1


class NovelFoodSynInline(admin.TabularInline):
    model = NovelFoodSyn
    extra = 1


class AllergenicityNovelFoodInline(admin.TabularInline):
    model = AllergenicityNovelFood
    extra = 1


class SubstanceOfConcernNovelFoodInline(admin.TabularInline):
    model = SubstanceOfConcernNovelFood
    autocomplete_fields = ["substance_of_concern"]
    extra = 1


class OrganismSynInline(admin.TabularInline):
    model = OrganismSyn
    extra = 1


class ChemicalSynInline(admin.TabularInline):
    model = ChemicalSyn
    extra = 1


class FamilyInline(admin.TabularInline):
    model = Family
    extra = 1


class GenusInline(admin.TabularInline):
    model = Genus
    extra = 1


class OrganismInline(admin.TabularInline):
    model = Organism
    extra = 1


@admin.register(NovelFood)
class NovelFoodAdmin(admin.ModelAdmin):
    # form = NovelFoodForm
    fieldsets = [
        (
            "General Information",
            {"fields": ["opinion", "title", "nf_code", "food_category"]},
        ),
        (
            "Toxicity",
            {
                "fields": [
                    "tox_study_required",
                    "mutagenicity",
                    "carcinogenicity",
                    "genotox_final_outcome",
                    "specific_toxicity",
                ]
            },
        ),
        (
            "Nutrition",
            {
                "fields": [
                    "protein_digestibility",
                    "antinutritional_factors",
                    "nutritional_disadvantage",
                ],
            },
        ),
        (
            "STABILITY",
            {
                "fields": [
                    "sufficient_data",
                    "food_matrices",
                    "instability_concerns",
                    ("shelflife_value", "shelflife_unit"),
                ],
                "description": "This section is for stability related fields",
            },
        ),
        (
            "HAZARDS",
            {
                "fields": ["endocrine_disrupt_prop"],
            },
        ),
        (
            "OUTCOME",
            {
                "fields": [("outcome", "outcome_remarks")],
            },
        ),
        ("Miscellaneous", {"fields": ["catalogue_identity"], "classes": ["collapse"]}),
    ]
    list_display = ["nf_code", "opinion", "outcome", "outcome_remarks"]
    search_fields = ["nf_code", "title"]
    autocomplete_fields = ["opinion", "shelflife_unit", "catalogue_identity"]
    inlines = [
        SubstanceOfConcernNovelFoodInline,
        NovelFoodSynInline,
        NovelFoodCategoryInline,
        NovelFoodChemicalInline,
        NovelFoodOrganismInline,
        BackgroundExposureAssessmentInline,
        HBGVInline,
        AllergenicityNovelFoodInline,
    ]
    list_filter = ["carcinogenicity", "mutagenicity"]


class IsFromVocabFilter(admin.SimpleListFilter):
    title = "Is from Vocab"
    parameter_name = "is_from_vocab"

    def lookups(self, request, model_admin):
        return (
            ("Yes", "Yes"),
            ("No", "No"),
        )

    def queryset(self, request, queryset):
        if self.value() == "Yes":
            return queryset.filter(organism_node__isnull=False)
        if self.value() == "No":
            return queryset.filter(organism_node__isnull=True)


@admin.register(Organism)
class OrganismAdmin(admin.ModelAdmin):
    list_display = [
        "get_organism",
        "get_scientific_name",
        "get_parent_nodes",
        "get_is_from_vocab",
    ]
    autocomplete_fields = ["organism_node"]
    inlines = [OrganismSynInline]
    search_fields = ["species_title"]
    list_filter = [IsFromVocabFilter]

    def get_is_from_vocab(self, obj):
        return obj.organism_node is not None

    get_is_from_vocab.boolean = True
    get_is_from_vocab.short_description = "Is from Vocab"

    def get_scientific_name(self, obj):
        if obj.organismsyn_set.filter(type__synonym_type="scientific name").exists():
            return obj.organismsyn_set.get(type__synonym_type="scientific name").synonym
        else:
            return None

    get_scientific_name.short_description = "Scientific Name"

    def get_organism(self, obj):
        if obj.species_title:
            return obj.species_title
        if obj.organism_node:
            return obj.organism_node.name
        else:
            return None

    get_organism.short_description = "Spicies"

    def get_parent_nodes(self, obj):
        if obj.organism_node:
            ancestors = obj.organism_node.get_significant_ancestors()
            while len(ancestors) > 0 and ancestors[-1].code in [
                "A0C5X",
                "A0B8X",
                "root",
            ]:
                # we do not need to display "All Lists (A0C5X)", "Natural sources (A0B8X)" and "root"
                ancestors = ancestors[:-1]
            res = ""
            for ancestor in ancestors:
                res += " < " + ancestor.name
            return res.lstrip(" < ")
        else:
            return f"{obj.genus.title} < {obj.genus.family.title} < {obj.genus.family.type.title}"

    get_parent_nodes.short_description = "Taxonomy Path"


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    inlines = [FamilyInline]


# Admin for Family
@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ["title", "type"]
    search_fields = ["title"]
    list_filter = ["type"]
    inlines = [GenusInline]


# Admin for Genus
@admin.register(Genus)
class GenusAdmin(admin.ModelAdmin):
    list_display = ["title", "family"]
    search_fields = ["title"]
    list_filter = ["family"]
    inlines = [OrganismInline]


@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ["catalogue_identity"]
    autocomplete_fields = ["catalogue_identity"]
    inlines = [ChemicalSynInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "definition", "regulation"]


@admin.register(NutritionalDisadvantage)
class NutritionalDisadvantageAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "definition"]


@admin.register(SynonymType)
class SynonymAdmin(admin.ModelAdmin):
    list_display = ["synonym_type"]


@admin.register(Allergenicity)
class AllergenicityAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(GenotoxFinalOutcome)
class GenotoxFinalOutcomeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(OrgModification)
class OrgModificationAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
