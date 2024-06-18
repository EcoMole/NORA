from django.db import models


class AssessmentRemarks(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_assess")
    title = models.CharField(max_length=255, db_column="assess")
    definition = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "ASSESSMENT"
        verbose_name = "Assessment Remarks"
        verbose_name_plural = "Assessment Remarks"


class Endpointstudy(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_tox")
    novel_food = models.ForeignKey(
        "novel_food.NovelFood", on_delete=models.CASCADE, db_column="id_study"
    )
    testing_method = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="testing_method_endpointstudies",
        db_column="id_testing_method",
        limit_choices_to={"taxonomy__code": "TEST_TYPE"},
        help_text="for ex.: in silico, in vitro, in vivo, human study etc. (TEST_TYPE vocab)",
    )
    test_type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="test_type_endpointstudies",
        db_column="id_test_type",
        limit_choices_to={"taxonomy__code": "TEST_TYPE"},
        help_text="for ex.: acute oral toxicity (OECD phrase ID 1703), or "
        "subchronic (OECD phrase ID 2399) (TEST_TYPE vocab)",
    )
    guideline_qualifier = models.ForeignKey(
        "taxonomies.GuidelineQualifier",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_qualifier_endpointstudies",
        db_column="id_guideline_qualifier",
    )
    guideline = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_endpointstudies",
        db_column="id_guideline",
        limit_choices_to={"taxonomy__code": "GUIDELINE"},
        help_text="(GUIDELINE vocab)",
    )
    species = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "MTX"},
        db_column="id_species",
        related_name="species_endpointstudies",
        help_text="(MTX vocab)",
    )
    sex = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "MTX"},
        db_column="id_sex",
        related_name="sex_endpointstudies",
        help_text="(MTX vocab)",
    )
    exp_duration = models.FloatField(null=True, blank=True)
    duration_unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "UNIT"},
        db_column="id_duration_unit",
        related_name="duration_unit_endpointstudies",
        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
    )
    study_source = models.ForeignKey(
        "studies.StudySource",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="study_source_endpointstudies",
        db_column="id_study_source",
    )
    remarks = models.TextField(null=True, blank=True)
    test_material = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        res = self.novel_food.title
        if self.testing_method:
            res += " - " + self.testing_method.name
        return res

    class Meta:
        db_table = "ENDPOINTSTUDY"
        verbose_name = "Endpoint Study"
        verbose_name_plural = "Endpoint Studies 📐🔬"


class Endpoint(models.Model):
    reference_point = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
        db_column="id_endpoint",
        related_name="endpoint_end_endstudy_outcomes",
        help_text="(ENDPOINT_HGV vocab)",
    )
    qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="qualifier_end_endstudy_outcomes",
        db_column="id_qualifier",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
        help_text="(QUALIFIER vocab)",
    )
    lovalue = models.FloatField(null=True, blank=True)
    unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "UNIT"},
        db_column="id_unit",
        related_name="unit_end_endstudy_outcomes",
        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
    )
    sex = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "MTX"},
        db_column="id_sex",
        related_name="sex_end_endstudy_outcomes",
        help_text="(MTX vocab)",
    )
    endpointstudy = models.ForeignKey(
        Endpointstudy,
        on_delete=models.CASCADE,
        db_column="id_tox",
        related_name="endpointstudy_end_endstudy_outcomes",
    )

    def __str__(self) -> str:
        res = self.endpointstudy.novel_food.title
        if self.reference_point:
            res += " - " + self.reference_point.name
        return res

    class Meta:
        db_table = "ENDPOINT"
        verbose_name = "Endpoint"
        verbose_name_plural = "📂 Endpoints"


class Outcome(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_hazard")
    endpoint = models.ForeignKey(
        Endpoint,
        on_delete=models.CASCADE,
        db_column="id_endpoint",
    )
    assessment_type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
        db_column="id_assessment_type",
        related_name="assessment_type_outcomes",
        verbose_name="Assessment Type",
        help_text="(ENDPOINT_HGV vocab)",
    )
    risk_qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        db_column="id_risk_qualifier",
        related_name="risk_qualifier_outcomes",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
        help_text="(QUALIFIER vocab)",
    )
    value = models.FloatField(
        db_column="risk_value",
        null=True,
        blank=True,
    )
    unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "UNIT"},
        db_column="id_risk_unit",
        related_name="unit_outcomes",
        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
    )
    uncertainty_factor = models.IntegerField(
        null=True, blank=True, verbose_name="uncertainty factor"
    )
    assessment_remarks = models.ForeignKey(
        AssessmentRemarks,
        db_column="id_assess",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Assessment Remarks",
        help_text="This field provides additional information regarding the "
        "assessment particularly when no health-based guidance value (e.g., ADI, TDI) "
        "is provided in the Opinion.",
    )
    remarks = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        res = ""
        if self.assessment_type:
            res += self.assessment_type.name
        if self.value:
            res += " - " + str(self.value)
        if self.unit:
            res += " - " + self.unit.name
        return res

    class Meta:
        db_table = "HAZARD"
        verbose_name = "Final Outcome"
        verbose_name_plural = "Final Outcomes 🎰"


