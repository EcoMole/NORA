from administrative.models import Opinion
from django.db import models
from django.db.models import Q
from taxonomies.models import TaxonomyNode
from taxonomies.util import Descriptor


class Allergenicity(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_allergenicity")
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "ALLERGENICITY"
        verbose_name = "Allergenicity"
        verbose_name_plural = "📂 Allergenicity"


class AllergenicityNovelFood(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_allergenicity_novel_food")
    allergenicity = models.ForeignKey(
        Allergenicity,
        on_delete=models.CASCADE,
        db_column="id_allergenicity",
        verbose_name="Allergenicity",
    )
    novel_food = models.ForeignKey(
        "NovelFood",
        on_delete=models.CASCADE,
        db_column="id_study",
        verbose_name="Novel Food",
    )

    class Meta:
        db_table = "ALLERGENICITY_NOVEL_FOOD"
        verbose_name = "Allergenicity Assignment"
        verbose_name_plural = "Allergenicity Assignments"


class NutritionalDisadvantage(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_nutri_disadvantage")
    yes_no = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        db_column="is_yn",
        related_name="yes_no_nutritional_disadvantages",
        help_text="(YESNO vocab)",
    )
    explanation = models.CharField(max_length=2000, blank=True)

    def __str__(self) -> str:
        return f"{self.yes_no} - {self.explanation}"

    class Meta:
        db_table = "NUTRITIONAL_DISADVANTAGE"
        verbose_name = "Nutritional Disadvantage"


class Category(models.Model):
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=255, null=True, blank=True)
    regulation = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        # related_name="regulation_categories",
        db_column="id_regulation",
        limit_choices_to={"taxonomy__code": "LEGREF"},
        help_text="(LEGREF vocab)",
    )

    def __str__(self) -> str:
        return f"{self.regulation} : {self.title}"

    class Meta:
        db_table = "SUB_TYPE"
        verbose_name = "Novel Food Category"
        verbose_name_plural = "📂 NF Categories"


class NovelFoodCategory(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "STUDY_SUB_TYPE"
        verbose_name = "Novel Food Category"
        verbose_name_plural = "Novel Food Categories"


class FoodCategory(models.Model):
    # id_food_category = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        # db_table = "FOOD_CATEGORY"
        verbose_name = "Food category"
        verbose_name_plural = "📂 Food categories"


class SynonymType(models.Model):
    id_synonym_type = models.AutoField(primary_key=True)
    synonym_type = models.CharField(
        max_length=255,
        help_text="Type of synonym -e.g. common name, trade name, synonym",
    )
    definition = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.synonym_type

    class Meta:
        db_table = "SYNONYM"
        verbose_name = "Synonym Type"
        verbose_name_plural = "📂 Synonym types"


class NovelFoodSyn(models.Model):
    type = models.ForeignKey(SynonymType, on_delete=models.CASCADE)
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    novel_food_synonym = models.CharField(max_length=255)

    def __str__(self):
        return ""

    class Meta:
        db_table = "STUDY_SYN"
        verbose_name = "Novel food synonym"


class Type(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_type")
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "TYPE"
        verbose_name = "Type (taxonomy)"
        verbose_name_plural = "📂 Types (taxonomy)"


class Family(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_family")
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, db_column="id_type", null=True, blank=True
    )
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "FAMILY"
        verbose_name = "Family (taxonomy)"
        verbose_name_plural = "📂 Families (taxonomy)"


class Genus(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_genus")
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, db_column="id_family", null=True, blank=True
    )
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "GENUS"
        verbose_name = "Genus (taxonomy)"
        verbose_name_plural = "📂 Genera (taxonomy)"


class Organism(models.Model):
    organism_node = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "MTX"},
        help_text="(MTX vocab)",
    )
    species_title = models.CharField(max_length=255, null=True, blank=True)
    genus = models.ForeignKey(
        Genus, on_delete=models.CASCADE, null=True, blank=True, db_column="id_genus"
    )

    def __str__(self):
        if self.species_title:
            return self.species_title
        elif self.organism_node:
            return self.organism_node.name
        else:
            return None

    class Meta:
        db_table = "ORGANISM"
        verbose_name = "Organism"
        verbose_name_plural = "Organisms 🦠"


class OrganismSyn(models.Model):
    type = models.ForeignKey(SynonymType, on_delete=models.CASCADE)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    synonym = models.CharField(max_length=255)

    class Meta:
        db_table = "ORG_SYN"
        verbose_name = "Organism synonym"


