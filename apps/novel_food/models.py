from administrative.models import Opinion
from django.db import models
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
        related_name="allergenicities",
    )

    class Meta:
        db_table = "ALLERGENICITY_NOVEL_FOOD"
        verbose_name = "Allergenicity"
        verbose_name_plural = "Allergenicity"


class FoodCategory(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_food_category")
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "FOOD_CATEGORY"
        verbose_name = "Food Category"
        verbose_name_plural = "📂 Food Categories"


class FoodCategoryNovelFood(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_food_category_study")
    food_category = models.ForeignKey(
        FoodCategory, on_delete=models.CASCADE, db_column="id_food_category"
    )
    novel_food = models.ForeignKey(
        "NovelFood",
        on_delete=models.CASCADE,
        db_column="id_study",
        related_name="food_categories",
    )

    def __str__(self) -> str:
        nf_code_part = (
            f" ({self.novel_food.nf_code})" if self.novel_food.nf_code else ""
        )
        return (
            self.food_category.title + " - " + f"{self.novel_food.title}{nf_code_part}"
        )

    class Meta:
        db_table = "STUDY_FOOD_CATEGORY"
        verbose_name = "Food Category of Novel Food"
        verbose_name_plural = "Food Categories"
        constraints = [
            models.UniqueConstraint(
                fields=["novel_food", "food_category"],
                name="unique_food_category_novel_food",
            ),
        ]


class NovelFoodCategory(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_sub_type")
    title = models.CharField(max_length=255, db_column="sub_type")
    definition = models.TextField(null=True, blank=True)
    regulation = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        # related_name="regulation_categories",
        db_column="id_regulation",
        limit_choices_to=models.Q(taxonomy__code="LEGREF")
        & ~models.Q(short_name="root"),
        help_text="(LEGREF vocab)",
    )

    def __str__(self) -> str:
        regulation_part = f"{self.regulation.name} : " if self.regulation else ""
        return regulation_part + self.title

    class Meta:
        db_table = "SUB_TYPE"
        verbose_name = "Novel Food Category"
        verbose_name_plural = "📂 Novel Food Categories"


class NovelFoodCategoryNovelFood(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_sub_type_study")
    novel_food = models.ForeignKey(
        "NovelFood",
        on_delete=models.CASCADE,
        db_column="id_study",
        related_name="novel_food_categories",
    )
    novel_food_category = models.ForeignKey(
        NovelFoodCategory, on_delete=models.CASCADE, db_column="id_sub_type"
    )

    def __str__(self) -> str:
        nf_code_part = (
            f" ({self.novel_food.nf_code})" if self.novel_food.nf_code else ""
        )
        return (
            self.novel_food_category.title
            + " - "
            + f"{self.novel_food.title}{nf_code_part}"
        )

    class Meta:
        db_table = "STUDY_SUB_TYPE"
        verbose_name = "Novel Food Category of Novel Food"
        verbose_name_plural = "Novel Food Categories"
        constraints = [
            models.UniqueConstraint(
                fields=["novel_food", "novel_food_category"],
                name="unique_novel_food_category_novel_food",
            ),
        ]


class SynonymType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_syn")
    title = models.CharField(
        max_length=255,
        help_text="Title of the synonym type e.g. common name, trade name, synonym",
        db_column="synonym",
    )
    definition = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "SYNONYM"
        verbose_name = "Synonym Type"
        verbose_name_plural = "📂 Synonym types"


class NovelFoodSyn(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_study_syn")
    syn_type = models.ForeignKey(
        SynonymType,
        on_delete=models.CASCADE,
        db_column="id_syn",
        verbose_name="Synonym Type",
    )
    novel_food = models.ForeignKey(
        "NovelFood",
        on_delete=models.CASCADE,
        db_column="id_study",
        related_name="synonyms",
    )
    title = models.CharField(max_length=255, db_column="study_syn")

    def __str__(self):
        return ""

    class Meta:
        db_table = "STUDY_SYN"
        verbose_name = "Novel food synonym"


class OrgType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_org_type")
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "ORG_TYPE"
        verbose_name = "Organism Type (custom taxonomy)"
        verbose_name_plural = "📂 Organism Types (custom taxonomy)"


class Family(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_family")
    org_type = models.ForeignKey(
        OrgType,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        db_column="id_org_type",
        verbose_name="Organism Type",
    )
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "FAMILY"
        verbose_name = "Family (custom taxonomy)"
        verbose_name_plural = "📂 Families (custom taxonomy)"


class Genus(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_genus")
    family = models.ForeignKey(
        Family, on_delete=models.SET_NULL, null=True, blank=False, db_column="id_family"
    )
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "GENUS"
        verbose_name = "Genus (custom taxonomy)"
        verbose_name_plural = "📂 Genera (custom taxonomy)"


class Organism(models.Model):
    duplicate_related = ["species", "synonyms"]

    id = models.AutoField(primary_key=True, db_column="id_org")
    vocab_id = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(taxonomy__code="MTX")
        & (
            models.Q(extended_name__icontains="(as animal)")
            | models.Q(extended_name__icontains="(as organism)")
            | models.Q(extended_name__icontains="(as plant)")
            | models.Q(short_name__icontains="(as animal)")
            | models.Q(short_name__icontains="(as organism)")
            | models.Q(short_name__icontains="(as plant)")
        ),
        help_text="(MTX vocab) - only records with '(as animal)' or '(as plant)' or "
        "'(as organism)' in the name are allowed",
        related_name="vocab_id_organisms",
        verbose_name="Organism vocabulary identification",
        db_column="id_organism",
    )

    def __str__(self):
        return (
            self.vocab_id.name
            if self.vocab_id
            else "MISSING ORGANISM VOCABULARY IDENTIFICATION"
        )

    class Meta:
        db_table = "ORGANISM"
        verbose_name = "Organism"
        verbose_name_plural = "📂 ORGANISMS"


class OrganismSyn(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_org_syn")
    syn_type = models.ForeignKey(
        SynonymType,
        on_delete=models.CASCADE,
        db_column="id_syn",
        verbose_name="Synonym Type",
    )
    organism = models.ForeignKey(
        Organism, on_delete=models.CASCADE, db_column="id_org", related_name="synonyms"
    )
    title = models.CharField(max_length=255, db_column="org_syn")

    class Meta:
        db_table = "ORG_SYN"
        verbose_name = "Organism synonym"


class Species(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_spec")
    name = models.CharField(max_length=255, unique=True, verbose_name="Species Name")
    scientific_name = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Scientific Name",
    )
    organism = models.ForeignKey(
        Organism,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        db_column="id_org",
        related_name="species",
    )
    genus = models.ForeignKey(
        Genus, on_delete=models.SET_NULL, null=True, blank=False, db_column="id_genus"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "SPECIES"
        verbose_name = "Species (custom taxonomy)"
        verbose_name_plural = "📂 Species (custom taxonomy)"


class NovelFoodOrganism(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_study_organism")
    novel_food = models.ForeignKey(
        "NovelFood",
        on_delete=models.CASCADE,
        db_column="id_study",
        related_name="organisms",
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
        limit_choices_to=models.Q(taxonomy__code="MTX")
        & ~models.Q(short_name="root")
        & models.Q(is_part_nature=True),
        help_text="(MTX vocab)",
        db_column="id_org_part",
        verbose_name="organism part",
    )
    variant = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="STRAIN if microorganism / VARIETY if plant / "
        "SUBSPECIES if animal",
    )
    is_gmo = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="is_gmo_novel_foods",
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
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
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
        verbose_name="has QPS",
        db_column="id_has_qps",
        help_text="Has qualified presumption of safety? applies only if the organism is a "
        "microorganism. (YESNO vocab)",
    )
    cell_culture = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Cell Type (Cell Culture)"
    )
    cells_modified = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="cells_modified_novel_foods",
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
        verbose_name="Cells Modified? (Cell Culture)",
        db_column="id_cells_modified",
        help_text="(YESNO vocab)",
    )

    class Meta:
        db_table = "STUDY_ORG"
        verbose_name = "Organism Identity of Novel food"
        verbose_name_plural = "Organism Identities"


class NovelFoodChemical(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_study_com")
    novel_food = models.ForeignKey(
        "NovelFood",
        on_delete=models.CASCADE,
        db_column="id_study",
        related_name="chemicals",
    )
    chemical = models.ForeignKey(
        "Chemical", on_delete=models.CASCADE, db_column="id_com"
    )

    class Meta:
        db_table = "STUDY_COM"
        verbose_name = "Chemical Identity of Novel Food"
        verbose_name_plural = "Chemical Identities"


class Chemical(models.Model):
    duplicate_related = ["chem_descriptors", "synonyms"]

    id = models.AutoField(primary_key=True, db_column="id_com")
    vocab_id = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        db_column="id_rnc_efsa",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="vocab_id_chemicals",
        limit_choices_to=models.Q(taxonomy__code="PARAM")
        & ~models.Q(short_name="root"),
        help_text="(PARAM vocab)",
        verbose_name="Chemical vocabulary identification",
    )

    def __str__(self):
        return (
            self.vocab_id.name
            if self.vocab_id
            else "MISSING CHEMICAL VOCABULARY IDENTIFICATION"
        )

    class Meta:
        db_table = "COMPONENT"
        verbose_name = "Chemicals"
        verbose_name_plural = "📂 CHEMICALS"


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
    id = models.AutoField(primary_key=True, db_column="id_com_descriptor")
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    value = models.CharField(
        max_length=255,
        verbose_name="Descriptor",
        help_text="contains e.g. the molecular formula itself if type is 'Molecular Formula', etc.",
    )
    chemical = models.ForeignKey(
        Chemical,
        on_delete=models.CASCADE,
        related_name="chem_descriptors",
        db_column="id_com",
    )

    class Meta:
        db_table = "COM_DESCRIPTOR"
        verbose_name = "Custom Descriptor"


class ChemicalSyn(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_com_syn")
    syn_type = models.ForeignKey(
        SynonymType,
        on_delete=models.CASCADE,
        db_column="id_syn",
        verbose_name="Synonym Type",
    )
    chemical = models.ForeignKey(
        Chemical, on_delete=models.CASCADE, db_column="id_com", related_name="synonyms"
    )
    title = models.CharField(max_length=255, db_column="com_syn")

    class Meta:
        db_table = "COM_SYN"
        verbose_name = "Chemical synonym"


class SubstanceOfConcernNovelFood(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_sub_of_concern_study")
    novel_food = models.ForeignKey(
        "NovelFood",
        on_delete=models.CASCADE,
        db_column="id_study",
        related_name="substances_of_concern",
    )
    substance_of_concern = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="substance_of_concern_substance_of_concern_novel_foods",
        limit_choices_to=models.Q(taxonomy__code="PARAM")
        & ~models.Q(short_name="root"),
        db_column="id_sub_of_concern",
        help_text="Fill only if there is a substance of concern, if not leave blank. (PARAM vocab)",
    )

    class Meta:
        db_table = "SUBSTANCE_OF_CONCERN_STUDY"
        verbose_name = "Hazard - Substance of concern"
        verbose_name_plural = "Hazard - Substances of concern"


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
    TOX_STUDY_REQUIRED_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
        ("no_new_data_added", "No new data added"),
    ]
    duplicate_related = [
        "substances_of_concern",
        "hbgvs",
        "bg_expo_assessments",
        "chemicals",
        "organisms",
        "synonyms",
        "novel_food_categories",
        "food_categories",
        "allergenicities",
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
        max_length=255, verbose_name="NF Code", null=True, blank=True
    )

    # toxicity
    tox_study_required = models.CharField(
        choices=TOX_STUDY_REQUIRED_CHOICES,
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Toxicology Required",
    )
    genotox_final_outcome = models.ForeignKey(
        GenotoxFinalOutcome,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        db_column="id_is_genotoxic",
        related_name="genotox_final_outcome_novel_foods",
        verbose_name="Genotoxicity Final Outcome",
    )
    final_toxicology_remarks = models.TextField(
        blank=True,
        null=True,
        help_text="Final toxicology assessment for all the toxicology studies",
    )
    # nutrition
    protein_digestibility = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        db_column="id_protein_digestibility",
        verbose_name="Protein digestibility",
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
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
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
        related_name="antinutritional_factors_novel_foods",
        help_text="(YESNO vocab)",
    )
    has_nutri_disadvantage = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        db_column="id_has_nutri_disadvantage",
        verbose_name="Nutritionally Disadvantageous",
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
        related_name="has_nutri_disadvantage_novel_foods",
        help_text="(YESNO vocab)",
    )
    nutri_disadvantage_explanation = models.TextField(
        blank=True,
        null=True,
        verbose_name="Reason For Disadvantage",
        help_text="explanation in case the Novel Food has a nutritional disadvantage",
    )

    # stability
    sufficient_data = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
        db_column="id_is_sufficient_data",
        related_name="sufficient_data_novel_foods",
        help_text="Were sufficient data provided? (YESNO vocab)",
    )

    food_matrices = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
        db_column="id_is_food_matrices",
        help_text="Were food matrices provided? (YESNO vocab)",
        related_name="food_matrices_novel_foods",
    )
    instability_concerns = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
        db_column="id_instability_concerns",
        related_name="instability_concerns_novel_foods",
        help_text="(YESNO vocab)",
    )
    shelflife_value = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Shelf Life Value",
    )
    shelflife_unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(taxonomy__code="UNIT")
        & models.Q(extended_name__in=["Hour", "Day", "Week", "Month", "Year"]),
        db_column="id_shelflife_unit",
        related_name="shelflife_unit_novel_foods",
        verbose_name="Shelf Life Unit",
        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
    )
    endocrine_disrupt_prop = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
        db_column="id_has_endocrine_disrupt_prop",
        verbose_name="Endocrine Disrupting Properties",
        related_name="endocrine_disrupt_prop_novel_foods",
        help_text="(YESNO vocab)",
    )
    outcome = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=OUTCOME_CHOICES,
        verbose_name="Opinion Outcome",
    )
    outcome_remarks = models.TextField(
        blank=True,
        null=True,
        help_text="explanation in case the Outcome is 'Negative' or 'Partially Negative'",
    )

    vocab_id = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(taxonomy__code="PARAM")
        & ~models.Q(short_name="root"),
        db_column="id_rms_efsa",
        related_name="vocab_id_novel_foods",
        verbose_name="NovelFood Vocabulary Identification",
        help_text="If missing in vocabulary, move on, do not add into vocab. (PARAM vocab)",
    )

    # django specific fields to get the models well tied together
    allergenicity = models.ManyToManyField(
        "Allergenicity",
        through="AllergenicityNovelFood",
        related_name="allergenicity_novel_foods",
    )

    def __str__(self) -> str:
        nf_code_part = f" ({self.nf_code})" if self.nf_code else ""
        return self.title + nf_code_part

    class Meta:
        db_table = "STUDY"
        verbose_name = "Novel Food 🥬"
        verbose_name_plural = "Novel Foods 🥬"


