from django.db import models
from novel_food.models import NovelFood


class ParameterType(models.Model):
    id_parameter_type = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Parameter type",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "PARAMETER_TYPE"
        verbose_name = "Parameter Type"
        verbose_name_plural = "📂 Parameter Types"


class Parameter(models.Model):
    id_parameter = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Parameter",
    )
    type = models.ForeignKey(
        ParameterType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    # For possible future use only
    vocab_id = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="vocab_id_parameters",
        limit_choices_to={"taxonomy__code": "PARAM"},
        help_text="(PARAM vocab)",
        verbose_name="Parameter Vocabulary Identification",
        db_column="id_param",
    )

    def __str__(self) -> str:
        if self.type is None:
            return self.title
        return f"{self.title} ({self.type})"

    class Meta:
        db_table = "PARAMETER"
        verbose_name = "Parameter"
        verbose_name_plural = "📂 Parameters"


class NovelFoodVariant(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_nf_variant")
    novel_food = models.ForeignKey(
        NovelFood,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="study_id",
    )
    food_form = models.ForeignKey(
        "FoodForm",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        db_column="id_food_form",
    )

    # django specific fields to get the models well tied together
    risk_assessment_red_flags = models.ManyToManyField(
        "RiskAssessmentRedFlags", through="RiskAssessmentRedFlagsNFVariant"
    )

    def __str__(self) -> str:
        food_form_part = f" - {self.food_form}" if self.food_form else ""
        return self.novel_food.title + food_form_part

    class Meta:
        db_table = "NOVEL_FOOD_VARIANT"
        verbose_name = "Novel Food Variant 🥗"
        verbose_name_plural = "Novel Food Variants 🥗"


class ProductionNovelFoodVariant(models.Model):
    """through table for Novel Food Variant and Production(taxonomy node)"""

    id_novel_food_variant = models.ForeignKey(
        NovelFoodVariant, blank=False, null=False, on_delete=models.CASCADE
    )

    process = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="process_production_novel_food_variants",
        limit_choices_to={"taxonomy__code": "MTX"},
        help_text="(MTX vocab)",
    )

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Production Process"
        verbose_name_plural = "Production Process"


class FoodForm(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_food_form")
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the food form",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "FOOD_FORM"
        verbose_name = "Food Form"
        verbose_name_plural = "📂 Food Forms"


class Composition(models.Model):
    id_composition = models.AutoField(primary_key=True)
    novel_food_variant = models.ForeignKey(
        NovelFoodVariant,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    parameter = models.ForeignKey(
        Parameter,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
    )
    qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="qualifier_compositions",
        db_column="id_qualifier",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
        help_text="(QUALIFIER vocab)",
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        blank=True,
        null=True,
        help_text="Value of the parameter",
    )
    upper_range_value = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        blank=True,
        null=True,
        help_text="Optional upper range value of the parameter",
    )
    unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="unit_compositions",
        db_column="id_unit",
        limit_choices_to={"taxonomy__code": "UNIT"},
        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
    )
    TYPE_CHOICES = (
        ("specification", "Specification"),
        ("characterisation", "Characterisation"),
        ("other", "Other"),
    )

    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
        blank=False,
        null=False,
        help_text="Specification/Composition/Other",
    )

    footnote = models.TextField(blank=True)

    def __str__(self):
        return ""


class ProposedUseType(models.Model):
    id_use_type = models.AutoField(primary_key=True)
    USE_CHOICES = [
        ("whole_foods", "Whole foods"),
        ("food_ingredients", "Food ingredients"),
        ("food_supplements", "Food supplements"),
        ("infant_follow_on_formula", "Infant formula and follow-on formula"),
        ("special_medical_purpose", "Food for special medical purposes"),
        ("total_diet_replacement", "Total diet replacement for weight control"),
    ]
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the proposed use type",
        choices=USE_CHOICES,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "PROPOSED_USE_TYPE"
        verbose_name = "Proposed Use Type"
        verbose_name_plural = "📂 Proposed Use Types"


class ProposedUse(models.Model):
    id_proposed_use = models.AutoField(primary_key=True)
    nf_variant = models.ForeignKey(
        NovelFoodVariant,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    use_type = models.ForeignKey(
        ProposedUseType,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    population = models.ForeignKey(
        "taxonomies.Population",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="population_proposed_uses",
        db_column="id_age",
    )

    def __str__(self):
        return f"{self.nf_variant} - {self.use_type} - {self.population}"


class RiskAssessmentRedFlags(models.Model):
    id_risk_assessment_red_flags = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the risk assessment red flags",
    )

    def __str__(self):
        return self.title


class RiskAssessmentRedFlagsNFVariant(models.Model):
    id_risk_assessment_red_flags_novel_food = models.AutoField(primary_key=True)
    nf_variant = models.ForeignKey(
        NovelFoodVariant, blank=False, null=False, on_delete=models.CASCADE
    )
    risk_assessment = models.ForeignKey(
        RiskAssessmentRedFlags, blank=False, null=False, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Risk assessment red flag"
        verbose_name_plural = "Risk assessment red flags"