class NovelFoodOrganism(models.Model):
    novel_food = models.ForeignKey(
        "NovelFood", on_delete=models.CASCADE, db_column="id_study"
    )
    organism = models.ForeignKey(
        Organism, on_delete=models.CASCADE, db_column="id_organism"
    )
    org_part = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="org_part_novel_foods",
        limit_choices_to={"taxonomy__code": "MTX"},
        # limit_choices_to=get_org_part_limit_choices,
        help_text="(MTX vocab)",
        db_column="id_org_part",
    )
    variant = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="STRAIN if microorganism / VARIETY if plant / "
        "SUBSPECIES if animal / CEll_TYPE if cell culture",
    )
    is_gmo = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="is_gmo_novel_foods",
        limit_choices_to={"taxonomy__code": "YESNO"},
        verbose_name="is GMO",
        db_column="id_is_gmo",
        help_text="Is the organism genetically modified? (YESNO vocab)",
    )
    has_qps = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="has_qps_novel_foods",
        limit_choices_to={"taxonomy__code": "YESNO"},
        verbose_name="has QPS",
        db_column="id_has_qps",
        help_text="Has qualified presumption of safety? (YESNO vocab)",
    )
    cell_culture = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="cell_culture_novel_foods",
        limit_choices_to={"taxonomy__code": "STRAIN"},
        db_column="id_cell_culture",
        help_text="(STRAIN vocab)",
    )
    is_cell_culture_modified = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="is_cell_culture_modified_novel_foods",
        limit_choices_to={"taxonomy__code": "YESNO"},
        verbose_name="is the cell culture modified",
        db_column="id_is_cell_culture_modified",
        help_text="Is the cell culture modified? (YESNO vocab)",
    )

    class Meta:
        db_table = "STUDY_ORG"
        verbose_name = "Organism Identity of Novel food"


def get_org_part_limit_choices():
    return Q(
        taxonomy__code="MTX",
        id__in=[
            obj.id
            for obj in TaxonomyNode.objects.filter(taxonomy__code="MTX")
            if "A16PR"
            in [ancestor.code for ancestor in obj.get_significant_ancestors()]
            # A16PR jsem dostal od Klárky jako node který je parentem všech organism parts.
            # Podle mě bych měl ale použít A0B8Y - "Part-nature" což je parentem toho nodu A16PR.
            # kouknout se jaké parenty maj nodes zmíněné v Combu které mám sepsány níže, jetli je "
            # parentem ten A0B8Y. (zjistím to pomocí n.get_significant_ancestors())
            # MTX catalogue, MTX ROOTs: Part-nature - 'A166E', 'A066N', 'A0CEG', 'A07XD', 'A0BA0'
            # id_plantPart = TaxonomyField(
            #     widget=TaxonomyWidget(
            #         "MTX",
            #         allowed_values=[
            #             "A166F",
            #             "A066V",
            #             "A066X",
            #             "A066Z",
            #             "A067A",
            #             "A166G",
            #             "A067B",
            #             "A166H",
            #             "A067D",
            #             "A166J",
            #             "A0EKT",
            #             "A0EKS",
            #             "A166K",
            #             "A067G",
            #             "A067D",
            #             "A0ESK",
            #             "A067M",
            #             "A066P",
            #             "A067T",
            #             "A067R",
            #             "A067S",
            #             "A166L",
            #             "A166M",
            #             "A166N",
            #             "A0F5F",
            #             "A07XD",
            #             "A0BA0",
            #             "A166P",
            #         ],
            #     ),
            #     required=False,
            # )
        ],
    )


class NovelFoodChemical(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    chemical = models.ForeignKey("Chemical", on_delete=models.CASCADE)

    class Meta:
        db_table = "STUDY_COM"
        verbose_name = "Chemical identity of Novel food"


# For possible future use only
class ChemicalType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_component_type")
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=2000, null=True, blank=True)

    class Meta:
        db_table = "COM_TYPE"
        verbose_name = "Chemical type (future use)"
        verbose_name_plural = "📂 Chemical types (future use)"


# For possible future use only
class StructureReported(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_structure_reported")
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=2000, null=True, blank=True)

    class Meta:
        db_table = "COM_STRUCTURE_SHOWN"
        verbose_name = "Structure reported (future use)"
        verbose_name_plural = "📂 Structures reported (future use)"


class Chemical(models.Model):
    id_chemical = models.AutoField(primary_key=True, db_column="id_component")
    catalogue_identity = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="catalogue_identity_chemicals",
        limit_choices_to={"taxonomy__code": "PARAM"},
        help_text="(PARAM vocab)",
    )

    chemical_type = models.ForeignKey(
        ChemicalType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column="component_type",
        help_text="The majority of the chemical types are extracted from the OECD picklist"
        "(OECD 2012). More on the purpose of this field: 2013:EN-458 page:20",
    )
    structure_reported = models.ForeignKey(
        StructureReported,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text="This field is used to indicate what type of structure (either SMILES or InChI) "
        "is reported. For example: the structure of the compound itself, the structure of "
        "the monomer if the compound is a polymer, the structure of an isomer, or "
        "no structure at all.",
    )

    def __str__(self):
        return self.catalogue_identity.name if self.catalogue_identity else None

    class Meta:
        db_table = "COMPONENT"
        verbose_name = "Chemicals"
        verbose_name_plural = "Chemicals 🧪"


