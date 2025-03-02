from core.models import Contribution
from django.contrib import admin
from django.utils.html import format_html
from novel_food.models import (
    HBGV,
    Allergenicity,
    AllergenicityNovelFood,
    BackgroundExposureAssessment,
    ChemDescriptor,
    Chemical,
    ChemicalSyn,
    Family,
    FoodCategory,
    FoodCategoryNovelFood,
    GenotoxFinalOutcome,
    Genus,
    NovelFood,
    NovelFoodCategory,
    NovelFoodCategoryNovelFood,
    NovelFoodChemical,
    NovelFoodOrganism,
    NovelFoodSyn,
    Organism,
    OrganismSyn,
    OrgType,
    Species,
    SpecificToxicity,
    SubstanceOfConcernNovelFood,
    SynonymType,
)
from taxonomies.util import Descriptor

from utils.admin_utils import duplicate_model


class NovelFoodCategoryNovelFoodInline(admin.TabularInline):
    model = NovelFoodCategoryNovelFood
    extra = 1
    verbose_name_plural = "Novel/Traditional Food Identity"


class SpecificToxicityInline(admin.TabularInline):
    model = SpecificToxicity
    autocomplete_fields = ["specific_toxicity"]
    extra = 1
    verbose_name_plural = "Hazards"


class FoodCategoryNovelFoodInline(admin.TabularInline):
    model = FoodCategoryNovelFood
    extra = 1
    verbose_name_plural = "Proposed Use"


class NovelFoodChemicalInline(admin.TabularInline):
    model = NovelFoodChemical
    extra = 1
    autocomplete_fields = ["chemical"]
    verbose_name_plural = "Novel/Traditional Food Identity"


class NovelFoodOrganismInline(admin.TabularInline):  # StackedInline
    model = NovelFoodOrganism
    autocomplete_fields = ["org_part", "organism"]
    extra = 1
    fieldsets = [
        (
            "General Information",
            {
                "fields": [
                    "novel_food",
                    "organism",
                    "org_part",
                    "variant",
                    "is_gmo",
                ]
            },
        ),
        (
            "if microorganism",
            {
                "fields": [
                    "has_qps",
                ],
                "classes": ["collapse"],
            },
        ),
        (
            "if cell culture",
            {
                "fields": [
                    "cell_culture",
                    "cells_modified",
                ],
                "classes": ["collapse"],
            },
        ),
    ]
    verbose_name_plural = "Novel/Traditional Food Identity"


class HBGVInline(admin.TabularInline):
    model = HBGV
    autocomplete_fields = ["type", "novel_food", "exceeded", "substance"]
    extra = 1
    verbose_name_plural = "Hazards"


class BackgroundExposureAssessmentInline(admin.TabularInline):
    model = BackgroundExposureAssessment
    autocomplete_fields = ["comp_of_interest"]
    extra = 1
    verbose_name_plural = "Nutrition"


class NovelFoodSynInline(admin.TabularInline):
    model = NovelFoodSyn
    extra = 1
    verbose_name_plural = "Novel/Traditional Food Identity"


class AllergenicityNovelFoodInline(admin.TabularInline):
    model = AllergenicityNovelFood
    extra = 1


class SubstanceOfConcernNovelFoodInline(admin.TabularInline):
    model = SubstanceOfConcernNovelFood
    autocomplete_fields = ["substance_of_concern"]
    extra = 0
    verbose_name_plural = "Hazards"


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


class SpeciesInline(admin.TabularInline):
    model = Species
    extra = 1
    autocomplete_fields = ["genus"]


class OrganismInline(admin.TabularInline):
    model = Organism
    extra = 1


class ChemDescriptorInline(admin.TabularInline):
    model = ChemDescriptor
    extra = 1


@admin.register(SynonymType)
class SynonymAdmin(admin.ModelAdmin):
    list_display = ["title"]


