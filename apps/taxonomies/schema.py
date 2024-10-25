import graphene
from graphene_django.types import DjangoObjectType
from taxonomies.models import Population


class PopulationType(DjangoObjectType):
    subgroup = graphene.String()
    qualifier = graphene.String()
    unit = graphene.String()

    class Meta:
        model = Population
        fields = "__all__"

    def resolve_subgroup(self, info):
        return self.subgroup.title if self.subgroup else None

    def resolve_qualifier(self, info):
        return self.qualifier.name if self.qualifier else None

    def resolve_unit(self, info):
        return self.unit.name if self.unit else None
