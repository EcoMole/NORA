from django.urls import path

from .views import get_distinct_genotox_final_outcome, get_distinct_tox_study_required

app_name = "novel_food"

urlpatterns = [
    path(
        "tox-study-required/",
        get_distinct_tox_study_required,
        name="get_distinct_tox_study_required",
    ),
    path(
        "genotox-final-outcome/",
        get_distinct_genotox_final_outcome,
        name="get_distinct_genotox_final_outcome",
    ),
]
