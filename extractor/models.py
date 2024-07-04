from django.db import models


class FreqUsedVocabNode(models.Model):
    FIELD_CHOICES = [("org_part", "Organism Part")]
    node = models.ForeignKey(
        "taxonomies.TaxonomyNode",
        null=True,
        blank=True,
        related_name="code_listings",
        verbose_name="taxnomy node",
        on_delete=models.SET_NULL,
    )
    field = models.CharField(
        choices=FIELD_CHOICES, max_length=255, null=False, blank=False
    )
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.field + f" - {str(self.node)}"

    class Meta:
        verbose_name = "Frequently Used Vocab Node"
        verbose_name_plural = "👩‍🔬 Frequently Used Vocab Nodes"
