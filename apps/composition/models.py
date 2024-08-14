from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

# from django.db.models.functions import Lower
from novel_food.models import NovelFood


def validate_case_insensitive_parameter_title(value):
    if Parameter.objects.filter(
        Q(title__iexact=value)
        | Q(vocab_id__short_name__iexact=value)
        | Q(vocab_id__extended_name__iexact=value)
    ).exists():
        raise ValidationError(
            "A parameter with this case-insensitive title already exists."
        )


class ParameterType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_parameter_type")
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
    id = models.AutoField(primary_key=True, db_column="id_parameter")
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
        db_column="id_parameter_type",
    )

    # For possible future use only
    vocab_id = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="vocab_id_parameters",
        limit_choices_to=models.Q(taxonomy__code="PARAM") & ~models.Q(short_name="root"),
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

    #     constraints = [
    #         models.UniqueConstraint(
    #             Lower("title"), name="unique_title_case_insensitive"
    #         )
    #     ]

    # def save(self, *args, **kwargs):
    #     if (
    #         Parameter.objects.filter(title__iexact=self.title)
    #         .exclude(pk=self.pk)
    #         .exists()
    #     ):
    #         raise ValidationError(
    #             f'A model instance with title "{self.title}" already exists.'
    #         )
    #     super().save(*args, **kwargs)


class NovelFoodVariant(models.Model):
    duplicate_related = [
        "productions",
        "compositions",
        "proposed_uses",
        "risk_assess_red_flags",
    ]

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
        novel_food_part = self.novel_food.title
        novel_food_part += (
            f" ({self.novel_food.nf_code})" if self.novel_food.nf_code else ""
        )
        food_form_part = f" - {self.food_form}" if self.food_form else ""
        question_number_part = ""
        if questions := [oq.question for oq in self.novel_food.opinion.questions.all()]:
            question_number_part = " -"
            for q in questions:
                question_number_part += f"{q.number}, "
            question_number_part = question_number_part[:-2]
        return novel_food_part + food_form_part + question_number_part

    class Meta:
        db_table = "NOVEL_FOOD_VARIANT"
        verbose_name = "Novel Food Variant 🥗"
        verbose_name_plural = "Novel Food Variants 🥗"


class ProductionNovelFoodVariant(models.Model):
    """through table for Novel Food Variant and Production(taxonomy node)"""

    id = models.AutoField(primary_key=True, db_column="id_production_nf_variant")
    nf_variant = models.ForeignKey(
        NovelFoodVariant,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_nf_variant",
        related_name="productions",
    )

    process = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="process_production_novel_food_variants",
        limit_choices_to=models.Q(taxonomy__code="MTX") & ~models.Q(short_name="root") & models.Q(is_process=True),
        help_text="(MTX vocab)",
        db_column="id_process",
        verbose_name="Process Step",
    )

    def __str__(self):
        return ""

    class Meta:
        db_table = "PRODUCTION_NF_VARIANT"
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
    id = models.AutoField(primary_key=True, db_column="id_composition")
    nf_variant = models.ForeignKey(
        NovelFoodVariant,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_nf_variant",
        related_name="compositions",
    )
    parameter = models.ForeignKey(
        Parameter,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
        db_column="id_parameter",
    )
    qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="qualifier_compositions",
        db_column="id_qualifier",
        limit_choices_to=models.Q(taxonomy__code="QUALIFIER") & ~models.Q(short_name="root"),
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
        limit_choices_to=models.Q(taxonomy__code="UNIT") & ~models.Q(short_name="root"),
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

    class Meta:
        verbose_name = "Composition"
        verbose_name_plural = "Composition"


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
        related_name="proposed_uses",
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
        verbose_name="Target Population",
    )
    remarks = models.TextField(
        blank=True, null=True, help_text="Can be used for comments on the population."
    )

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "Proposed Use"
        verbose_name_plural = "Proposed Use"


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
        related_name="risk_assess_red_flags",
    )
    risk_assess_red_flag = models.ForeignKey(
        RiskAssessRedFlag,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_risk_assess_red_flag",
        verbose_name="Red Flag",
    )

    def __str__(self):
        return ""

    class Meta:
        db_table = "RISK_ASSESS_RED_FLAG_NF_VARIANT"
        verbose_name = "Risk assessment red flag"
        verbose_name_plural = "Risk assessment red flags"
