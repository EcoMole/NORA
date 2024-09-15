import django_filters
from novel_food.models import NovelFood


class NovelFoodFilter(django_filters.FilterSet):
    title_exact_include = django_filters.CharFilter(
        field_name="title", lookup_expr="exact"
    )
    title_icontains_include = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains"
    )

    # Exclusion filters
    title_exact_exclude = django_filters.CharFilter(method="filter_title_exact_exclude")
    title_icontains_exclude = django_filters.CharFilter(
        method="filter_title_icontains_exclude"
    )

    class Meta:
        model = NovelFood
        fields = ["title"]

    def filter_title_exact_exclude(self, queryset, name, value):
        return queryset.exclude(title__exact=value)

    def filter_title_icontains_exclude(self, queryset, name, value):
        return queryset.exclude(title__icontains=value)
