import graphene
from novel_food.models import NovelFood
from novel_food.schema import NovelFoodType


# Define the custom filter input
class NovelFoodFilterInput(graphene.InputObjectType):
    include = graphene.String()
    key = graphene.String()
    qualifier = graphene.String()
    value = graphene.String()


class NovelFoodConnection(graphene.relay.Connection):
    # necessary to use Rela-style connection for NovelFoodType with
    # custom resolver (custom filter) for the connection
    class Meta:
        node = NovelFoodType


class Query(graphene.ObjectType):
    novel_foods = graphene.ConnectionField(
        NovelFoodConnection, filters=graphene.List(NovelFoodFilterInput)
    )

    def resolve_novel_foods(self, info, filters=None, **kwargs):
        qs = NovelFood.objects.all()
        print("filters")
        print(filters)

        return qs


schema = graphene.Schema(query=Query)
