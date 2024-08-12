import graphene
from graphene_django.types import DjangoObjectType

from .models import NovelFood


class NovelFoodType(DjangoObjectType):
    class Meta:
        model = NovelFood


class Query(graphene.ObjectType):
    novel_foods = graphene.List(NovelFoodType)

    def resolve_novel_foods(self, info):
        return NovelFood.objects.all()
