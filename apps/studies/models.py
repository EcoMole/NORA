from django.db import models


class Assessment(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_assess")
    title = models.CharField(max_length=255, db_column="assessment")
    definition = models.CharField(max_length=255)

    class Meta:
        db_table = "ASSESSMENT"


class EndpointStudy(models.Model):
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
        help_text="for ex.: in silico, in vitro, in vivo, human study etc.",
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
        "subchronic (OECD phrase ID 2399)",
    )
    guideline_qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_qualifier_endpointstudies",
        db_column="id_guideline_qualifier",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
    )
    guideline = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_endpointstudies",
        db_column="id_guideline",
        limit_choices_to={"taxonomy__code": "GUIDELINE"},
    )
    species = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "MTX"},
        db_column="id_species",
        related_name="species_endpointstudies",
    )
    sex = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "MTX"},
        db_column="id_sex",
        related_name="sex_endpointstudies",
    )
    exp_duration = models.FloatField()
    duration_unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "UNIT"},
        db_column="id_duration_unit",
        help_text="UNIT Catalogue",
        related_name="duration_unit_endpointstudies",
    )
    study_source = models.ForeignKey(
        "studies.StudySource",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="study_source_endpointstudies",
        db_column="id_study_source",
    )
    remarks = models.CharField(max_length=2000)
    test_material = models.CharField(max_length=255)


class EndEndstudyOutcome(models.Model):
    qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="qualifier_end_endstudy_outcomes",
        db_column="id_qualifier",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
    )
    lovalue = models.FloatField()
    unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "UNIT"},
        db_column="id_unit",
        help_text="UNIT Catalogue",
        related_name="unit_end_endstudy_outcomes",
    )
    sex = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "MTX"},
        db_column="id_sex",
        related_name="sex_end_endstudy_outcomes",
    )
    endpointstudy = models.ForeignKey(
        EndpointStudy,
        on_delete=models.CASCADE,
        db_column="id_tox",
        related_name="endpointstudy_end_endstudy_outcomes",
    )
    endpoint = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
        db_column="id_endpoint",
        related_name="endpoint_end_endstudy_outcomes",
    )


class Outcome(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_hazard")
    assessment_type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "ENDPOINT_HGV"},
        db_column="id_assessment_type",
        related_name="assessment_type_outcomes",
    )
    risk_qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        db_column="id_risk_qualifier",
        related_name="risk_qualifier_outcomes",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
    )
    value = models.FloatField(db_column="risk_value")
    unit = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "UNIT"},
        db_column="id_risk_unit",
        help_text="UNIT Catalogue",
        related_name="unit_outcomes",
    )
    safety_factor = models.IntegerField()
    assessment = models.ForeignKey(
        Assessment,
        db_column="id_assess",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    remarks = models.CharField(max_length=2000)
    end_endstudy_outcome = models.ForeignKey(
        EndEndstudyOutcome, on_delete=models.CASCADE, db_column="end_endstudy_hazard"
    )
    toxicity_concern = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        related_name="toxicity_concern_outcomes",
    )

    class Meta:
        db_table = "HAZARD"


class StudyType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_study_type")
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "STUDY_TYPE"


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

    class Meta:
        db_table = "HAZARD_AGE"
        constraints = [
            models.UniqueConstraint(
                fields=["outcome", "population"], name="unique_outcome_population"
            ),
        ]


class StudySource(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_study_type")
    title = models.CharField(max_length=255)

    class Meta:
        db_table = "STUDY_SOURCE"


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
        help_text="for ex.: in silico, in vitro, in vivo, human study etc.",
    )
    guideline_qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_qualifier_admes",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
    )
    guideline = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_admes",
        limit_choices_to={"taxonomy__code": "GUIDELINE"},
    )
    study_source = models.ForeignKey(
        "studies.StudySource",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="study_source_admes",
        db_column="id_study_source",
    )
    remarks = models.TextField(max_length=2000, db_column="study_comment")
    test_material = models.CharField(max_length=255)

    class Meta:
        db_table = "PKTK"


class ADMEStudyType(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_pktkade_study_type")
    adme = models.ForeignKey(ADME, db_column="id_pktkade", on_delete=models.CASCADE)
    study_type = models.ForeignKey(
        StudyType, db_column="id_study_type", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "PKTK_STUDY_TYPE"


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
        help_text="for ex.: in silico, in vitro, in vivo, human study etc.",
    )
    guideline_qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="guideline_qualifier_genotoxes",
        db_column="id_guideline_qualifier",
        limit_choices_to={"taxonomy__code": "QUALIFIER"},
    )
    genotox_genotox_guideline = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="genotox_guideline_genotoxes",
        db_column="id_genotox_guideline",
        limit_choices_to={"taxonomy__code": "GUIDELINE"},
    )
    outcome = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"taxonomy__code": "YESNO"},
        db_column="id_is_genotoxic",
        related_name="outcome_genotoxes",
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
        "subchronic (OECD phrase ID 2399)",
    )
    test_material = models.CharField(max_length=255)


class GenotoxOutcome(models.Model):
    id_tox = models.ForeignKey(Genotox, on_delete=models.CASCADE)
    hazard = models.ForeignKey(Outcome, on_delete=models.CASCADE)