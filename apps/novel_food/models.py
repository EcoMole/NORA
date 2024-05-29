from django.db import models
from administrative.models import Opinion

class Allergenicity(models.Model):
    id_allergenicity = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = "ALLERGENICITY"
        verbose_name = "Allergenicity"
        verbose_name_plural = "Allergenicity - options"


class AllergenicityNovelFood(models.Model):
    allergenicity = models.ForeignKey(Allergenicity, on_delete=models.CASCADE)
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)

    class Meta:
        db_table = "ALLERGENICITY_NOVEL_FOOD"
        verbose_name = "Allergenicity Assignment"
        verbose_name_plural = "Allergenicity Assignments"


class NutritionalDisadvantage(models.Model):
    id_nutritional_disadvantage = models.AutoField(primary_key=True)
    outcome = models.CharField() #yesNo vocab
    explanation = models.CharField(max_length=2000, blank=True)

    def __str__(self) -> str:
        return f'{self.outcome} - {self.explanation}'

    class Meta:
        db_table = "NUTRITIONAL_DISADVANTAGE"
        verbose_name = "Nutritional Disadvantage"


class Category(models.Model):
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)
    regulation_id = models.CharField() #vocab

    def __str__(self) -> str:
        return f'{self.regulation_id} : {self.title}'

    class Meta:
        db_table = "SUBTYPE"
        verbose_name = "Novel Food Category"
        verbose_name_plural = "NF Categories - options"


