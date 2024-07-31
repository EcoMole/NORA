import administrative.schema
import graphene
import novel_food.schema


class Query(novel_food.schema.Query, administrative.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
