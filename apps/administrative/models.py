from django.db import models

# from taxonomies.models import TaxonomyNode


class Opinion(models.Model):
    OUTCOME_CHOICES = [
        ("positive", "Positive"),
        ("negative", "Negative"),
        ("partially_negative", "Partially Negative"),
    ]
    id = models.AutoField(primary_key=True, db_column="id_op")
    document_type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        related_name="opinions",
        verbose_name="Document type",
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "REF_TYPE"},
        help_text="(REF_TYPE vocab)",
        db_column="id_op_type",
        #   limit_choices_to=lambda: Q(pk__in=TaxonomyNode.objects.get(
        # taxonomy__code='REF_TYPE', code='').get_descendants()))
    )
    title = models.CharField(
        max_length=2000,
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
    # upload_to='pdfs/' parameter in the FileField specifies
    # the subdirectory within the MEDIA_ROOT where the files will be saved
    pdf = models.FileField(upload_to="pdfs/", null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "OPINION"
        verbose_name = "Opinion 📄"
        verbose_name_plural = "Opinions 📄"


class Question(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_question")
    number = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        db_column="question",
        help_text="Question number",
    )

    def __str__(self) -> str:
        return self.number

    class Meta:
        db_table = "QUESTION"
        verbose_name = "Question"
        verbose_name_plural = "Questions❔"


class Panel(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_panel")
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        help_text="Title of the panel",
        db_column="panel",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "PANEL"
        verbose_name = "Panel"
        verbose_name_plural = "📂 Panels"


class OpinionPanel(models.Model):
    """through table for Opinion and Panel"""

    opinion = models.ForeignKey(
        Opinion,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_op",
    )
    panel = models.ForeignKey(
        Panel,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_panel",
    )

    def __str__(self) -> str:
        return f"{self.opinion} - {self.panel}"

    class Meta:
        db_table = "OP_AUTHOR"


class Applicant(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_applicant")
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


class MandateType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_mandate_type")

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="Title of the mandate type",
        db_column="mandate_type",
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "MANDATE_TYPE"
        verbose_name = "Mandate Type"
        verbose_name_plural = "📂 Mandate Typess"


class OpinionQuestion(models.Model):
    """through table for Opinion and Question"""

    opinion = models.ForeignKey(
        Opinion,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_op",
    )
    question = models.ForeignKey(
        Question,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_question",
    )

    def __str__(self) -> str:
        return f"{self.opinion} - {self.question}"

    class Meta:
        db_table = "OP_QUESTION"


class ScientificOfficer(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_sci_officer")
    first_name = models.CharField(max_length=255, blank=False, null=False)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        if self.middle_name is None:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    class Meta:
        db_table = "SCI_OFFICER"
        verbose_name = "Scientific Officer"
        verbose_name_plural = "📂 Scientific Officers"


class OpinionSciOfficer(models.Model):
    """through table for Opinion and Scientific Officer"""

    opinion = models.ForeignKey(
        Opinion,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_op",
    )
    sci_officer = models.ForeignKey(
        ScientificOfficer,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.opinion} - {self.sci_officer}"

    class Meta:
        db_table = "OP_SCI_OFFICER"


class Mandate(models.Model):
    """through table for Question and MandateType and regulations from TaxonomyNode"""

    id = models.AutoField(primary_key=True, db_column="id_mandate")

    question = models.ForeignKey(
        Question,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_question",
    )
    mandate_type = models.ForeignKey(
        MandateType,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        db_column="id_mandate_type",
    )
    regulation = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="regulation_mandates",
        db_column="id_regulation",
        limit_choices_to={"taxonomy__code": "LEGREF"},
        help_text="(LEGREF vocab)",
    )

    def __str__(self) -> str:
        res = f"{self.question} - {self.mandate_type}"
        if self.regulation:
            res += f" - {self.regulation.name}"
        return res

    class Meta:
        db_table = "QUESTION_MANDATE"
        verbose_name = "Question Mandate Regulation"
        verbose_name_plural = "📂 Question Mandate Regulation"


class QuestionApplicant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.question} - {self.applicant}"

    class Meta:
        db_table = "QUESTION_APPLICANT"
        verbose_name = "Question Applicant"
        verbose_name_plural = "📂 Question Applicants"
