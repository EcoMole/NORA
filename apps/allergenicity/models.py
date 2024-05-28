from django.db import models
from novel_food.models import NovelFood


class Allergenicity(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        #db_table = "ALLERGENICITY"
        verbose_name = "Allergenicity"
        verbose_name_plural = "Allergenicities"


class AllergenicityNovelFood(models.Model):
    allergenicity = models.ForeignKey(Allergenicity, on_delete=models.CASCADE)
    novel_food = models.ForeignKey(NovelFood, on_delete=models.CASCADE)

    class Meta:
        #db_table = "ALLERGENICITY_NOVEL_FOOD"
        verbose_name = "Allergenicity assignment"
        verbose_name_plural = "Allergenicity assignments"
