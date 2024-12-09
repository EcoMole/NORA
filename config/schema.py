import graphene
from django.apps import apps
from django.db.models import BooleanField, Case, Q, Value, When
from novel_food.models import NovelFood
from novel_food.schema import NovelFoodType


class ValueFieldsInput(graphene.InputObjectType):
    django_app = graphene.String()
    django_model = graphene.String()
    qualifier_field = graphene.String()
    value_field = graphene.String()
    upper_range_value_field = graphene.String()


# Define the custom filter input
class CoupledFilterInput(graphene.InputObjectType):
    key = graphene.String()
    qualifier = graphene.String()
    value = graphene.String()
    django_lookup_field = graphene.String()
    field_type = graphene.String()
    value_fields = graphene.Field(ValueFieldsInput)


class NovelFoodFilterInput(graphene.InputObjectType):
    django_lookup_filter = graphene.String()
    include = graphene.String()
    django_app = graphene.String()
    django_model = graphene.String()
    coupled_filters = graphene.List(CoupledFilterInput)


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
        def get_sub_queryset(
            filter_qualifier,
            filter_value,
            django_app,
            django_model,
            qualifier_field,
            value_field,
            upper_range_value_field,
        ):
            qualifier_field = qualifier_field + "__extended_name"

            if filter_qualifier == "lt":
                annot_condition = (
                    Q(**{qualifier_field: "traces"})
                    | Q(**{qualifier_field: "Less than"})
                    | Q(**{qualifier_field: "Less than or equal to"})
                    | (
                        (
                            Q(**{qualifier_field: "Greater than"})
                            | Q(**{qualifier_field: "Greater than or qual to"})
                            | Q(**{qualifier_field: "Equal to"})
                            | Q(**{qualifier_field: "Circa"})
                        )
                        & Q(**{value_field + "__lt": filter_value})
                    )
                )

            elif filter_qualifier == "gt":
                annot_condition = (
                    Q(**{qualifier_field: "traces"})
                    | Q(**{qualifier_field: "Greater than"})
                    | Q(**{qualifier_field: "Greater than or equal to"})
                    | (
                        (
                            Q(**{qualifier_field: "Less than"})
                            | Q(**{qualifier_field: "Less than or equal to"})
                            | Q(**{qualifier_field: "Equal to"})
                            | Q(**{qualifier_field: "Circa"})
                        )
                        & Q(**{value_field + "__gt": filter_value})
                    )
                )
                if upper_range_value_field:
                    annot_condition |= Q(
                        **{upper_range_value_field + "__gt": filter_value}
                    )

            elif filter_qualifier == "iexact":
                annot_condition = (
                    Q(**{qualifier_field: "traces"})
                    | (
                        (
                            Q(**{qualifier_field: "Equal to"})
                            | Q(**{qualifier_field: "Circa"})
                        )
                        & Q(**{value_field: filter_value})
                    )
                    | (
                        Q(**{qualifier_field: "Greater than"})
                        & Q(**{value_field + "__lt": filter_value})
                    )
                    | (
                        Q(**{qualifier_field: "Greater than or equal to"})
                        & (
                            Q(**{value_field: filter_value})
                            | Q(**{value_field + "__lt": filter_value})
                        )
                    )
                    | (
                        Q(**{qualifier_field: "Less than"})
                        & Q(**{value_field + "__gt": filter_value})
                    )
                    | (
                        Q(**{qualifier_field: "Less than or equal to"})
                        & (
                            Q(**{value_field: filter_value})
                            | Q(**{value_field + "__gt": filter_value})
                        )
                    )
                )
                if upper_range_value_field:
                    annot_condition |= Q(
                        **{upper_range_value_field + "__isnull": False}
                    ) & (
                        Q(**{value_field: filter_value})
                        | Q(**{upper_range_value_field: filter_value})
                        | (
                            Q(**{value_field + "__lt": filter_value})
                            & Q(**{upper_range_value_field + "__gt": filter_value})
                        )
                    )
            else:
                raise ValueError("Frontend has not send a supported filter_qualifier")

            annotation = {
                "include": Case(
                    When(annot_condition, then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField(),
                )
            }

            qs = (
                apps.get_model(django_app, django_model)
                .objects.annotate(**annotation)
                .filter(include=True)
            )
            return qs

        def create_q_object(lookup_field, filter_qualifier, filter_value):
            lookup = f"{lookup_field}__{filter_qualifier}"
            print("lookup: filter_value", f"{lookup}: {filter_value}")
            return Q(**{lookup: filter_value})

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

        nf_qs = NovelFood.objects.all()

        print("filters")
        print(filters)

        map = {
            "is before": "lt",
            "is after": "gt",
            "is": "iexact",
            "contains": "icontains",
            "is None": "isnull",
            "is greater than": "gt",
            "is less than": "lt",
        }

        for f in filters:
            lookup_filter = f.get("django_lookup_filter")
            include = f.get("include", None)
            django_app = f.get("django_app", None)
            django_model = f.get("django_model", None)

            model = NovelFood
            # todo: decide whether this prest of NovelFood model will be set here in backnd or
            # todo: in frontend
            if django_app and django_model:
                model = apps.get_model(django_app, django_model)

            qs = model.objects.all()

            for coup_f in f.get("coupled_filters"):
                field_type = coup_f.get("field_type", None)
                filter_qualifier = map[coup_f.get("qualifier")]
                filter_value = coup_f.get("value", None)
                lookup_field = coup_f.get("django_lookup_field", None)
                if lookup_field.startswith(lookup_filter):
                    # Remove lookup_filter from lookup_field
                    lookup_field = lookup_field[len(lookup_filter) :]
                    lookup_field = lookup_field.lstrip("_")

                value_fields = coup_f.get("value_fields", None)
                if value_fields:
                    django_app = value_fields.get("django_app", None)
                    django_model = value_fields.get("django_model", None)
                    qualifier_field = value_fields.get("qualifier_field", None)
                    value_field = value_fields.get("value_field", None)
                    upper_range_value_field = value_fields.get(
                        "upper_range_value_field", None
                    )
                else:
                    django_app = None
                    django_model = None
                    qualifier_field = None
                    value_field = None
                    upper_range_value_field = None

                # for taxonomy node fields
                if field_type == "tax_node":
                    # values offered in frontend are:
                    # TaxonomyNode.short_name values or
                    # TaxonomyNode.extended_name values if TaxonomyNode.short_name is empty,
                    # therefore here we match incomming filter_value with TaxonomyNode.short_name or
                    # with TaxonomyNode.extended_name if TaxonomyNode.short_name is empty
                    if filter_qualifier == "isnull":
                        q_object = create_isnull_or_isempty_q_object(lookup_field)
                    else:
                        short_name_lookup = (
                            f"{lookup_field}__short_name__{filter_qualifier}"
                        )
                        extended_name_lookup = (
                            f"{lookup_field}__extended_name__{filter_qualifier}"
                        )
                        q_object = (Q(**{short_name_lookup: filter_value})) | (
                            (
                                Q(**{f"{lookup_field}__short_name__isnull": True})
                                | Q(**{f"{lookup_field}__short_name": ""})
                            )
                            & Q(**{extended_name_lookup: filter_value})
                        )

                # for fields which are django.db.models.TextField
                elif field_type == "text_field":
                    if filter_qualifier == "isnull":
                        q_object = create_isnull_or_isempty_q_object(lookup_field)
                        q_object |= Q(**{lookup_field + "__exact": ""})
                    else:
                        q_object = create_q_object(
                            lookup_field, filter_qualifier, filter_value
                        )

                # value fields
                elif field_type == "value_field":
                    if filter_qualifier == "isnull":
                        q_object = create_isnull_or_isempty_q_object(lookup_field)
                    else:
                        sub_queryset = get_sub_queryset(
                            filter_qualifier,
                            filter_value,
                            django_app,
                            django_model,
                            qualifier_field,
                            value_field,
                            upper_range_value_field,
                        )
                        if lookup_field.endswith(f"__{value_field}"):
                            lookup_field = lookup_field[: -len(f"__{value_field}")]

                        q_object = Q(**{f"{lookup_field}__in": sub_queryset})

                # for all other fields
                else:
                    if filter_qualifier == "isnull":
                        q_object = create_isnull_or_isempty_q_object(lookup_field)
                    else:
                        q_object = create_q_object(
                            lookup_field, filter_qualifier, filter_value
                        )

                print("q_object", q_object)
                qs = qs.filter(q_object).distinct()

                if model == NovelFood:
                    if include == "must have":
                        # nf_qs becomes intersection of nf_qs and qs
                        nf_qs = nf_qs.filter(pk__in=qs.values_list("pk", flat=True))

                    elif include == "must not have":
                        # nf_qs becomes nf_qs difference from qs
                        nf_qs = nf_qs.exclude(pk__in=qs.values_list("pk", flat=True))

            if model != NovelFood:
                if include == "must have":
                    nf_qs = nf_qs.filter(Q(**{f"{lookup_filter}__in": qs})).distinct()
                elif include == "must not have":
                    nf_qs = nf_qs.exclude(Q(**{f"{lookup_filter}__in": qs})).distinct()
        print("QUERYSET: ", nf_qs)
        return nf_qs


schema = graphene.Schema(query=Query)