class StudyType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_study_type")
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "STUDY_TYPE"
        verbose_name = "ADME Study Type"
        verbose_name_plural = "ADME Study Types"


class OutcomePopulation(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_hazard_age")
    outcome = models.ForeignKey(
        Outcome, db_column="id_hazard", on_delete=models.CASCADE
    )
    population = models.ForeignKey(
        "taxonomies.Population",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="population_outcome_populations",
        db_column="id_age",
    )

    def __str__(self) -> str:
        res = ""
        if self.outcome and self.outcome.assessment_type:
            res += self.outcome.assessment_type.name
        if self.population:
            res += " - " + self.population.__str__()
        return res

    class Meta:
        db_table = "HAZARD_AGE"
        verbose_name = "Outcome Population"
        verbose_name_plural = "Outcome Populations"
        constraints = [
            models.UniqueConstraint(
                fields=["outcome", "population"], name="unique_outcome_population"
            ),
        ]


class StudySource(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_study_type")
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "STUDY_SOURCE"
        verbose_name_plural = "Study Sources"


class ADME(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_pktkade")
    novel_food = models.ForeignKey(
        "novel_food.NovelFood", db_column="pktkade_study", on_delete=models.CASCADE
    )
    testing_method = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="testing_method_admes",
        db_column="assay_system_endpoint",
        limit_choices_to={"taxonomy__code": "TEST_TYPE"},
        help_text="for ex.: in silico, in vitro, in vivo, human study etc. (TEST_TYPE vocab)",
    )
    guideline_qualifier = models.ForeignKey(
        "taxonomies.GuidelineQualifier",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_qualifier_admes",
    )
    guideline = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_admes",
        limit_choices_to={"taxonomy__code": "GUIDELINE"},
        help_text="(GUIDELINE vocab)",
    )
    study_source = models.ForeignKey(
        "studies.StudySource",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="study_source_admes",
        db_column="id_study_source",
    )
    test_material = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.TextField(db_column="study_comment", null=True, blank=True)

    def __str__(self) -> str:
        res = self.novel_food.title
        if self.testing_method:
            res += " - " + self.testing_method.name
        return res

    class Meta:
        db_table = "PKTK"
        verbose_name = "ADME Study"
        verbose_name_plural = "ADME Studies ♻️🔬"


class ADMEStudyType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_pktkade_study_type")
    adme = models.ForeignKey(ADME, db_column="id_pktkade", on_delete=models.CASCADE)
    study_type = models.ForeignKey(
        StudyType, db_column="id_study_type", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        res = self.adme.novel_food.title
        if self.adme.testing_method:
            res += " - " + self.adme.testing_method.name
        return res

    class Meta:
        db_table = "PKTK_STUDY_TYPE"
        verbose_name = "ADME Study Type"
        verbose_name_plural = "ADME Study Types"


class Genotox(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_tox")
    novel_food = models.ForeignKey(
        "novel_food.NovelFood", on_delete=models.CASCADE, db_column="id_study"
    )
    testing_method = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="testing_method_genotoxes",
        db_column="id_testing_method",
        limit_choices_to={"taxonomy__code": "TEST_TYPE"},
        help_text="for ex.: in silico, in vitro, in vivo, human study etc. (TEST_TYPE vocab)",
    )
    guideline_qualifier = models.ForeignKey(
        "taxonomies.GuidelineQualifier",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_qualifier_genotoxes",
        db_column="id_guideline_qualifier",
    )
    genotox_guideline = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="genotox_guideline_genotoxes",
        db_column="id_genotox_guideline",
        limit_choices_to={"taxonomy__code": "GUIDELINE"},
        help_text="(GUIDELINE vocab)",
    )
    outcome = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "POSNEG"},
        db_column="id_is_genotoxic",
        related_name="outcome_genotoxes",
        help_text="(POSNEG vocab)",
    )
    study_source = models.ForeignKey(
        "studies.StudySource",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="study_source_genotoxes",
        db_column="id_study_source",
    )
    test_type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="test_type_genotoxes",
        db_column="id_test_type",
        limit_choices_to={"taxonomy__code": "TEST_TYPE"},
        help_text="for ex.: acute oral toxicity (OECD phrase ID 1703), or "
        "subchronic (OECD phrase ID 2399). (TEST_TYPE vocab)",
    )
    test_material = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        res = self.novel_food.title
        if self.testing_method:
            res += " - " + self.testing_method.name
        return res

    class Meta:
        db_table = "GENOTOX"
        verbose_name = "Genotox Study"
        verbose_name_plural = "Genotox Studies 🧬🔬"
