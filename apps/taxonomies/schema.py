import graphene
from graphene_django.types import DjangoObjectType
from taxonomies.models import Population


class PopulationType(DjangoObjectType):
    subgroup = graphene.String()
    qualifier = graphene.String()
    value = graphene.String()

    class Meta:
        model = Population
        exclude = ["unit", "upper_range_value"]

    def resolve_subgroup(self, info):
        return self.subgroup.title if self.subgroup else None

    def resolve_qualifier(self, info):
        return self.qualifier.name if self.qualifier else None

    def resolve_value(self, info):
        value_str = str(self.value)
        upper_range_str = str(self.upper_range_value)
        unit_str = self.unit.name if self.unit else None
        return f"{value_str}-{upper_range_str} {unit_str}"
