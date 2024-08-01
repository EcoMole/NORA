import graphene
from graphene_django.types import DjangoObjectType

from .models import Opinion


class OpinionType(DjangoObjectType):
    class Meta:
        model = Opinion


class Query(graphene.ObjectType):
    opinions = graphene.List(OpinionType)

    def resolve_opinions(self, info):
        return Opinion.objects.all()
