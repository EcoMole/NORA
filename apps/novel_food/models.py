from django.db import models
from administrative.models import Opinion


class NutritionalDisadvantage(models.Model):
    #syn = models.ForeignKey("StudySyn", on_delete=models.CASCADE) #?
    outcome = models.CharField() #yesNo vocab
    explanation = models.CharField(max_length=2000)
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)

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


class Variant(models.Model):
    org = models.ForeignKey(Organism, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class NovelFoodOrganism(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    org_part = models.CharField(help_text='part of organism', blank=True) #vocab

    class Meta:
        db_table = "STUDY_ORG"
        verbose_name = "Organism Identity of NF"


class NovelFoodComponent(models.Model):
    novel_food = models.ForeignKey("NovelFood", on_delete=models.CASCADE)
    component = models.CharField(blank=True) #vocab 
    qualifier = models.CharField(blank=True) #vocab
    value = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "STUDY_COM"
        verbose_name = "Novel food component"
        verbose_name_plural = "Novel food components"


class NovelFood(models.Model):
    id_study = models.AutoField(primary_key=True)
    opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE, related_name="novel_food")
    #TODO check relation
    is_mutagenic = models.BooleanField(blank=True, null=True, verbose_name='mutagenic') #yesNo vocab

    is_genotoxic = models.BooleanField(blank=True, null=True, verbose_name='genotoxicity') #yesNo vocab

    is_carcinogenic = models.BooleanField(blank=True, null=True, verbose_name='carcinogenic') #yesNo vocab

    nf_code = models.CharField(max_length=2000, verbose_name='NF Code')

    tox_study_required = models.BooleanField(blank=True, null=True) #yesNo vocab

    protein_digestibility = models.CharField(blank=True) # vocab
    antinutritional_factors = models.CharField(blank=True) #vocab
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, blank=True, null=True)
    sufficient_data = models.BooleanField(blank=True, null=True, help_text='Were sufficient data provided?') #yesNo vocab
    food_matrices = models.BooleanField(blank=True, null=True, verbose_name='food matrices', help_text='Were food matrices provided?')  #yesNo vocab
    shelflife_value = models.FloatField(blank=True, null=True)
    shelflife_unit = models.CharField(blank=True, help_text='UNIT Catalogue') #UNIT vocab
    rms_efsa = models.CharField(blank=True) #? what is this? vocab
    endocrine_disrupt_prop = models.CharField(blank=True) #vocab
    outcome = models.CharField(blank=True) #yesNo vocab
    outcome_remarks = models.CharField(max_length=2000,blank=True)

    def __str__(self) -> str:
        return self.nf_code

    class Meta:
        db_table = "STUDY"
        verbose_name = "Novel food"
        verbose_name_plural = "Novel foods"
