from django.apps import apps
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(["GET"])
# def get_novel_food_values_list(request):
#     distinct_values = NovelFood.objects.values_list(
#         "tox_study_required", flat=True
#     ).distinct()
#     return Response(distinct_values)


# @api_view(["GET"])
# def get_distinct_genotox_final_outcome(request):
#     distinct_values = NovelFood.objects.values_list(
#         "genotox_final_outcome", flat=True
#     ).distinct()
#     return Response(distinct_values)


def get_choices_from_field(app_name, model_name, field_name):
    if not app_name or not model_name or not field_name:
        return None
    Model = apps.get_model(app_label=app_name, model_name=model_name)
    if not Model:
        raise ValueError(f"Model '{model_name}' in app '{app_name}' does not exist.")
    field = Model._meta.get_field(field_name)
    if hasattr(field, "choices"):
        print("field.choices: ", field.choices)
        return field.choices
    return None


def get_limit_choices_to(app_name, model_name, field_name):
    if not app_name or not model_name or not field_name:
        return None
    Model = apps.get_model(app_label=app_name, model_name=model_name)
    if not Model:
        raise ValueError(f"Model '{model_name}' in app '{app_name}' does not exist.")
    field = Model._meta.get_field(field_name)

    limit_choices_to = None
    if (
        hasattr(field, "remote_field")
        and field.remote_field
        and hasattr(field.remote_field, "limit_choices_to")
    ):
        limit_choices_to = field.remote_field.limit_choices_to
        print("field.remote_field.limit_choices_to: ", limit_choices_to)
    elif hasattr(field, "limit_choices_to"):
        limit_choices_to = field.limit_choices_to
        print("field.limit_choices_to: ", limit_choices_to)
    return limit_choices_to


@api_view(["GET"])
def get_novel_food_values_list(request):
    # Extract parameters
    django_app = request.query_params.get("djangoApp")
    django_model = request.query_params.get("djangoModel")
    django_field = request.query_params.get("djangoField")
    django_limitchoices_app = request.query_params.get("djangoLimitchoicesApp", None)
    django_limitchoices_model = request.query_params.get(
        "djangoLimitchoicesModel", None
    )
    django_limitchoices_field = request.query_params.get(
        "djangoLimitchoicesField", None
    )

    try:
        model = apps.get_model(django_app, django_model)
    except LookupError:
        return Response({"error": f"Model {django_model} not found."}, status=400)

    if not hasattr(model, django_field):
        return Response(
            {"error": f"Field {django_field} not found on model {django_model}."},
            status=400,
        )

    limit_choices = get_limit_choices_to(
        django_limitchoices_app, django_limitchoices_model, django_limitchoices_field
    )
    print("limit_choices: ", limit_choices)

    if limit_choices:
        qs = model.objects.filter(limit_choices)
    else:
        qs = model.objects.all()

    distinct_values = qs.order_by().values_list(django_field, flat=True).distinct()

    if django_field == "short_name" and hasattr(model, "extended_name"):
        if limit_choices:
            qs_extended = model.objects.filter(limit_choices)
        else:
            qs_extended = model.objects.all()
        distinct_values_extended = (
            qs_extended.order_by().values_list("extended_name", flat=True).distinct()
        )
        distinct_values = distinct_values.union(distinct_values_extended)

    if get_choices_from_field(django_app, django_model, django_field):
        res = [
            pair[0]
            for pair in get_choices_from_field(django_app, django_model, django_field)
        ]
        return Response(res)
    return Response(distinct_values)
