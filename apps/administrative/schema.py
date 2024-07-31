import graphene
from graphene_django.types import DjangoObjectType

from .models import Opinion


class OpinionType(DjangoObjectType):
    class Meta:
        model = Opinion


class Query(graphene.ObjectType):
    mymodels = graphene.List(OpinionType)

    def resolve_mymodels(self, info):
        return Opinion.objects.all()
