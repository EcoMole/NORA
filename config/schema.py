import graphene
from novel_food.models import NovelFood
from novel_food.schema import NovelFoodType


class Query(graphene.ObjectType):
    novel_foods = graphene.List(NovelFoodType, novelFoodTitle=graphene.String())

    def resolve_novel_foods(self, info, novelFoodTitle=None, **kwargs):
        print("novelFoodTitle", novelFoodTitle)
        if novelFoodTitle:
            return NovelFood.objects.filter(title=novelFoodTitle)
        return NovelFood.objects.all()


schema = graphene.Schema(query=Query)