class HasContributor(admin.SimpleListFilter):
    title = "Opinion Contributor"
    parameter_name = "has_opinion_contributor"

    def lookups(self, request, model_admin):
        return (
            Contribution.objects.filter(opinion__isnull=False)
            .values_list("user__id", "user__first_name")
            .distinct()
        )

    def queryset(self, request, queryset):
        if self.value():
            # self.value() is the id of the selected contributor
            return queryset.filter(opinion__contributions__user__id=self.value())


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
            return queryset.filter(opinion__contributions__status=self.value())


@admin.register(NovelFood)
class NovelFoodAdmin(admin.ModelAdmin):
    list_display = [
        "nf_code",
        "title",
        "opinion_doi",
        "outcome",
        "get_contributions",
    ]
    list_display_links = ["nf_code", "title", "outcome", "get_contributions"]
    list_filter = ["outcome", HasContributor, HasContributorStatus]
    fieldsets = [
        (
            "GENERAL INFORMATION",
            {"fields": ["opinion", "title", "nf_code", "vocab_id"]},
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
            "NUTRITION",
            {
                "fields": [
                    "protein_digestibility",
                    "antinutritional_factors",
                    (
                        "has_nutri_disadvantage",
                        "nutri_disadvantage_explanation",
                    ),
                ],
            },
        ),
        (
            "TOXICOLOGY",
            {
                "fields": [
                    "tox_study_required",
                    "genotox_final_outcome",
                    "final_toxicology_remarks",
                ]
            },
        ),
        (
            "HAZARDS",
            {
                "fields": ["endocrine_disrupt_prop"],
            },
        ),
        (
            "CONCLUSION",
            {
                "fields": [("outcome", "outcome_remarks")],
            },
        ),
    ]

    def opinion_doi(self, obj):
        return obj.opinion.doi

    opinion_doi.short_description = "Opinion DOI"
    opinion_doi.admin_order_field = "opinion__doi"

    def get_contributions(self, obj):
        contributions = Contribution.objects.filter(opinion=obj.opinion)
        result = "<br>".join([str(contribution) for contribution in contributions])
        return format_html(result)

    get_contributions.short_description = "Opinion Contributions"

    search_fields = [
        "nf_code",
        "title",
        "vocab_id__short_name",
        "vocab_id__extended_name",
    ]
    autocomplete_fields = ["opinion", "shelflife_unit", "vocab_id"]
    inlines = [
        NovelFoodCategoryNovelFoodInline,
        NovelFoodSynInline,
        NovelFoodChemicalInline,
        NovelFoodOrganismInline,
        FoodCategoryNovelFoodInline,
        BackgroundExposureAssessmentInline,
        AllergenicityNovelFoodInline,
        SubstanceOfConcernNovelFoodInline,
        HBGVInline,
        SpecificToxicityInline,
    ]
    actions = [duplicate_model]


@admin.register(NovelFoodCategory)
class NovelFoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "regulation", "definition"]


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Allergenicity)
class AllergenicityAdmin(admin.ModelAdmin):
    list_display = ["title"]


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
            return queryset.filter(vocab_id__isnull=False)
        if self.value() == "No":
            return queryset.filter(vocab_id__isnull=True)


