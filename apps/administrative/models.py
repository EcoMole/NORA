from django.db import models

# from taxonomies.models import TaxonomyNode


class Opinion(models.Model):
    OUTCOME_CHOICES = [
        ("positive", "Positive"),
        ("negative", "Negative"),
        ("partially_negative", "Partially Negative"),
    ]
    id_op = models.AutoField(primary_key=True)
    # id_op_type = models.ForeignKey(
    #     "taxonomies.TaxonomyNode",
    #     null=True,
    #     blank=True,
    #     related_name="opinions",
    #     verbose_name="Document type",
    #     on_delete=models.SET_NULL,
    #     limit_choices_to=lambda: Q(pk__in=TaxonomyNode.objects.get(
    # taxonomy__code='REF_TYPE', code='').get_descendants()))
    # )
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Title of the opinion",
    )
    doi = models.CharField(
        max_length=255, blank=True, null=True, help_text="Digital Object Identifier"
    )
    url = models.URLField(blank=True, null=True, help_text="URL to the opinion")
    publication_date = models.DateField(
        blank=True, null=True, help_text="Date of publication"
    )
    adoption_date = models.DateField(
        blank=True, null=True, help_text="Date of adoption"
    )
    outcome = models.CharField(
        max_length=255,
        choices=OUTCOME_CHOICES,
        blank=True,
        null=True,
        help_text="Outcome of the opinion",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "OPINION"


class Panel(models.Model):
    id_panel = models.AutoField(primary_key=True)
    panel = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Title of the panel",
    )

    def __str__(self) -> str:
        return self.panel

    class Meta:
        db_table = "PANEL"


class OPAuthor(models.Model):
    """through table for Opinion and Panel"""

    id_op = models.ForeignKey(
        Opinion,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    id_panel = models.ForeignKey(
        Panel,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.id_op} - {self.id_panel}"

    class Meta:
        db_table = "OP_AUTHOR"


class Applicant(models.Model):
    id_applicant = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Name of the applicant",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "APPLICANT"


class Dossier(models.Model):
    id_dossier = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(
        Applicant,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="dossiers",
        db_column="id_applicant",
    )

    def __str__(self) -> str:
        return self.number

    class Meta:
        db_table = "DOSSIER"


class Mandate(models.Model):
    id_mandate = models.AutoField(primary_key=True)

    TYPE_CHOICES = [
        ("novel_food", "Novel food"),
        ("new_dossier", "New dossier"),
        ("extension_of_use", "Extension of use"),
        ("nutrient_source", "Nutrient source"),
        ("traditional_food", "Traditional food"),
        ("nutrient_source", "Nutrient source"),
    ]

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the mandate type",
        choices=TYPE_CHOICES,
    )

    mandate_parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="mandates",
        db_column="id_mandate_parent",
    )

    # regulation = models.ForeignKey(
    #     "taxonomies.TaxonomyNode",
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     related_name="mandate_types",
    #     db_column='id_regulation'
    # )
    # TODO: remove this field after the extraction is complete
    helper_regulation = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="this field will be removed after the extraction is complete",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "MANDATE"


class Question(models.Model):
    id_question = models.AutoField(primary_key=True)
    question = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Question number",
    )
    dossier = models.OneToOneField(
        Dossier,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Dossier number",
        related_name="questions",
        db_column="id_dossier",
    )
    mandate = models.ForeignKey(
        Mandate,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="questions",
        db_column="id_mandate",
    )

    def __str__(self) -> str:
        return self.question

    class Meta:
        db_table = "QUESTION"


class OPQuestion(models.Model):
    """through table for Opinion and Question"""

    id_op = models.ForeignKey(
        Opinion,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    id_question = models.ForeignKey(
        Question,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.id_op} - {self.id_question}"

    class Meta:
        db_table = "OP_QUESTION"


class ScientificOfficer(models.Model):
    id_sci_officer = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    class Meta:
        db_table = "SCI_OFFICER"


class OPScientificOfficer(models.Model):
    """through table for Opinion and Scientific Officer"""

    id_op = models.ForeignKey(
        Opinion,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    id_sci_officer = models.ForeignKey(
        ScientificOfficer,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.id_op} - {self.id_sci_officer}"

    class Meta:
        db_table = "OP_SCI_OFFICER"