class NovelFoodCategory(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "STUDY_SUB_TYPE"
        verbose_name = "Novel Food Category"
        verbose_name_plural = "Novel Food Categories"


class FoodCategory(models.Model):
    #id_food_category = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        #db_table = "FOOD_CATEGORY"
        verbose_name = "Food category"
        verbose_name_plural = "Food categories - options"


class SynonymType(models.Model):
    id_synonym_type = models.AutoField(primary_key=True)
    synonym_type = models.CharField(max_length=255, help_text='Type of synonym -e.g. common name, trade name, synonym')
    definition = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.synonym_type

    class Meta:
        db_table = "SYNONYM"
        verbose_name = "Synonym Type"
        verbose_name_plural = "Synonym types - options"
    

class NovelFoodSyn(models.Model):
    type = models.ForeignKey(SynonymType, on_delete=models.CASCADE)
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    novel_food_synonym = models.CharField(max_length=255)

    def __str__(self):
        return ''

    class Meta:
        db_table = "STUDY_SYN"
        verbose_name = "Novel food synonym"

class Organism(models.Model):
    organism_node = models.CharField(help_text='organism') #Catalogue

    def __str__(self):
        return self.organism_node
    
    class Meta:
        db_table = "ORGANISM"
        verbose_name = "Organism"
        verbose_name_plural = "Organisms"

class OrganismSyn(models.Model):
    type = models.ForeignKey(SynonymType, on_delete=models.CASCADE)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    synonym = models.CharField(max_length=255)

    class Meta:
        db_table = "ORG_SYN"
        verbose_name = "Organism synonym"

class NovelFoodOrganism(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    org_part = models.CharField(help_text='part of organism', blank=True) #vocab
    is_gmo = models.BooleanField(blank=True, null=True) #yesNo vocab
    variant = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "STUDY_ORG"
        verbose_name = "Organism Identity of Novel food"


class NovelFoodChemical(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    chemical = models.ForeignKey("Chemical", on_delete=models.CASCADE)

    class Meta:
        db_table = "STUDY_COM"
        verbose_name = "Chemical identity of Novel food"

# For possible future use only
class ChemicalType(models.Model): 
    id_chemical_type = models.AutoField(primary_key=True, db_column='id_component_type')
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=2000)

    class Meta:
        db_table = "COM_TYPE"
        verbose_name = "Chemical type (future use)"
        verbose_name_plural = "Chemical types (future use)"

# For possible future use only
class StructureReported(models.Model):
    id_structure_reported = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    definition = models.CharField(max_length=2000)

    class Meta:
        db_table = "COM_STRUCTURE_SHOWN"
        verbose_name = "Structure reported (future use)"
        verbose_name_plural = "Structures reported (future use)"

class Chemical(models.Model):
    id_chemical = models.AutoField(primary_key=True, db_column='id_component')
    catalogue_identity = models.CharField(max_length=255, db_column='ID_RNC_EFSA', blank=True) #vocab param
    chemical_type = models.ForeignKey(ChemicalType, on_delete=models.CASCADE, blank=True, null=True, db_column='component_type')
    structure_reported = models.ForeignKey(StructureReported, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "COMPONENT"
        verbose_name = "Chemicals"
        verbose_name_plural = "Chemicals" 

    
class ChemicalSyn(models.Model):
    type = models.ForeignKey(SynonymType, on_delete=models.CASCADE)
    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)
    synonym = models.CharField(max_length=255)

    class Meta:
        db_table = "COM_SYN"
        verbose_name = "Chemical synonym"

class BackgroundExposureAssessment(models.Model):
    id_background_exposure_assessment = models.AutoField(primary_key=True)
    component_of_interest = models.CharField(max_length=255, blank=True) #vocab
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return ''
    
    class Meta:
        db_table = "BG_EXPO_ASSESSMENT"
        verbose_name = "Background exposure assessment"

class SubstanceOfConcernNovelFood(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    substance_of_concern = models.CharField(max_length=255) #vocab

    class Meta:
        db_table = "SUBSTANCE_OF_CONCERN_STUDY"
        verbose_name = "Substance of concern"

class GenotoxFinalOutcome(models.Model):
    id_genotox_final_outcome = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "GENOTOX_FINAL_OUTCOME"
        verbose_name = "Genotoxicity final outcome"
        verbose_name_plural = "Genotoxicity final outcomes"

class NovelFood(models.Model):
    id_study = models.AutoField(primary_key=True)
    opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE, related_name="novel_food")
    title = models.CharField(max_length=255, blank=False, verbose_name='NF name')
    nf_code = models.CharField(max_length=2000, verbose_name='NF Code')

    is_mutagenic = models.BooleanField(blank=True, null=True, verbose_name='mutagenic') #yesNo vocab
    genotox_final_outcome = models.ForeignKey(GenotoxFinalOutcome, on_delete=models.CASCADE, blank=True, null=True)
    is_carcinogenic = models.BooleanField(blank=True, null=True, verbose_name='carcinogenic') #yesNo vocab

    tox_study_required = models.BooleanField(blank=True, null=True) #yesNo vocab
    endocrine_disrupt_prop = models.BooleanField(blank=True, null=True, verbose_name='endocrine disrupt properties') #vocab

    protein_digestibility = models.BooleanField(blank=True, null=True) # vocab yesNo
    antinutritional_factors = models.BooleanField(blank=True, null=True) # vocab yesNo
    nutritional_disadvantage = models.OneToOneField(NutritionalDisadvantage, on_delete=models.CASCADE, blank=True, null=True)

    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, blank=True, null=True)

    sufficient_data = models.BooleanField(blank=True, null=True, help_text='Were sufficient data provided?') #yesNo vocab
    food_matrices = models.BooleanField(blank=True, null=True, verbose_name='food matrices', help_text='Were food matrices provided?')  #yesNo vocab
    shelflife_value = models.FloatField(blank=True, null=True)
    shelflife_unit = models.CharField(blank=True, help_text='UNIT Catalogue') #UNIT vocab
    instability_concerns = models.BooleanField(blank=True, null=True, verbose_name='instability concerns') #vocab yesNo

    rms_efsa = models.CharField(blank=True) #? what is this? vocab
    
    outcome = models.CharField(blank=True) #yesNo vocab
    outcome_remarks = models.CharField(max_length=2000,blank=True)

    # django specific fields to get the models well tied together
    allergenicity = models.ManyToManyField("Allergenicity", through='AllergenicityNovelFood', related_name='novel_foods')

    def __str__(self) -> str:
        return self.nf_code

    class Meta:
        db_table = "STUDY"
        verbose_name = "Novel Food"
        verbose_name_plural = "Novel Foods"