@admin.register(Organism)
class OrganismAdmin(admin.ModelAdmin):
    list_display = [
        "get_organism",
        "get_custom_species_name",
        "get_is_from_vocab",
    ]
    list_display_links = [
        "get_organism",
        "get_custom_species_name",
    ]
    fieldsets = [
        (
            "General Information",
            {
                "fields": [
                    "vocab_id",
                ]
            },
        ),
        (
            "Taxonomy Information",
            {
                "fields": [
                    "get_vocab_species_name",
                    "get_vocab_tax_path",
                    "get_custom_species_name",
                    "get_custom_tax_path",
                ]
            },
        ),
    ]
    readonly_fields = [
        "get_vocab_species_name",
        "get_vocab_tax_path",
        "get_custom_species_name",
        "get_custom_tax_path",
    ]
    autocomplete_fields = [
        "vocab_id",
    ]  # "genus"
    inlines = [SpeciesInline, OrganismSynInline]
    search_fields = ["vocab_id__short_name", "vocab_id__extended_name"]
    list_filter = [IsFromVocabFilter]
    actions = [duplicate_model]

    def get_is_from_vocab(self, obj):
        return obj.vocab_id is not None

    get_is_from_vocab.boolean = True
    get_is_from_vocab.short_description = "Is from Vocab"

    def get_organism(self, obj):
        return str(obj)

    get_organism.short_description = "Organism vocabulary identification"
    get_organism.admin_order_field = "vocab_id__short_name"

    def get_vocab_species_name(self, obj):
        if species_names := obj.vocab_id.implicit_attributes.filter(code="A01"):
            return "\n".join(sn.value for sn in species_names)
        else:
            return "NO DATA"

    get_vocab_species_name.short_description = (
        "Vocab Species Name or Vocab Scientific Name"
    )

    def get_vocab_tax_path(self, obj):
        if ancestors := obj.vocab_id.get_significant_ancestors():
            while len(ancestors) > 0 and ancestors[-1].code in [
                "A0C5X",
                "A0B8X",
                "root",
            ]:
                # we do not need to display "All Lists (A0C5X)", "Natural sources (A0B8X)"
                # and "root"
                ancestors = ancestors[:-1]
            res = ""
            for ancestor in ancestors:
                res += " < " + ancestor.name
            return res.lstrip(" < ")
        else:
            return "NO DATA"

    get_vocab_tax_path.short_description = "Vocab Taxonomy Path"

    def get_custom_species_name(self, obj):
        if species := obj.species.all():
            return "\n".join(
                f"{s.name} - {s.scientific_name}" if s.scientific_name else s.name
                for s in species
            )
        return "-"

    get_custom_species_name.short_description = (
        "Custom Species Name - Custom Scientific Name"
    )
    get_custom_species_name.admin_order_field = "species__name"

    def get_custom_tax_path(self, obj):
        species = obj.species.all()
        if not species:
            return "-"

        results = []
        for s in species:
            parts = [
                s.name if s.name else "",
                " - " if s.name and s.scientific_name else "",
                s.scientific_name if s.scientific_name else "",
                f" < {s.genus.title}" if s.genus else " < -",
                f" < {s.genus.family.title}" if s.genus.family else " < -",
                f" < {s.genus.family.org_type.title}"
                if s.genus.family.org_type
                else " < -",
            ]
            results.append("".join(parts))

        return "\n".join(results)

    get_custom_tax_path.short_description = "Custom Taxonomy Path"


@admin.register(OrgType)
class OrgTypeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ["title", "org_type"]
    search_fields = ["title"]
    list_filter = ["org_type"]


@admin.register(Genus)
class GenusAdmin(admin.ModelAdmin):
    list_display = ["title", "family"]
    search_fields = ["title"]
    list_filter = ["family"]
    autocomplete_fields = ["family"]


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ["name", "scientific_name", "genus"]
    search_fields = ["name", "scientific_name"]
    list_filter = ["genus"]
    autocomplete_fields = ["organism", "genus"]
    actions = [duplicate_model]


