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


@api_view(["GET"])
def get_novel_food_values_list(request):
    # Get parameters from request
    django_model = request.query_params.get("djangoModel")
    django_field = request.query_params.get("djangoField")

    # Dynamically get the model
    try:
        model = apps.get_model("novel_food", django_model)
    except LookupError:
        return Response({"error": "Model not found."}, status=400)

    # Ensure the field exists on the model
    if not hasattr(model, django_field):
        return Response(
            {"error": f"Field {django_field} not found on model {django_model}."},
            status=400,
        )

    # Query the distinct values of the field dynamically
    distinct_values = model.objects.values_list(django_field, flat=True).distinct()
    print("distinct_values")
    print(distinct_values)

    return Response(distinct_values)
