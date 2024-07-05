from core.models import Contribution
from django.contrib import admin
from novel_food.models import (
    HBGV,
    Allergenicity,
    AllergenicityNovelFood,
    BackgroundExposureAssessment,
    ChemDescriptor,
    Chemical,
    ChemicalSyn,
    ChemicalType,
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
    StructureReported,
    SubstanceOfConcernNovelFood,
    SynonymType,
)
from taxonomies.util import Descriptor
from util.admin_utils import duplicate_model


class NovelFoodCategoryNovelFoodInline(admin.TabularInline):
    model = NovelFoodCategoryNovelFood
    extra = 1


class FoodCategoryNovelFoodInline(admin.TabularInline):
    model = FoodCategoryNovelFood
    extra = 1


class NovelFoodChemicalInline(admin.TabularInline):
    model = NovelFoodChemical
    extra = 1
    autocomplete_fields = ["chemical"]


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


class HBGVInline(admin.TabularInline):
    model = HBGV
    autocomplete_fields = ["type", "novel_food", "exceeded", "substance"]
    extra = 1


class BackgroundExposureAssessmentInline(admin.TabularInline):
    model = BackgroundExposureAssessment
    autocomplete_fields = ["comp_of_interest"]
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
    extra = 0


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


@admin.register(NovelFood)
class NovelFoodAdmin(admin.ModelAdmin):
    list_display = [
        "nf_code",
        "title",
        "opinion_doi",
        "outcome",
        "responsible_person",
        "status",
    ]
    list_display_links = ["nf_code", "title", "outcome", "responsible_person", "status"]
    fieldsets = [
        (
            "General Information",
            {"fields": ["opinion", "title", "nf_code", "vocab_id"]},
        ),
        (
            "TOXICOLOGY",
            {
                "fields": [
                    "tox_study_required",
                    "genotox_final_outcome",
                    "specific_toxicity",
                    "final_toxicology_remarks",
                ]
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
    ]

    def opinion_doi(self, obj):
        return obj.opinion.doi

    opinion_doi.short_description = "Opinion DOI"

    def responsible_person(self, obj):
        contribution = Contribution.objects.filter(opinion=obj.opinion).first()
        if contribution:
            user = contribution.user
            return user.first_name

    responsible_person.short_description = "Responsible Person"

    def status(self, obj):
        contribution = Contribution.objects.filter(opinion=obj.opinion).first()
        if contribution:
            return contribution.status

    status.short_description = "Status"

    search_fields = [
        "nf_code",
        "title",
        "vocab_id__short_name",
        "vocab_id__extended_name",
    ]
    autocomplete_fields = ["opinion", "shelflife_unit", "vocab_id", "specific_toxicity"]
    inlines = [
        SubstanceOfConcernNovelFoodInline,
        NovelFoodSynInline,
        FoodCategoryNovelFoodInline,
        NovelFoodCategoryNovelFoodInline,
        NovelFoodChemicalInline,
        NovelFoodOrganismInline,
        BackgroundExposureAssessmentInline,
        HBGVInline,
        AllergenicityNovelFoodInline,
    ]
    actions = [duplicate_model]


@admin.register(NovelFoodCategory)
class NovelFoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "regulation", "definition"]


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "definition"]


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
        "get_is_from_vocab",
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
        return obj.vocab_id.name

    get_organism.short_description = "Species"

    def get_vocab_species_name(self, obj):
        if species_names := obj.vocab_id.implicit_attributes.filter(code="A01"):
            return "\n".join(sn.value for sn in species_names)
        else:
            return "😢"

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
            return "😢"

    get_vocab_tax_path.short_description = "Vocab Taxonomy Path"

    def get_custom_species_name(self, obj):
        if species := obj.species_set.all():
            return "\n".join(
                f"{s.name} - {s.scientific_name}" if s.scientific_name else s.name
                for s in species
            )
        return "-"

    get_custom_species_name.short_description = (
        "Custom Species Name - Custom Scientific Name"
    )

    def get_custom_tax_path(self, obj):
        species = obj.species_set.all()
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
    list_display = ["vocab_id", "get_iupac", "get_mol_form", "get_cas"]
    autocomplete_fields = ["vocab_id"]
    inlines = [ChemDescriptorInline, ChemicalSynInline]
    search_fields = ["vocab_id"]
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

    @staticmethod
    def get_descriptors_to_display(custom_descriptors, vocab_descriptors):
        result = ""
        if custom_descriptors.exists():
            for descriptor in custom_descriptors:
                result += descriptor.value + ", "
        if vocab_descriptors.exists():
            for attr in vocab_descriptors:
                result += attr.value + ", "
        if result == "":
            return "😢"
        else:
            return result[:-2]

    def get_iupac(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.IUPAC.value),
            obj.vocab_id.implicit_attributes.filter(code=Descriptor.IUPAC.value),
        )

    get_iupac.short_description = Descriptor.IUPAC.verbose

    def get_mol_form(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.MOLECULAR_FORMULA.value),
            obj.vocab_id.implicit_attributes.filter(
                code=Descriptor.MOLECULAR_FORMULA.value
            ),
        )

    get_mol_form.short_description = Descriptor.MOLECULAR_FORMULA.verbose

    def get_pest_class(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.PEST_CLASS.value),
            obj.vocab_id.implicit_attributes.filter(code=Descriptor.PEST_CLASS.value),
        )

    get_pest_class.short_description = Descriptor.PEST_CLASS.verbose

    def get_flavis_number(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.FLAVIS_NUMBER.value),
            obj.vocab_id.implicit_attributes.filter(
                code=Descriptor.FLAVIS_NUMBER.value
            ),
        )

    get_flavis_number.short_description = Descriptor.FLAVIS_NUMBER.verbose

    def get_detail_level(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.DETAIL_LEVEL.value),
            obj.vocab_id.implicit_attributes.filter(code=Descriptor.DETAIL_LEVEL.value),
        )

    get_detail_level.short_description = Descriptor.DETAIL_LEVEL.verbose

    def get_smiles(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.SMILES_NOTATION.value),
            obj.vocab_id.implicit_attributes.filter(
                code=Descriptor.SMILES_NOTATION.value
            ),
        )

    get_smiles.short_description = Descriptor.SMILES_NOTATION.verbose

    def get_zoo_label(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.ZOO_LABEL.value),
            obj.vocab_id.implicit_attributes.filter(code=Descriptor.ZOO_LABEL.value),
        )

    get_zoo_label.short_description = Descriptor.ZOO_LABEL.verbose

    def get_cas(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.CAS.value),
            obj.vocab_id.implicit_attributes.filter(code=Descriptor.CAS.value),
        )

    get_cas.short_description = Descriptor.CAS.verbose

    def get_ec_subinvent_entry_ref(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.COM_ECSUBINVENTENTRYREF.value),
            obj.vocab_id.implicit_attributes.filter(
                code=Descriptor.COM_ECSUBINVENTENTRYREF.value
            ),
        )

    get_ec_subinvent_entry_ref.short_description = (
        Descriptor.COM_ECSUBINVENTENTRYREF.verbose
    )

    def get_inchi(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.INCHI.value),
            obj.vocab_id.implicit_attributes.filter(code=Descriptor.INCHI.value),
        )

    get_inchi.short_description = Descriptor.INCHI.verbose

    def get_category(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.CATEGORY.value),
            obj.vocab_id.implicit_attributes.filter(code=Descriptor.CATEGORY.value),
        )

    get_category.short_description = Descriptor.CATEGORY.verbose

    def get_other_names(self, obj):
        return self.get_descriptors_to_display(
            obj.chem_descriptors.filter(type=Descriptor.OTHER_NAMES.value),
            obj.vocab_id.implicit_attributes.filter(code=Descriptor.OTHER_NAMES.value),
        )

    get_other_names.short_description = Descriptor.OTHER_NAMES.verbose


@admin.register(ChemicalType)
class ChemicalTypeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    list_filter = ["title"]


@admin.register(StructureReported)
class StructureReportedAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    list_filter = ["title"]


@admin.register(GenotoxFinalOutcome)
class GenotoxFinalOutcomeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
