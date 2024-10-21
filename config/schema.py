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
        def create_q_object(lookup_field, lookup_type, value):
            lookup = f"{lookup_field}__{lookup_type}"
            print("lookup: value", f"{lookup}: {value}")
            return Q(**{lookup: value})

        def create_isnull_or_isempty_q_object(field_chain):
            """
            Creates Q objects which check whether
            each foreign key or field in the field_chain is null or,
            for the longest chain, if it is either null or an empty string.
            """
            fields = field_chain.split("__")
            q_objects = Q()
            for i in range(len(fields), 0, -1):
                f_chain = "__".join(fields[:i])
                q_objects |= Q(**{f_chain + "__isnull": True})
            return q_objects

        qs = NovelFood.objects.all()

        print("filters")
        print(filters)

        map = {
            "is before": "lt",
            "is after": "gt",
            "is": "exact",
            "contains": "icontains",
            "is None": "isnull",
            "is greater than": "gt",
            "is less than": "lt",
        }

        for f in filters:
            include = f.get("include")
            lookup_field = f.get("django_lookup_field")
            lookup_type = map[f.get("qualifier")]
            value = f.get("value")

            if lookup_field.endswith("__tax_node"):
                # the value searched on TaxonomyNode instances might be
                # either in short_name or in extended_name attributes
                prefix = lookup_field[: -len("__tax_node")]

                if lookup_type == "isnull":
                    q_object = create_isnull_or_isempty_q_object(prefix)
                    q_object |= Q(**{f"{prefix}__short_name__isnull": True}) & Q(
                        **{f"{prefix}__extended_name__isnull": True}
                    )
                else:
                    q_object = (
                        Q(**{f"{prefix}__short_name__isnull": False})
                        & ~Q(**{f"{prefix}__short_name": ""})
                        & Q(**{f"{prefix}__short_name__{lookup_type}": value})
                    ) | (
                        (
                            Q(**{f"{prefix}__short_name__isnull": True})
                            | Q(**{f"{prefix}__short_name": ""})
                        )
                        & Q(**{f"{prefix}__extended_name__{lookup_type}": value})
                    )

            elif lookup_field.endswith("__text_field"):
                lookup_field = lookup_field[: -len("__text_field")]

                if lookup_type == "isnull":
                    q_object = create_isnull_or_isempty_q_object(lookup_field)
                    q_object |= Q(**{lookup_field + "__exact": ""})
                else:
                    q_object = create_q_object(lookup_field, lookup_type, value)

            else:
                if lookup_type == "isnull":
                    q_object = create_isnull_or_isempty_q_object(lookup_field)
                else:
                    q_object = create_q_object(lookup_field, lookup_type, value)

            print("q_object", q_object)

            if include == "must have":
                qs = qs.filter(q_object)
            elif include == "must not have":
                qs = qs.exclude(q_object)
        return qs


schema = graphene.Schema(query=Query)
