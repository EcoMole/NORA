import django_filters
from novel_food.models import NovelFood


class NovelFoodFilter(django_filters.FilterSet):
    title_exact = django_filters.CharFilter(field_name="title", lookup_expr="exact")
    title_icontains = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains"
    )
    title_startswith = django_filters.CharFilter(
        field_name="title", lookup_expr="startswith"
    )

    class Meta:
        model = NovelFood
        fields = ["title"]  # Specify other fields
