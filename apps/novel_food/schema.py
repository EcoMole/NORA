import graphene
from graphene_django.types import DjangoObjectType

from .models import NovelFood


class NovelFoodType(DjangoObjectType):
    class Meta:
        model = NovelFood


class Query(graphene.ObjectType):
    mymodels = graphene.List(NovelFoodType)

    def resolve_mymodels(self, info):
        return NovelFood.objects.all()
