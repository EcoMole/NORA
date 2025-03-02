import itertools

from django.db import models
from model_utils import Choices
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from utils.sync_mixin import SyncMixin


class Taxonomy(models.Model):
    code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "📂 Taxonomies"

    def __str__(self):
        return self.code


class TaxonomyNode(MPTTModel, SyncMixin):
    code = models.CharField(
        max_length=100, db_index=True, help_text="if creating new record use: NORA"
    )

    taxonomy = models.ForeignKey(
        "Taxonomy", null=True, blank=False, on_delete=models.CASCADE
    )

    short_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="if Organism: use SPECIES name + '(as animal)' or '(as plant)' or '(as organism)'",
    )

    scope = models.TextField(null=True, blank=True)

    extended_name = models.TextField(null=True, blank=True)

    order = models.IntegerField(default=1)

    reportable = models.BooleanField(default=True)

    STATUS = Choices(
        ("A", "APPROVED", "Approved"),
        ("D", "DEPRECATED", "Deprecated"),
        ("P", "PRELIMINARY", "Preliminary"),
        ("E", "EXPORTED", "Exported"),
    )

    status = models.CharField(max_length=1, choices=STATUS)

    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )

    is_botanic = models.BooleanField(
        default=False,
        help_text="Is this node marked as being in 'botanic' hierarchy?",
    )

    is_yesno = models.BooleanField(
        default=False,
        help_text="Is this node marked as being in 'yesno' hierarchy?",
    )

    is_gender = models.BooleanField(
        default=False,
        help_text="Is this node marked as being in 'gender' hierarchy?",
    )

    is_part_nature = models.BooleanField(
        default=False,
        help_text="Does this node belong to 'PartNature' facet from MTX?",
    )

    is_process = models.BooleanField(
        default=False,
        help_text="Does this node belong to 'process' facet from MTX?",
    )

    def to_html(self):
        ret = [self.code]
        if self.short_name:
            ret.append("; <b>%s</b>" % (self.short_name,))
        if self.extended_name:
            ret.append("; <b>%s</b>" % (self.extended_name,))
        if self.status != "A":
            ret.append("; status: %s" % (self.get_status_display(),))
        if hasattr(self, "match_count") and self.match_count:
            ret.append(' <span style="color: gray">(%s)</span>' % (self.match_count,))

        ret = "".join(ret)

        if self.scope:
            ret = '<span title="%s">%s</span>' % (self.scope, ret)
        if self.get_descendant_count():
            ret = '<span class="has_children">%s</span>' % (ret,)
        if self.status != "A":
            ret = '<span class="status_%s">%s</span>' % (
                self.status.lower(),
                ret,
            )

        return ret

    def get_significant_descendants(self):
        descendants = list(self.get_descendants())
        return descendants

    def get_significant_ancestors(self):
        ancestors = list(self.get_ancestors(ascending=True))
        if len(ancestors) > 1:
            ancestors = ancestors[:-1]
            if len(ancestors) > 2:
                for idx, ancestor in enumerate(ancestors):
                    if ancestor.code in (
                        "RF-00003395-PAR",
                        "RF-00003397-PAR",
                    ):
                        ancestors = ancestors[:idx]
                        break
        return ancestors

    def __str__(self):
        # return "%s %s %s (%s)" % (self.code, self.short_name,
        # self.extended_name, self.taxonomy.code)
        suffix = "(deprecated)" if self.status == self.STATUS.DEPRECATED else None
        base = " ".join(filter(None, [self.short_name, self.extended_name, suffix]))
        return "%s (%s)" % (base, self.code)

    @property
    def name(self):
        suffix = ""
        if self.status == self.STATUS.DEPRECATED:
            suffix = " (deprecated)"
        if self.short_name:
            return self.short_name + suffix
        return self.extended_name + suffix

    @property
    def all_names(self):
        def to_names(value):
            return [e.strip() for e in value.split("//")]

        def sanitize_name(direct_names, indirect_names):
            res = []

            # prev = ""
            for name, direct in sorted(
                {(e.strip(), True) for e in direct_names}.union(
                    {(e.strip(), False) for e in indirect_names}
                )
            ):
                res.append([name, direct])
                # prev = name

            return [
                e[0] for e in sorted(res, key=lambda x: (not x[1], x[0]))
            ]  # make direct names first

        # Got the names from taxonomies
        # direct_names = to_names(self.name)

        # The name might be also present among ImplicitAttributes ("A01")
        indirect_names = itertools.chain(
            *(
                to_names(e.value)
                for e in self.implicit_attributes.all()
                if e.code == "A01"
            )
        )

        return " // ".join(sanitize_name(to_names(self.name), indirect_names))

    class MPTTMeta:
        order_insertion_by = ["order", "code"]

    class Meta:
        verbose_name_plural = "📂 Taxonomy Nodes"