class ChemDescriptor(models.Model):
    TYPE_CHOICES = [
        (
            Descriptor.OTHER_NAMES.value,
            Descriptor.OTHER_NAMES.verbose,
        ),
        (Descriptor.IUPAC.value, Descriptor.IUPAC.verbose),
        (
            Descriptor.MOLECULAR_FORMULA.value,
            Descriptor.MOLECULAR_FORMULA.verbose,
        ),
        (Descriptor.CAS.value, Descriptor.CAS.verbose),
        (
            Descriptor.SMILES_NOTATION.value,
            Descriptor.SMILES_NOTATION.verbose,
        ),
        (Descriptor.INCHI.value, Descriptor.INCHI.verbose),
        (Descriptor.ZOO_LABEL.value, Descriptor.ZOO_LABEL.verbose),
        (Descriptor.CATEGORY.value, Descriptor.CATEGORY.verbose),
        (Descriptor.PEST_CLASS.value, Descriptor.PEST_CLASS.verbose),
        (
            Descriptor.DETAIL_LEVEL.value,
            Descriptor.DETAIL_LEVEL.verbose,
        ),
        (
            Descriptor.COM_ECSUBINVENTENTRYREF.value,
            Descriptor.COM_ECSUBINVENTENTRYREF.verbose,
        ),
        (
            Descriptor.FLAVIS_NUMBER.value,
            Descriptor.FLAVIS_NUMBER.verbose,
        ),
    ]
    id = models.AutoField(primary_key=True, db_column="id_chem_descriptor")
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    value = models.CharField(max_length=255)
    chemical = models.ForeignKey(
        Chemical, on_delete=models.CASCADE, related_name="chem_descriptors"
    )

    class Meta:
        db_table = "CHEM_DESCRIPTOR"
        verbose_name = "Custom Descriptor"


class ChemicalSyn(models.Model):
    type = models.ForeignKey(SynonymType, on_delete=models.CASCADE)
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    synonym = models.CharField(max_length=255)

    class Meta:
        db_table = "COM_SYN"
        verbose_name = "Chemical synonym"


class SubstanceOfConcernNovelFood(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    substance_of_concern = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="substance_of_concern_substance_of_concern_novel_foods",
        limit_choices_to={"taxonomy__code": "PARAM"},
        db_column="id_sub_of_concern",
        help_text="(PARAM vocab)",
    )

    class Meta:
        db_table = "SUBSTANCE_OF_CONCERN_STUDY"
        verbose_name = "Substance of concern"
        verbose_name_plural = "Substances of concern"


