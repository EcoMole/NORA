import graphene
from graphene_django.filter import DjangoFilterConnectionField
from novel_food.filters import NovelFoodFilter
from novel_food.models import NovelFood
from novel_food.schema import NovelFoodType


class Query(graphene.ObjectType):
    novel_foods = DjangoFilterConnectionField(
        NovelFoodType, filterset_class=NovelFoodFilter
    )

    def resolve_novel_foods(self, info, **kwargs):
        return NovelFood.objects.all()


schema = graphene.Schema(query=Query)
