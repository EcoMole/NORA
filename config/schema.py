import graphene
from novel_food.models import NovelFood
from novel_food.schema import NovelFoodType


class Query(graphene.ObjectType):
    novel_foods = graphene.List(NovelFoodType, novel_food_title=graphene.String())

    def resolve_novel_foods(self, info, novel_food_title=None, **kwargs):
        if novel_food_title:
            return NovelFood.objects.filter(title=novel_food_title)
        return NovelFood.objects.all()


schema = graphene.Schema(query=Query)
