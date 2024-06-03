from django.db import models


class Assessment(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_assess")
    title = models.CharField(max_length=255, db_collation="assessment")
    definition = models.CharField(max_length=255)

    class Meta:
        db_table = "ASSESSMENT"


class EndpointStudy(models.Model):
    study = models.ForeignKey("Study", on_delete=models.CASCADE)
    testing_method = models.ForeignKey("TestingMethod", on_delete=models.CASCADE)
    test_type = models.ForeignKey("TestType", on_delete=models.CASCADE)
    guideline_qualifier = models.ForeignKey(
        "GuidelineQualifier", on_delete=models.CASCADE
    )
    guideline = models.ForeignKey("Guideline", on_delete=models.CASCADE)
    species = models.ForeignKey("Species", on_delete=models.CASCADE)
    sex = models.ForeignKey("Sex", on_delete=models.CASCADE)
    exp_duration = models.FloatField()
    duration_unit = models.ForeignKey("DurationUnit", on_delete=models.CASCADE)
    helper_amount_of_studies_combined = models.IntegerField()
    study_source = models.ForeignKey("StudySource", on_delete=models.CASCADE)
    remarks = models.CharField(max_length=2000)
    test_material = models.CharField(max_length=255)


class EndEndstudyOutcome(models.Model):
    qualifier = models.ForeignKey("Qualifier", on_delete=models.CASCADE)
    lovalue = models.FloatField()
    unit = models.ForeignKey("Unit", on_delete=models.CASCADE)
    sex = models.ForeignKey("Sex", on_delete=models.CASCADE)
    tox = models.ForeignKey(EndpointStudy, on_delete=models.CASCADE)
    endpoint = models.ForeignKey("Endpoint", on_delete=models.CASCADE)


class Outcome(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_hazard")
    hazard = models.ForeignKey("Hazard", on_delete=models.CASCADE)
    assessment_type = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        db_column="id_assessment_type",
        on_delete=models.SET_NULL,
    )
    risk_qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        db_column="id_risk_qualifier",
        on_delete=models.SET_NULL,
    )
    value = models.FloatField(db_column="risk_value")
    unit = models.ForeignKey(
        "taxonomies.TaxonomyNode", db_column="id_risk_unit", on_delete=models.SET_NULL
    )
    safety_factor = models.IntegerField()
    assessment = models.ForeignKey(
        Assessment, db_column="id_assess", on_delete=models.SET_NULL
    )
    remarks = models.CharField(max_length=2000)
    end_endstudy_outcome = models.ForeignKey(
        EndEndstudyOutcome, on_delete=models.SET_NULL
    )
    toxicity_concern = models.ForeignKey(
        "taxonomies.TaxonomyNode", on_delete=models.SET_NULL
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
        "taxonomies.Population", db_column="id_age", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "HAZARD_AGE"
        constraints = [
            models.UniqueConstraint(fields=["hazard", "age"], name="unique_hazard_age"),
        ]


class StudySource(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_study_type")
    title = models.CharField(max_length=255)

    class Meta:
        db_table = "STUDY_SOURCE"


class ADME(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_pktkade")
    novel_food = models.ForeignKey(
        "novelfood.NovelFood", db_column="pktkade_study", on_delete=models.CASCADE
    )
    testing_method = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        db_column="assay_system_endpoint",
        on_delete=models.SET_NULL,
    )
    guideline_qualifier = models.ForeignKey(
        "taxonomies.TaxonomyNode", on_delete=models.SET_NULL
    )
    guideline = models.ForeignKey("taxonomies.TaxonomyNode", on_delete=models.SET_NULL)
    helper_amount_of_studies_combined = models.IntegerField()
    study_source = models.ForeignKey(
        StudySource, db_column="id_study_source", on_delete=models.SET_NULL
    )
    remarks = models.TextField(max_length=2000, db_collation="study_comment")
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
    study = models.ForeignKey("Study", on_delete=models.CASCADE)
    testing_method = models.ForeignKey("TestingMethod", on_delete=models.CASCADE)
    guideline_qualifier = models.ForeignKey(
        "GuidelineQualifier", on_delete=models.CASCADE
    )
    genotox_guideline = models.ForeignKey("GenotoxGuideline", on_delete=models.CASCADE)
    outcome = models.ForeignKey("Outcome", on_delete=models.CASCADE)
    helper_amount_of_studies_combined = models.IntegerField()
    study_source = models.ForeignKey(StudySource, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=255)
    test_material = models.CharField(max_length=255)


class GenotoxOutcome(models.Model):
    tox = models.ForeignKey(Genotox, on_delete=models.CASCADE)
    hazard = models.ForeignKey("Hazard", on_delete=models.CASCADE)
