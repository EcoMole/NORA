from django.db import models


class Allergenicity(models.Model):
    title = models.CharField(max_length=255)


class AllergenicityStudy(models.Model):
    allergenicity = models.ForeignKey(Allergenicity, on_delete=models.CASCADE)
    study = models.ForeignKey("Study", on_delete=models.CASCADE)


class NutritionalDisadvantage(models.Model):
    syn = models.ForeignKey("StudySyn", on_delete=models.CASCADE)
    explanation = models.CharField(max_length=2000)
    study = models.ForeignKey("Study", on_delete=models.CASCADE)


class SubType(models.Model):
    sub_type = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)
    regulation_id = models.BigIntegerField()


class StudySubType(models.Model):
    study = models.ForeignKey("Study", on_delete=models.CASCADE)
    sub_type = models.ForeignKey(SubType, on_delete=models.CASCADE)


class FoodCategory(models.Model):
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)


class StudySyn(models.Model):
    syn = models.ForeignKey("Syn", on_delete=models.CASCADE)
    study = models.ForeignKey("Study", on_delete=models.CASCADE)
    study_syn = models.CharField(max_length=255)


class Organism(models.Model):
    org_node = models.BigIntegerField()


class Variant(models.Model):
    org = models.ForeignKey(Organism, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class StudyOrg(models.Model):
    study = models.ForeignKey("Study", on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    org_part = models.BigIntegerField()


class StudyCom(models.Model):
    study = models.ForeignKey("Study", on_delete=models.CASCADE)
    com = models.BigIntegerField()
    qualifier = models.BigIntegerField()
    value = models.FloatField()


class Study(models.Model):
    id_study = models.AutoField(primary_key=True)
    op = models.BigIntegerField()
    id_is_mutagenic = models.BigIntegerField()
    id_is_genotoxic = models.BigIntegerField()
    id_is_carcinogenic = models.BigIntegerField()
    nf_code = models.CharField(max_length=2000)
    tox_study_required = models.BigIntegerField()
    protein_digestibility = models.BigIntegerField()
    antinutritional_factors = models.BigIntegerField()
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    is_sufficient_data = models.BigIntegerField()
    is_food_matrices = models.BigIntegerField()
    shelflife_unit = models.BigIntegerField()
    shelflife_value = models.FloatField()
    rms_efsa = models.BigIntegerField()
    endocrine_disrupt_prop = models.BigIntegerField()
    outcome = models.BigIntegerField()
    outcome_remarks = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return self.nf_code

    class Meta:
        db_table = "STUDY"