class SpecificToxicity(models.Model):
    specific_toxicity = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=False,
        blank=False,
        db_column="id_toxicity",
        verbose_name="Specific Toxicity",
        on_delete=models.CASCADE,
        limit_choices_to=models.Q(taxonomy__code="TOXICITY")
        & ~models.Q(short_name="root"),
        related_name="novel_foods",
        help_text="if novel food has specific toxicity, specify which one. (TOXICITY vocab)",
    )
    novel_food = models.ForeignKey(
        NovelFood,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="specific_toxicities",
    )

    def __str__(self):
        return str(self.novel_food) + " - " + str(self.specific_toxicity)

    class Meta:
        db_table = "SPECIFIC_TOXICITY"
        verbose_name = "Hazard - Specific Toxicity"
        verbose_name_plural = "Hazard - Specific Toxicities"
        constraints = [
            models.UniqueConstraint(
                fields=["novel_food", "specific_toxicity"],
                name="unique_specific_toxicity_novel_food",
            ),
        ]


class BackgroundExposureAssessment(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_bg_exp_assessment")
    novel_food = models.ForeignKey(
        NovelFood,
        on_delete=models.CASCADE,
        related_name="bg_expo_assessments",
        db_column="id_study",
    )
    comp_of_interest = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="comp_of_interest_bg_expo_assessments",
        db_column="id_comp_of_interest",
        limit_choices_to=models.Q(taxonomy__code="PARAM")
        & ~models.Q(short_name="root"),
        help_text="Compound of interest (PARAM vocab)",
        verbose_name="Compound Assessed",
    )

    def __str__(self) -> str:
        return ""

    class Meta:
        db_table = "BG_EXPO_ASSESSMENT"
        verbose_name = "Background exposure assessment"
        verbose_name_plural = "Background exposure assessment"


class HBGV(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_hbgv")
    novel_food = models.ForeignKey(
        NovelFood,
        on_delete=models.CASCADE,
        related_name="hbgvs",
        db_column="id_study",
    )
    type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="type_hbgvs",
        limit_choices_to=models.Q(taxonomy__code="ENDPOINT_HGV")
        & ~models.Q(short_name="root"),
        db_column="id_type",
        help_text="(ENDPOINT_HGV vocab)",
    )
    substance = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="substance_hbgvs",
        limit_choices_to=models.Q(taxonomy__code="PARAM")
        & ~models.Q(short_name="root"),
        db_column="id_substance",
        help_text="(PARAM vocab)",
    )
    exceeded = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="exceeded_hbgvs",
        limit_choices_to=models.Q(taxonomy__code="YESNO")
        & ~models.Q(short_name="root")
        & models.Q(is_yesno=True),
        db_column="id_exceeded",
        help_text="(YESNO vocab)",
        verbose_name="Exceedance",
    )

    def __str__(self):
        return f"{self.novel_food.title} - {self.substance.name} - {self.type.name}"

    class Meta:
        verbose_name = "Health-Based Guidance Value"
        verbose_name_plural = "Health-Based Guidance Values"