class GenotoxFinalOutcome(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_genotox_final_outcome")
    title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "GENOTOX_FINAL_OUTCOME"
        verbose_name = "Genotoxicity final outcome"
        verbose_name_plural = "Genotoxicity final outcomes"


class NovelFood(models.Model):
    OUTCOME_CHOICES = [
        ("negative", "Negative"),
        ("partially_negative", "Partially Negative"),
        ("positive", "Positive"),
    ]

    # general info
    id = models.AutoField(primary_key=True, db_column="id_study")
    opinion = models.ForeignKey(
        Opinion,
        on_delete=models.SET_NULL,
        db_column="id_op",
        related_name="opinion_novel_foods",
        null=True,
    )
    title = models.CharField(max_length=255, blank=False, verbose_name="NF Name")
    nf_code = models.CharField(
        max_length=2000, verbose_name="NF Code", null=True, blank=True
    )

    food_category = models.ForeignKey(
        FoodCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        db_column="id_food_category",
        related_name="food_category_novel_foods",
    )
    # toxicity
    specific_toxicity = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        db_column="id_toxicity",
        verbose_name="Specific Toxicity",
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "TOXICITY"},
        related_name="specific_toxicity_novel_foods",
        help_text="if novel food has specific toxicity, specify which one. (TOXICITY vocab)",
    )
    tox_study_required = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        db_column="id_tox_study_required",
        verbose_name="Tox study required",
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        related_name="tox_study_required_novel_foods",
        help_text="(YESNO vocab)",
    )
    mutagenicity = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        db_column="id_is_mutagenic",
        verbose_name="Mutagenicity",
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        related_name="mutagenicity_novel_foods",
        help_text="(YESNO vocab)",
    )
    carcinogenicity = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        db_column="id_is_carcinogenic",
        verbose_name="Carcinogenicity",
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        related_name="carcinogenicity_novel_foods",
        help_text="(YESNO vocab)",
    )
    genotox_final_outcome = models.ForeignKey(
        GenotoxFinalOutcome,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        db_column="id_is_genotoxic",
        related_name="genotox_final_outcome_novel_foods",
    )
    # nutrition
    protein_digestibility = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        db_column="id_protein_digestibility",
        verbose_name="Protein digestibility",
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        related_name="protein_digestibility_novel_foods",
        help_text="(YESNO vocab)",
    )
    antinutritional_factors = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        db_column="id_antinutritional_factors",
        verbose_name="Antinutritional factors",
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        related_name="antinutritional_factors_novel_foods",
        help_text="(YESNO vocab)",
    )
    nutritional_disadvantage = models.OneToOneField(
        NutritionalDisadvantage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        db_column="id_nutri_disadvantage",
        related_name="nutritional_disadvantage_novel_foods",
    )
    # stability
    sufficient_data = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        db_column="id_is_sufficient_data",
        related_name="sufficient_data_novel_foods",
        help_text="Were sufficient data provided? (YESNO vocab)",
    )

    food_matrices = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        db_column="id_is_food_matrices",
        help_text="Were food matrices provided? (YESNO vocab)",
        related_name="food_matrices_novel_foods",
    )
    instability_concerns = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        db_column="id_instability_concerns",
        related_name="instability_concerns_novel_foods",
        help_text="(YESNO vocab)",
    )
    shelflife_value = models.FloatField(blank=True, null=True)
    shelflife_unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "UNIT"},
        db_column="id_shelflife_unit",
        related_name="shelflife_unit_novel_foods",
        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
    )
    endocrine_disrupt_prop = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        db_column="id_has_endocrine_disrupt_prop",
        verbose_name="has endocrine disrupt properties",
        related_name="endocrine_disrupt_prop_novel_foods",
        help_text="(YESNO vocab)",
    )
    outcome = models.CharField(
        max_length=255, blank=True, null=True, choices=OUTCOME_CHOICES
    )
    outcome_remarks = models.CharField(
        max_length=2000,
        blank=True,
        null=True,
        help_text="explanation in case the Outcome is 'Partially Negative'",
    )

    catalogue_identity = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "PARAM"},
        db_column="id_rms_efsa",
        related_name="catalogue_identity_novel_foods",
        help_text="(PARAM vocab)",
    )

    # django specific fields to get the models well tied together
    allergenicity = models.ManyToManyField(
        "Allergenicity",
        through="AllergenicityNovelFood",
        related_name="allergenicity_novel_foods",
    )

    def __str__(self) -> str:
        nf_code_part = f"{self.nf_code} - " if self.nf_code else ""
        return nf_code_part + self.title

    class Meta:
        db_table = "STUDY"
        verbose_name = "Novel Food"
        verbose_name_plural = "Novel Foods 🥬"


class BackgroundExposureAssessment(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_bg_exp_assessment")
    novel_food = models.ForeignKey(
        NovelFood,
        on_delete=models.CASCADE,
        related_name="novel_food_bg_expo_assessments",
        db_column="id_study",
    )
    comp_of_interest = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="comp_of_interest_bg_expo_assessments",
        db_column="id_comp_of_interest",
        limit_choices_to={"taxonomy__code": "PARAM"},
        help_text="Compound of interest (PARAM vocab)",
    )

    def __str__(self) -> str:
        return ""

    class Meta:
        db_table = "BG_EXPO_ASSESSMENT"
        verbose_name = "Background exposure assessment"


class HBGV(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_hbgv")
    novel_food = models.ForeignKey(
        NovelFood,
        on_delete=models.CASCADE,
        related_name="novel_food_hbgvs",
        db_column="id_study",
    )
    type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="type_hbgvs",
        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
        db_column="id_type",
        help_text="(ENDPOINT_HGV vocab)",
    )
    substance = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="substance_hbgvs",
        limit_choices_to={"taxonomy__code": "PARAM"},
        db_column="id_substance",
        help_text="(PARAM vocab)",
    )
    exceeded_for_population = models.ForeignKey(
        "taxonomies.Population",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="population_hbgvs",
        db_column="id_age",
        help_text="Population for which the HBGV is exceeded",
    )

    def __str__(self):
        return f"{self.novel_food.title} - {self.substance.name} - {self.type.name}"

    class Meta:
        verbose_name = "Health-Based Guidence Value"
        verbose_name_plural = "Health-Based Guidence Values"
