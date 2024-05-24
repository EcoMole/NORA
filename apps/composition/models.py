from django.db import models


class FootNote(models.Model):
    id_footnote = models.AutoField(primary_key=True)
    footnote = models.CharField(
        max_length=255,
        unique=True, #?
        blank=False,
        null=False,
        help_text="Footnote text",
    )

class ParameterType(models.Model):
    id_parameter_type = models.AutoField(primary_key=True)
    parameter_type = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Parameter type",
    )

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
        decimal_places=10,
        blank=False,
        null=False,
        help_text="Value of the parameter",
    )
    upper_range_value = models.DecimalField(
        max_digits=10,
        decimal_places=10,
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
    #novel_food_variant

    qualifier = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Qualifier VOCABULARY",
    )

    TYPE_CHOICES = ( #TODO upresnit treti choice
        ("specification", "Specification"),
        ("composition", "Composition"),
        ("other", "Other"),
    )

    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
        blank=False,
        null=False,
        help_text="Specification/Composition/Other",
    )

    footnote = models.ForeignKey(
        FootNote,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )

class NovelFoodVariant(models.Model):
    id_novel_food_variant = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the novel food variant",
    )

class ProductionNovelFoodVariant(models.Model):
    """through table for Novel Food Variant and Production(taxonomy node)"""
    id_novel_food_variant = models.ForeignKey(NovelFoodVariant, blank=False, null=False, on_delete=models.CASCADE)

    id_node = models.CharField( # delete after adding catalogue
        max_length=255,
        blank=False,
        null=False,
        help_text="Taxonomy node",
    )
    # TODO catalogue
    #id_node = models.ForeignKey("taxonomies.TaxonomyNode", blank=False, null=False, on_delete=models.CASCADE)

class FoodForm(models.Model):
    id_food_form = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the food form",
    )


class FoodForm_NovelFoodVariant(models.Model):
    """through table for Novel Food Variant and Food form"""
    id_food_form = models.ForeignKey(FoodForm, blank=False, null=False, on_delete=models.CASCADE)
    id_novel_food_variant = models.ForeignKey(NovelFoodVariant, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id_food_form} - {self.id_novel_food_variant}"

    class Meta:
        db_table = "FOOD_FORM_NF_VARIANT"


