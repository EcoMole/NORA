from administrative.models import Opinion
from django.db import models


class Allergenicity(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_allergenicity")
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "ALLERGENICITY"
        verbose_name = "Allergenicity"
        verbose_name_plural = "Allergenicity - options"


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
    )

    def __str__(self) -> str:
        return f"{self.regulation} : {self.title}"

    class Meta:
        db_table = "SUB_TYPE"
        verbose_name = "Novel Food Category"
        verbose_name_plural = "NF Categories - options"


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
        verbose_name_plural = "Food categories - options"


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
        verbose_name_plural = "Synonym types - options"


class NovelFoodSyn(models.Model):
    type = models.ForeignKey(SynonymType, on_delete=models.CASCADE)
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    novel_food_synonym = models.CharField(max_length=255)

    def __str__(self):
        return ""

    class Meta:
        db_table = "STUDY_SYN"
        verbose_name = "Novel food synonym"


class Organism(models.Model):
    organism_node = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "MTX"},
    )

    def __str__(self):
        return self.organism_node.name

    class Meta:
        db_table = "ORGANISM"
        verbose_name = "Organism"
        verbose_name_plural = "Organisms"


class OrganismSyn(models.Model):
    type = models.ForeignKey(SynonymType, on_delete=models.CASCADE)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    synonym = models.CharField(max_length=255)

    class Meta:
        db_table = "ORG_SYN"
        verbose_name = "Organism synonym"


class NovelFoodOrganism(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    org_part = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="org_part_novel_foods",
        limit_choices_to={"taxonomy__code": "MTX"},
    )
    is_gmo = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="is_gmo_novel_foods",
        limit_choices_to={"taxonomy__code": "YESNO"},
    )
    variant = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="variant_novel_foods",
        limit_choices_to={"taxonomy__code": "STRAIN"},
    )

    class Meta:
        db_table = "STUDY_ORG"
        verbose_name = "Organism Identity of Novel food"


class NovelFoodChemical(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    chemical = models.ForeignKey("Chemical", on_delete=models.CASCADE)

    class Meta:
        db_table = "STUDY_COM"
        verbose_name = "Chemical identity of Novel food"


# For possible future use only
class ChemicalType(models.Model):
    id_chemical_type = models.AutoField(primary_key=True, db_column="id_component_type")
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=2000)

    class Meta:
        db_table = "COM_TYPE"
        verbose_name = "Chemical type (future use)"
        verbose_name_plural = "Chemical types (future use)"


# For possible future use only
class StructureReported(models.Model):
    id_structure_reported = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=2000)

    class Meta:
        db_table = "COM_STRUCTURE_SHOWN"
        verbose_name = "Structure reported (future use)"
        verbose_name_plural = "Structures reported (future use)"


class Chemical(models.Model):
    id_chemical = models.AutoField(primary_key=True, db_column="id_component")
    catalogue_identity = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="catalogue_identity_chemicals",
        limit_choices_to={"taxonomy__code": "PARAM"},
    )

    chemical_type = models.ForeignKey(
        ChemicalType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column="component_type",
    )
    structure_reported = models.ForeignKey(
        StructureReported, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.catalogue_identity.name

    class Meta:
        db_table = "COMPONENT"
        verbose_name = "Chemicals"
        verbose_name_plural = "Chemicals"


class ChemicalSyn(models.Model):
    type = models.ForeignKey(SynonymType, on_delete=models.CASCADE)
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    synonym = models.CharField(max_length=255)

    class Meta:
        db_table = "COM_SYN"
        verbose_name = "Chemical synonym"


class BackgroundExposureAssessment(models.Model):
    id_background_exposure_assessment = models.AutoField(primary_key=True)
    component_of_interest = models.CharField(max_length=255, blank=True)  # vocab
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return ""

    class Meta:
        db_table = "BG_EXPO_ASSESSMENT"
        verbose_name = "Background exposure assessment"


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
    )

    class Meta:
        db_table = "SUBSTANCE_OF_CONCERN_STUDY"
        verbose_name = "Substance of concern"


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
    nf_code = models.CharField(max_length=2000, verbose_name="NF Code")

    food_category = models.ForeignKey(
        FoodCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        db_column="id_food_category",
        related_name="food_category_novel_foods",
    )
    # toxicity
    tox_study_required = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        db_column="id_tox_study_required",
        verbose_name="Tox study required",
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        related_name="tox_study_required_novel_foods",
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
        help_text="Were sufficient data provided?",
        related_name="sufficient_data_novel_foods",
    )

    food_matrices = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        db_column="id_is_food_matrices",
        help_text="Were food matrices provided?",
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
    )
    shelflife_value = models.FloatField(blank=True, null=True)
    shelflife_unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "UNIT"},
        db_column="id_shelflife_unit",
        help_text="UNIT Catalogue",
        related_name="shelflife_unit_novel_foods",
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
    )
    outcome = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "POSNEG"},
        db_column="id_outcome",
        related_name="outcome_novel_foods",
    )
    outcome_remarks = models.CharField(max_length=2000, blank=True, null=True)

    catalogue_identity = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "PARAM"},
        db_column="id_rms_efsa",
        related_name="catalogue_identity_novel_foods",
    )

    # django specific fields to get the models well tied together
    allergenicity = models.ManyToManyField(
        "Allergenicity",
        through="AllergenicityNovelFood",
        related_name="allergenicity_novel_foods",
    )

    def __str__(self) -> str:
        return self.nf_code + " - " + self.title

    class Meta:
        db_table = "STUDY"
        verbose_name = "Novel Food"
        verbose_name_plural = "Novel Foods"


class HBGV(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_hbgv")
    type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="type_hbgvs",
        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
        db_column="id_type",
    )
    novel_food = models.ForeignKey(
        NovelFood,
        on_delete=models.CASCADE,
        related_name="novel_food_hbgvs",
        db_column="id_study",
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
    substance = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="substance_hbgvs",
        limit_choices_to={"taxonomy__code": "PARAM"},
        db_column="id_substance",
    )

    def __str__(self):
        return f"{self.novel_food.title} - {self.substance.name} - {self.type.name}"

    class Meta:
        verbose_name = "Health-Based Guidence Value"
        verbose_name_plural = "Health-Based Guidence Values"