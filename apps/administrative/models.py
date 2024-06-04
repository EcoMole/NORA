from django.db import models

# from taxonomies.models import TaxonomyNode


class Opinion(models.Model):
    OUTCOME_CHOICES = [
        ("positive", "Positive"),
        ("negative", "Negative"),
        ("partially_negative", "Partially Negative"),
    ]
    id_op = models.AutoField(primary_key=True)
    id_op_type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        related_name="opinions",
        verbose_name="Document type",
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "REF_TYPE"}
        #   limit_choices_to=lambda: Q(pk__in=TaxonomyNode.objects.get(
        # taxonomy__code='REF_TYPE', code='').get_descendants()))
    )
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
    # upload_to='pdfs/' parameter in the FileField specifies
    # the subdirectory within the MEDIA_ROOT where the files will be saved
    pdf = models.FileField(upload_to="pdfs/", null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "OPINION"
        verbose_name = "Opinion 📄"
        verbose_name_plural = "Opinions 📄"


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
        verbose_name = "Panel"
        verbose_name_plural = "📂 Panels"


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
        verbose_name = "Applicant"
        verbose_name_plural = "📂 Applicants"


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

    regulation = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="mandate_types",
        db_column="id_regulation",
        limit_choices_to={"taxonomy__code": "LEGREF"},
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "MANDATE"
        verbose_name = "Mandate"
        verbose_name_plural = "📂 Mandates"


class Question(models.Model):
    id_question = models.AutoField(primary_key=True)
    question = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Question number",
    )

    applicant = models.ForeignKey(
        Applicant,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="applicant_questions",
        db_column="id_applicant",
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
        verbose_name = "Question"
        verbose_name_plural = "📂 Questions"


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
        verbose_name = "Scientific Officer"
        verbose_name_plural = "📂 Scientific Officers"


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
