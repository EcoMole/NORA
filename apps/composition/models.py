from typing import Any
from django.db import models

from novel_food.models import NovelFood


class ParameterType(models.Model):
    id_parameter_type = models.AutoField(primary_key=True)
    parameter_type = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Parameter type",
    )

    def __str__(self) -> str:
        return self.parameter_type

class Parameter(models.Model):
    id_parameter = models.AutoField(primary_key=True)
    parameter_title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Parameter",
    )
    parameter_type = models.ForeignKey(
        ParameterType,
        blank=True, # not each parameter is assigned to some type
        null=True,
        on_delete=models.SET_NULL,
    )

    parameter_tax_node = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Tax node VOCABULARY",
    )

    def __str__(self) -> str:
        if self.parameter_type is None:
            return self.parameter_title
        return f'{self.parameter_title} ({self.parameter_type})'


class NovelFoodVariant(models.Model):
    id_novel_food_variant = models.AutoField(primary_key=True)
    novel_food = models.ForeignKey(NovelFood, blank=True, null=True, on_delete=models.CASCADE, db_column='study_id') #TODO Make false before db delete

    def __str__(self) -> str:
        return self.novel_food.title
    

class ProductionNovelFoodVariant(models.Model):
    """through table for Novel Food Variant and Production(taxonomy node)"""
    id_novel_food_variant = models.ForeignKey(NovelFoodVariant, blank=False, null=False, on_delete=models.CASCADE)

    id_node = models.CharField( # vocab
        max_length=255,
        blank=False,
        null=False,
        verbose_name='production process step',
        help_text="Taxonomy node",
    )

class FoodForm(models.Model):
    id_food_form = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the food form",
    )

    def __str__(self) -> str:
        return self.title


class FoodFormNovelFoodVariant(models.Model):
    """through table for Novel Food Variant and Food form"""
    food_form = models.ForeignKey(FoodForm, blank=False, null=False, on_delete=models.CASCADE)
    novel_food_variant = models.ForeignKey(NovelFoodVariant, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.food_form} - {self.novel_food_variant}"

    class Meta:
        db_table = "FOOD_FORM_NF_VARIANT"


class Composition(models.Model):
    id_composition = models.AutoField(primary_key=True)
    parameter = models.ForeignKey(
        Parameter,
        blank=False,
        null=False,
        on_delete=models.PROTECT,
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        blank=False,
        null=False,
        help_text="Value of the parameter",
    )
    upper_range_value = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        blank=True,
        null=True,
        help_text="Optional upper range value of the parameter",
    )
    unit = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Unit VOCABULARY",
    )
    novel_food_variant = models.ForeignKey(
        NovelFoodVariant,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    qualifier = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Qualifier VOCABULARY",
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

    footnote = models.CharField(
        max_length=2000,
        blank=True
    )


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
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    # TODO add age
    """ id_age = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Age VOCABULARY",
    ) """

class BackgroundExposureAssessment(models.Model): # move to Nutrition
    id_back_expo_assessment = models.AutoField(primary_key=True)
    compound_of_interest = models.CharField(
        max_length=2000,
        blank=False,
        null=False,
        help_text="Compound of interest",
    )

    proposed_use = models.ForeignKey(
        ProposedUse,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    #yn = models.ForeignKey("taxonomies.YesNo", blank=False, null=False, on_delete=models.CASCADE)
