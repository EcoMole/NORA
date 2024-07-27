from django.db import models


class Endpointstudy(models.Model):
    duplicate_related = ["endpoints"]

    id = models.AutoField(primary_key=True, db_column="id_tox")
    novel_food = models.ForeignKey(
        "novel_food.NovelFood", on_delete=models.CASCADE, db_column="id_study"
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
        limit_choices_to={"taxonomy__code": "STUDYGUIDELINE"},
        help_text="(STUDYGUIDELINE vocab)",
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
    study_duration = models.DecimalField(
        max_digits=10, decimal_places=4, null=True, blank=True, db_column="exp_duration"
    )
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
    test_material = models.CharField(
        max_length=255, null=True, blank=True, db_column="testsubstance"
    )

    def __str__(self) -> str:
        test_type_part = f" - {self.test_type.name}" if self.test_type else ""
        species_part = f" - {self.species.name}" if self.species else ""

        return self.novel_food.title + test_type_part + species_part

    class Meta:
        db_table = "ENDPOINTSTUDY"
        verbose_name = "Endpoint Study 🔬📐"
        verbose_name_plural = "Endpoint Studies 🔬📐"


class Endpoint(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_endpoint")
    endpointstudy = models.ForeignKey(
        Endpointstudy,
        on_delete=models.CASCADE,
        db_column="id_tox",
        related_name="endpoints",
    )
    reference_point = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
        db_column="id_reference_point",
        related_name="endpoint_endpoints",
        help_text="(ENDPOINT_HGV vocab)",
    )
    qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="qualifier_endpoints",
        db_column="id_qualifier",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
        help_text="(QUALIFIER vocab)",
    )
    lovalue = models.DecimalField(
        max_digits=10, decimal_places=4, null=True, blank=True, verbose_name="Value"
    )
    unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "UNIT"},
        db_column="id_unit",
        related_name="unit_endpoints",
        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
    )
    subpopulation = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "MTX"},
        db_column="id_subpopulation",
        related_name="subpopulation_endpoints",
        help_text="value such as 'male', 'female', 'mothers', 'fetuses', 'offsprings' are "
        "stored here. (MTX vocab)",
    )

    def __str__(self) -> str:
        reference_point_part = (
            f" - {self.reference_point.name}" if self.reference_point else ""
        )
        lovalue_part = f" {self.lovalue}" if self.lovalue else ""
        subpopulation_part = (
            f" - {self.subpopulation.name}" if self.subpopulation else ""
        )

        return (
            str(self.endpointstudy)
            + reference_point_part
            + lovalue_part
            + subpopulation_part
        )

    class Meta:
        db_table = "ENDPOINT"
        verbose_name = "Endpoint"
        verbose_name_plural = "📂 Endpoints"


class FinalOutcome(models.Model):
    duplicate_related = ["populations"]

    id = models.AutoField(primary_key=True, db_column="id_hazard")
    endpoint = models.ForeignKey(
        Endpoint,
        on_delete=models.CASCADE,
        db_column="id_endpoint",
    )
    outcome = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
        db_column="id_assessment_type",
        related_name="outcome_final_outcomes",
        help_text="(ENDPOINT_HGV vocab)",
    )
    qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        db_column="id_risk_qualifier",
        related_name="qualifier_final_outcomes",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
        help_text="(QUALIFIER vocab)",
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=4,
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
        related_name="unit_final_outcomes",
        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
    )
    uncertainty_factor = models.IntegerField(
        null=True, blank=True, db_column="safety_factor"
    )
    remarks = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        res = ""
        if self.outcome:
            res += self.outcome.name
        if self.value:
            res += " - " + str(self.value)
        if self.unit:
            res += " - " + self.unit.name
        return res

    class Meta:
        db_table = "HAZARD"
        verbose_name = "Final Outcome 🎰"
        verbose_name_plural = "Final Outcomes 🎰"


class InvestigationType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_investigation_type")
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "INVESTIGATION_TYPE"
        verbose_name = "Investigation Type"
        verbose_name_plural = "Investigation Types"


class FinalOutcomePopulation(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_hazard_age")
    final_outcome = models.ForeignKey(
        FinalOutcome,
        db_column="id_hazard",
        on_delete=models.CASCADE,
        related_name="populations",
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
        if self.final_outcome and self.final_outcome.outcome:
            res += self.final_outcome.outcome.name
        if self.population:
            res += " - " + self.population.__str__()
        return res

    class Meta:
        db_table = "HAZARD_AGE"
        verbose_name = "Final Outcome Population"
        verbose_name_plural = "Final Outcome Populations"
        constraints = [
            models.UniqueConstraint(
                fields=["final_outcome", "population"],
                name="unique_final_outcome_population",
            ),
        ]


class StudySource(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_study_source")
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "STUDY_SOURCE"
        verbose_name_plural = "Study Sources"


class ADME(models.Model):
    duplicate_related = ["investigation_types"]

    id = models.AutoField(primary_key=True, db_column="id_pktkade")
    novel_food = models.ForeignKey(
        "novel_food.NovelFood", db_column="id_pktkade_study", on_delete=models.CASCADE
    )
    test_type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="test_type_admes",
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
        limit_choices_to={"taxonomy__code": "STUDYGUIDELINE"},
        help_text="(STUDYGUIDELINE vocab)",
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
        if self.test_type:
            res += " - " + self.test_type.name
        return res

    class Meta:
        db_table = "PKTK"
        verbose_name = "ADME Study 🔬♻️"
        verbose_name_plural = "ADME Studies 🔬♻️"


class ADMEInvestigationType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_pktkade_investigation_type")
    adme = models.ForeignKey(
        ADME,
        db_column="id_pktkade",
        on_delete=models.CASCADE,
        related_name="investigation_types",
    )
    investigation_type = models.ForeignKey(
        InvestigationType, db_column="id_investigation_type", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        res = self.adme.novel_food.title
        if self.adme.test_type:
            res += " - " + self.adme.test_type.name
        return res

    class Meta:
        db_table = "PKTK_INVESTIGATION_TYPE"
        verbose_name = "ADME Investigation Type"
        verbose_name_plural = "ADME Investigation Types"
        constraints = [
            models.UniqueConstraint(
                fields=["adme", "investigation_type"],
                name="unique_adme_investigation_type",
            )
        ]


class Genotox(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_tox")
    novel_food = models.ForeignKey(
        "novel_food.NovelFood", on_delete=models.CASCADE, db_column="id_study"
    )
    guideline_qualifier = models.ForeignKey(
        "taxonomies.GuidelineQualifier",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_qualifier_genotoxes",
        db_column="id_guideline_qualifier",
    )
    guideline = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_genotoxes",
        db_column="id_genotox_guideline",
        limit_choices_to={"taxonomy__code": "STUDYGUIDELINE"},
        help_text="(STUDYGUIDELINE vocab)",
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
        if self.test_type:
            res += " - " + self.test_type.name
        return res

    class Meta:
        db_table = "GENOTOX"
        verbose_name = "Genotoxicity Study 🔬🧬"
        verbose_name_plural = "Genotoxicity Studies 🔬🧬"
