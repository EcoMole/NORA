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
        def create_null_or_empty_filter(field_chain):
            """
            Creates Q objects which check whether
            each foreign key or field in the field_chain is null or,
            for the longest chain, if it is either null or an empty string.
            """
            fields = field_chain.split("__")
            q_objects = Q()
            for i in range(len(fields), 0, -1):
                f_chain = "__".join(fields[:i])
                if i == len(fields):
                    # checks if it is the first iteration in the reversed loop
                    q_objects |= Q(**{f_chain + "__isnull": True}) | Q(
                        **{f_chain + "__exact": ""}
                    )
                else:
                    q_objects |= Q(**{f_chain + "__isnull": True})
            return q_objects

        qs = NovelFood.objects.all()

        print("filters")
        print(filters)

        map = {
            "is": "exact",
            "contains": "icontains",
            "is None": "isnull",
        }

        for f in filters:
            include = f.get("include")
            lookup_field = f.get("django_lookup_field")
            lookup_type = map[f.get("qualifier")]
            value = f.get("value")

            if lookup_type == "isnull":
                # if any attribute in the lookup_field chain is null,
                # we need to check whether any foreign key in the chain is null
                q_object = create_null_or_empty_filter(lookup_field)
            else:
                # Construct the lookup expression, e.g., 'title__icontains'
                lookup = f"{lookup_field}__{lookup_type}"
                q_object = Q(**{lookup: value})
                print("lookup: value", f"{lookup}: {value}")

            # the value searched on TaxonomyNode instances might be
            # either in short_name or in extended_name attributes
            if lookup_field.endswith("__tax_node"):
                prefix = lookup_field[: -len("__tax_node")]

                if lookup_type == "isnull":
                    q_object = create_null_or_empty_filter(prefix)
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

            print("q_object", q_object)

            if include == "must have":
                qs = qs.filter(q_object)
            elif include == "must not have":
                qs = qs.exclude(q_object)
        return qs


schema = graphene.Schema(query=Query)