class ImplicitAttribute(models.Model):
    node = models.ForeignKey(
        TaxonomyNode, related_name="implicit_attributes", on_delete=models.CASCADE
    )
    code = models.CharField(max_length=100)
    value = models.CharField(
        max_length=45000
    )  # max_length extended due to long values in PARAM catalogue (starting from PARAM v6.0)

    def __str__(self):
        return "%s-%s (%s)" % (self.code, self.value, self.node)


class ExtendedTaxonomyNodeInformation(models.Model):
    taxonomy_node = models.ForeignKey(
        "TaxonomyNode", related_name="extended_info", on_delete=models.CASCADE
    )

    key = models.CharField(max_length=3)
    index = models.IntegerField()
    value = models.CharField(max_length=25500)


class Subgroup(models.Model):
    id = models.BigAutoField(primary_key=True, db_column="id_subgroup")
    title = models.CharField(max_length=255, db_column="subgroup")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "SUBGROUP"
        verbose_name = "Subgroup"
        verbose_name_plural = "📂 Subgroups"


class Population(models.Model):
    id = models.BigAutoField(primary_key=True, db_column="id_age")
    subgroup = models.ForeignKey(
        Subgroup,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="subgroup_populations",
        db_column="id_subgroup",
        verbose_name="Target Population",
    )
    qualifier = models.ForeignKey(
        TaxonomyNode,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="qualifier_populations",
        db_column="id_qualifier",
        verbose_name="Age Qualifier",
        limit_choices_to=models.Q(taxonomy__code="QUALIFIER")
        & ~models.Q(short_name="root")
        & ~models.Q(status=TaxonomyNode.STATUS.DEPRECATED),
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Age Value",
    )
    upper_range_value = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        null=True,
        blank=True,
        verbose_name="Age Upper Range Value",
        help_text="only if there is upper range value for age",
    )
    unit = models.ForeignKey(
        TaxonomyNode,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="unit_populations",
        db_column="id_unit",
        limit_choices_to=models.Q(taxonomy__code="UNIT")
        & models.Q(extended_name__in=["Hour", "Day", "Week", "Month", "Year"])
        & ~models.Q(status=TaxonomyNode.STATUS.DEPRECATED),
        verbose_name="Age Unit",
        help_text="use full name (e.g. 'gram' not 'g'). (UNIT vocab)",
    )

    def __str__(self):
        repr = ""
        if self.qualifier and self.qualifier.name:
            repr += self.qualifier.name
        if self.value:
            repr += f" {self.value}"
        if self.upper_range_value:
            repr += f" - {self.upper_range_value}"
        if self.unit:
            repr += f" {self.unit.name}"

        return f"{self.subgroup} - {repr}" if repr else str(self.subgroup)

    class Meta:
        db_table = "AGE"
        verbose_name = "Population"
        verbose_name_plural = "📂 Populations"


class GuidelineQualifier(models.Model):
    id = models.BigAutoField(primary_key=True, db_column="id_quideline_qualifier")
    title = models.CharField(
        max_length=255, db_column="guideline_qualifier", unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "GUIDELINE_QUALIFIER"
        verbose_name = "Guideline Qualifier"
        verbose_name_plural = "📂 Guideline Qualifiers"
