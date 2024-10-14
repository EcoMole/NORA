import graphene
from django.db.models import Q
from novel_food.models import NovelFood
from novel_food.schema import NovelFoodType


# Define the custom filter input
class NovelFoodFilterInput(graphene.InputObjectType):
    include = graphene.String()
    key = graphene.String()
    qualifier = graphene.String()
    value = graphene.String()
    django_lookup_field = graphene.String()


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

        map = {
            "is": "exact",
            "contains": "icontains",
            "is None": "isnull",
        }

        for f in filters:
            lookup_field = f.get("django_lookup_field")
            lookup_type = map[f.get("qualifier")]
            include = f.get("include")
            value = f.get("value")

            # Construct the lookup expression, e.g., 'title__icontains'
            lookup = f"{lookup_field}__{lookup_type}"
            print(lookup)
            # if lookup_type is 'isnull', the value should be True
            value = True if lookup_type == "isnull" else value
            q_object = Q(**{lookup: value})

            if include == "must have":
                qs = qs.filter(q_object)
            elif include == "must not have":
                qs = qs.exclude(q_object)
        return qs


schema = graphene.Schema(query=Query)
