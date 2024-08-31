from django.urls import path

from .views import get_novel_food_values_list

app_name = "novel_food"

urlpatterns = [
    path(
        "novel-food-values-list/",
        get_novel_food_values_list,
        name="get_novel_food_values_list",
    ),
]
