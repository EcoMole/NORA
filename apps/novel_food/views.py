from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import NovelFood  # Replace with your model name


@api_view(["GET"])
def get_distinct_tox_study_required(request):
    distinct_values = NovelFood.objects.values_list(
        "tox_study_required", flat=True
    ).distinct()
    return Response(distinct_values)


@api_view(["GET"])
def get_distinct_genotox_final_outcome(request):
    distinct_values = NovelFood.objects.values_list(
        "genotox_final_outcome", flat=True
    ).distinct()
    return Response(distinct_values)
