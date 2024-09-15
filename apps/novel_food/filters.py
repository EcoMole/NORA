import django_filters
from novel_food.models import NovelFood


class NovelFoodFilter(django_filters.FilterSet):
    title_exact_filter = django_filters.CharFilter(
        field_name="title", lookup_expr="exact"
    )
    title_icontains_filter = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains"
    )

    # Exclusion filters
    title_exact_exclude = django_filters.CharFilter(method="filter_exclude_exact")
    title_icontains_exclude = django_filters.CharFilter(
        method="filter_exclude_icontains"
    )

    class Meta:
        model = NovelFood
        fields = ["title"]

    def filter_exclude_exact(self, queryset, name, value):
        return queryset.exclude(title__exact=value)

    def filter_exclude_icontains(self, queryset, name, value):
        return queryset.exclude(title__icontains=value)
