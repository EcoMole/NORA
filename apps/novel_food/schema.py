import graphene
from administrative.schema import OpinionType  # noqa
from graphene_django.types import DjangoObjectType

from .models import NovelFood


class NovelFoodType(DjangoObjectType):
    class Meta:
        model = NovelFood
        fields = "__all__"


class Query(graphene.ObjectType):
    novel_foods = graphene.List(NovelFoodType)

    def resolve_novel_foods(self, info):
        return NovelFood.objects.all()
