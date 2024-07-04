from django.db import models


class VocabNodeField(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vocab Node Field"
        verbose_name_plural = "📂 Vocab Node Fields"


class FreqUsedVocabNode(models.Model):
    field = models.ForeignKey(
        VocabNodeField, on_delete=models.CASCADE, null=False, blank=False
    )
    entity = models.CharField(max_length=255, null=True, blank=True)
    node = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        related_name="code_listings",
        verbose_name="taxnomy node",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        result = self.field.title
        result += f" - {self.entity}" if self.entity else ""
        result += f" - {str(self.node)}"
        return result

    class Meta:
        verbose_name = "Frequently Used Vocab Node"
        verbose_name_plural = "📂 Frequently Used Vocab Nodes"
