import graphene
import novel_food.schema


class Query(novel_food.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
