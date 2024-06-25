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
        verbose_name_plural = "Production Processes"


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


class ProposedUse(models.Model):
    USE_CHOICES = [
        ("whole foods", "Whole foods"),
        ("food ingredients", "Food ingredients"),
        ("food supplements", "Food supplements"),
        ("infant follow on formula", "Infant formula and follow-on formula"),
        ("special medical purpose", "Food for special medical purposes"),
        ("total diet replacement", "Total diet replacement for weight control"),
    ]
    id = models.AutoField(primary_key=True, db_column="id_proposed_use")
    nf_variant = models.ForeignKey(
        NovelFoodVariant,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_nf_variant",
    )
    use_type = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        choices=USE_CHOICES,
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
        return ""


class RiskAssessRedFlag(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_risk_assess_red_flag")
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the risk assessment red flag",
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "RISK_ASSESS_RED_FLAG"
        verbose_name = "Risk assessment red flag"
        verbose_name_plural = "Risk assessment red flags"


class RiskAssessRedFlagNFVariant(models.Model):
    id = models.AutoField(
        primary_key=True, db_column="id_risk_assess_red_flag_nf_variant"
    )
    nf_variant = models.ForeignKey(
        NovelFoodVariant,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_nf_variant",
    )
    risk_assess_red_flag = models.ForeignKey(
        RiskAssessRedFlag,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_risk_assess_red_flag",
    )

    def __str__(self):
        return ""

    class Meta:
        db_table = "RISK_ASSESS_RED_FLAG_NF_VARIANT"
        verbose_name = "Risk assessment red flag"
        verbose_name_plural = "Risk assessment red flags"