@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ["get_chemical", "get_iupac", "get_mol_form", "get_cas"]
    autocomplete_fields = ["vocab_id"]
    inlines = [ChemDescriptorInline, ChemicalSynInline]
    search_fields = ["vocab_id__short_name", "vocab_id__extended_name"]
    readonly_fields = [
        "get_iupac",
        "get_mol_form",
        "get_pest_class",
        "get_flavis_number",
        "get_detail_level",
        "get_smiles",
        "get_zoo_label",
        "get_cas",
        "get_ec_subinvent_entry_ref",
        "get_inchi",
        "get_category",
        "get_other_names",
    ]
    fieldsets = [
        (
            "General Information",
            {"fields": ["vocab_id"]},
        ),
        (
            "Final Descriptors (Custom Descriptors + Vocabulary Descriptors)",
            {
                "fields": [
                    "get_iupac",
                    "get_mol_form",
                    "get_cas",
                    "get_smiles",
                    "get_inchi",
                    "get_zoo_label",
                    "get_category",
                    "get_pest_class",
                    "get_detail_level",
                    "get_ec_subinvent_entry_ref",
                    "get_flavis_number",
                    "get_other_names",
                ]
            },
        ),
    ]
    actions = [duplicate_model]

    def get_chemical(self, obj):
        return str(obj)

    get_chemical.short_description = "Chemical vocabulary identification"
    get_chemical.admin_order_field = "vocab_id__short_name"

    @staticmethod
    def get_descriptors_to_display(custom_descriptors, obj_vocab_id, descriptor):
        descriptors = []
        if custom_descriptors.exists():
            descriptors.extend([descriptor.value for descriptor in custom_descriptors])
        if (
            obj_vocab_id
            and (
                vocab_descriptors := obj_vocab_id.implicit_attributes.filter(
                    code=descriptor
                )
            ).exists()
        ):
            descriptors.extend([attr.value for attr in vocab_descriptors])
        if not descriptors:
            return "NO DATA"
        return ", ".join(descriptors)

    def get_iupac(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.IUPAC.value),
            obj.vocab_id,
            Descriptor.IUPAC.value,
        )

    get_iupac.short_description = Descriptor.IUPAC.verbose

    def get_mol_form(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.MOLECULAR_FORMULA.value),
            obj.vocab_id,
            Descriptor.MOLECULAR_FORMULA.value,
        )

    get_mol_form.short_description = Descriptor.MOLECULAR_FORMULA.verbose

    def get_pest_class(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.PEST_CLASS.value),
            obj.vocab_id,
            Descriptor.PEST_CLASS.value,
        )

    get_pest_class.short_description = Descriptor.PEST_CLASS.verbose

    def get_flavis_number(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.FLAVIS_NUMBER.value),
            obj.vocab_id,
            Descriptor.FLAVIS_NUMBER.value,
        )

    get_flavis_number.short_description = Descriptor.FLAVIS_NUMBER.verbose

    def get_detail_level(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.DETAIL_LEVEL.value),
            obj.vocab_id,
            Descriptor.DETAIL_LEVEL.value,
        )

    get_detail_level.short_description = Descriptor.DETAIL_LEVEL.verbose

    def get_smiles(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.SMILES_NOTATION.value),
            obj.vocab_id,
            Descriptor.SMILES_NOTATION.value,
        )

    get_smiles.short_description = Descriptor.SMILES_NOTATION.verbose

    def get_zoo_label(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.ZOO_LABEL.value),
            obj.vocab_id,
            Descriptor.ZOO_LABEL.value,
        )

    get_zoo_label.short_description = Descriptor.ZOO_LABEL.verbose

    def get_cas(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.CAS.value),
            obj.vocab_id,
            Descriptor.CAS.value,
        )

    get_cas.short_description = Descriptor.CAS.verbose

    def get_ec_subinvent_entry_ref(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.COM_ECSUBINVENTENTRYREF.value),
            obj.vocab_id,
            Descriptor.COM_ECSUBINVENTENTRYREF.value,
        )

    get_ec_subinvent_entry_ref.short_description = (
        Descriptor.COM_ECSUBINVENTENTRYREF.verbose
    )

    def get_inchi(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.INCHI.value),
            obj.vocab_id,
            Descriptor.INCHI.value,
        )

    get_inchi.short_description = Descriptor.INCHI.verbose

    def get_category(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.CATEGORY.value),
            obj.vocab_id,
            Descriptor.CATEGORY.value,
        )

    get_category.short_description = Descriptor.CATEGORY.verbose

    def get_other_names(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.OTHER_NAMES.value),
            obj.vocab_id,
            Descriptor.OTHER_NAMES.value,
        )

    get_other_names.short_description = Descriptor.OTHER_NAMES.verbose


@admin.register(GenotoxFinalOutcome)
class GenotoxFinalOutcomeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
