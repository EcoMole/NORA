import graphene
from novel_food.models import NovelFood
from novel_food.schema import NovelFoodType


class Query(graphene.ObjectType):
    novel_foods = graphene.List(
        NovelFoodType,
    )

    def resolve_novel_foods(self, info, filters=None, **kwargs):
        queryset = NovelFood.objects.all()
        # filtering logic
        # ...
        return queryset


schema = graphene.Schema(query=Query)
