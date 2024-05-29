from django.db import models
from administrative.models import Opinion


class NutritionalDisadvantage(models.Model):
    #syn = models.ForeignKey("StudySyn", on_delete=models.CASCADE) #?
    outcome = models.CharField() #yesNo vocab
    explanation = models.CharField(max_length=2000)
    #novel_food = models.OneToOneField("NovelFood", on_delete=models.CASCADE, related_name='nutritional_disadvantage')

    def __str__(self) -> str:
        return f'{self.outcome} - {self.explanation}'

    class Meta:
        db_table = "NUTRITIONAL_DISADVANTAGE"
        verbose_name = "Nutritional disadvantage"


class Category(models.Model):
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)
    regulation_id = models.CharField() #vocab

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "SUBTYPE"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class NovelFoodCategory(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    class Meta:
        db_table = "STUDY_SUBTYPE"
        verbose_name = "Novel food category"
        verbose_name_plural = "Novel food categories"


class FoodCategory(models.Model):
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        #db_table = "FOOD_CATEGORY"
        verbose_name = "Food category"
        verbose_name_plural = "Food categories"


class Synonym(models.Model):
    id_syn = models.AutoField(primary_key=True)
    synonym = models.CharField(max_length=255)
    definition = models.CharField(max_length=2000)

    class Meta:
        db_table = "SYNONYM"
        verbose_name = "Synonym"
    

class NovelFoodSyn(models.Model):
    synonym = models.ForeignKey(Synonym, on_delete=models.CASCADE)
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    novel_food_synonym = models.CharField(max_length=255)

    class Meta:
        db_table = "STUDY_SYN"
        verbose_name = "Novel food synonym"

class Organism(models.Model):
    organism_node = models.CharField(help_text='organism') #Catalogue


""" class Variant(models.Model):
    org = models.ForeignKey(Organism, on_delete=models.CASCADE)
    title = models.CharField(max_length=255) """


class NovelFoodOrganism(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    variant = models.ForeignKey(Organism, on_delete=models.CASCADE)
    org_part = models.CharField(help_text='part of organism', blank=True) #vocab
    is_gmo = models.BooleanField(blank=True, null=True) #yesNo vocab

    class Meta:
        db_table = "STUDY_ORG"
        verbose_name = "Organism Identity of Novel food"


class NovelFoodComponent(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    component = models.ForeignKey("Component", on_delete=models.CASCADE)

    class Meta:
        db_table = "STUDY_COM"
        verbose_name = "Chemical identity of Novel food"

# For possible future use only
class ComponentType(models.Model):
    id_component_type = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=2000)

    class Meta:
        db_table = "COM_TYPE"
        verbose_name = "Component type"
        verbose_name_plural = "Component types"

# For possible future use only
class StructureReported(models.Model):
    id_structure_reported = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=2000)

    class Meta:
        db_table = "COM_STRUCTURE_SHOWN"
        verbose_name = "Structure reported"
        verbose_name_plural = "Structures reported"

class Component(models.Model):
    id_component = models.AutoField(primary_key=True)
    catalogue_identity = models.CharField(max_length=255, db_column='ID_RNC_EFSA') #vocab param
    component_type = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    structure_reported = models.ForeignKey(StructureReported, on_delete=models.CASCADE)

    class Meta:
        db_table = "COMPONENT"
        verbose_name = "Chemicals" #TODO rename the model
        verbose_name_plural = "Chemicals" #TODO rename the model

    
class BackgroundExposureAssessment(models.Model):
    id_background_exposure_assessment = models.AutoField(primary_key=True)
    component_of_interest = models.CharField(max_length=255, blank=True) #vocab
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)


class NovelFood(models.Model):
    id_study = models.AutoField(primary_key=True)
    opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE, related_name="novel_food")
    #TODO check relation
    title = models.CharField(max_length=255, blank=False)
    is_mutagenic = models.BooleanField(blank=True, null=True, verbose_name='mutagenic') #yesNo vocab

    is_genotoxic = models.BooleanField(blank=True, null=True, verbose_name='genotoxic') #yesNo vocab

    is_carcinogenic = models.BooleanField(blank=True, null=True, verbose_name='carcinogenic') #yesNo vocab

    nf_code = models.CharField(max_length=2000, verbose_name='NF Code')

    tox_study_required = models.BooleanField(blank=True, null=True) #yesNo vocab

    protein_digestibility = models.BooleanField(blank=True, null=True) # vocab yesNo
    antinutritional_factors = models.BooleanField(blank=True, null=True) # vocab yesNo
    nutritional_disadvantage = models.OneToOneField(NutritionalDisadvantage, on_delete=models.CASCADE, blank=True, null=True)

    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, blank=True, null=True)

    sufficient_data = models.BooleanField(blank=True, null=True, help_text='Were sufficient data provided?') #yesNo vocab
    food_matrices = models.BooleanField(blank=True, null=True, verbose_name='food matrices', help_text='Were food matrices provided?')  #yesNo vocab
    shelflife_value = models.FloatField(blank=True, null=True)
    shelflife_unit = models.CharField(blank=True, help_text='UNIT Catalogue') #UNIT vocab
    #chybi instability concerns

    rms_efsa = models.CharField(blank=True) #? what is this? vocab
    endocrine_disrupt_prop = models.BooleanField(blank=True, null=True, verbose_name='endocrine disrupt properties') #vocab
    outcome = models.CharField(blank=True) #yesNo vocab
    outcome_remarks = models.CharField(max_length=2000,blank=True)

    def __str__(self) -> str:
        return self.nf_code

    class Meta:
        db_table = "STUDY"
        verbose_name = "Novel food"
        verbose_name_plural = "Novel foods"
