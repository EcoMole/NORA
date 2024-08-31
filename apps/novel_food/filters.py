import django_filters

from .models import NovelFood


def get_fileld_name(field_name):
    field_name = (
        "opinion__adoption_date"
        if field_name == "opinion_adoption_date"
        else field_name
    )
    field_name = (
        "opinion__publication_date"
        if field_name == "opinion_publication_date"
        else field_name
    )
    return field_name


class NullableBooleanFilter(django_filters.BooleanFilter):
    def filter(self, qs, value):
        field_name = get_fileld_name(self.field_name)
        if value is True or value is False:
            return qs.filter(**{f"{field_name}__isnull": value})
        return super().filter(qs, value)


class NovelFoodFilter(django_filters.FilterSet):
    class Meta:
        model = NovelFood
        fields = ["title", "nf_code", "tox_study_required", "genotox_final_outcome"]

    def __init__(self, *args, **kwargs):
        # not necessary, but useful for debugging
        super().__init__(*args, **kwargs)

    def default_filter_method(self, queryset, name, value):
        print("default_filter_method name: ", name)
        print("default_filter_method value: ", value)

        # Splitting the filter name to handle cases like 'nf_code_exact_include'
        name_parts = name.split("_")
        field_name = "_".join(
            name_parts[:-2]
        )  # Extract the actual field name (e.g., 'nf_code')
        lookup_type = name_parts[-2]  # Get the lookup type (e.g., 'exact')
        # todo get_fileld_name() should be more dynamic
        field_name = get_fileld_name(field_name)
        # Include or exclude based on filter type
        if name_parts[-1] == "include":
            return queryset.filter(**{f"{field_name}__{lookup_type}": value})
        elif name_parts[-1] == "exclude":
            return queryset.exclude(**{f"{field_name}__{lookup_type}": value})

    # nf_code
    nf_code_isnull = NullableBooleanFilter(field_name="nf_code", lookup_expr="isnull")
    nf_code_exact_include = django_filters.CharFilter(method="default_filter_method")
    nf_code_exact_exclude = django_filters.CharFilter(method="default_filter_method")
    nf_code_icontains_include = django_filters.CharFilter(
        method="default_filter_method"
    )
    nf_code_icontains_exclude = django_filters.CharFilter(
        method="default_filter_method"
    )

    # title
    title_isnull = NullableBooleanFilter(field_name="title", lookup_expr="isnull")
    title_exact_include = django_filters.CharFilter(method="default_filter_method")
    title_exact_exclude = django_filters.CharFilter(method="default_filter_method")
    title_icontains_include = django_filters.CharFilter(method="default_filter_method")
    title_icontains_exclude = django_filters.CharFilter(method="default_filter_method")

    # tox_study_required
    tox_study_required_isnull = NullableBooleanFilter(
        field_name="tox_study_required", lookup_expr="isnull"
    )
    tox_study_required_exact_include = django_filters.CharFilter(
        method="default_filter_method"
    )
    tox_study_required_exact_exclude = django_filters.CharFilter(
        method="default_filter_method"
    )

    # opinion_adoption_date
    opinion_adoption_date_isnull = NullableBooleanFilter(
        field_name="opinion_adoption_date", lookup_expr="isnull"
    )
    opinion_adoption_date_exact_include = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_adoption_date_exact_exclude = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_adoption_date_gt_include = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_adoption_date_gt_exclude = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_adoption_date_lt_include = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_adoption_date_lt_exclude = django_filters.CharFilter(
        method="default_filter_method"
    )

    # opinion_publication_date
    opinion_publication_date_isnull = NullableBooleanFilter(
        field_name="opinion_publication_date", lookup_expr="isnull"
    )
    opinion_publication_date_exact_include = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_publication_date_exact_exclude = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_publication_date_gt_include = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_publication_date_gt_exclude = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_publication_date_lt_include = django_filters.CharFilter(
        method="default_filter_method"
    )
    opinion_publication_date_lt_exclude = django_filters.CharFilter(
        method="default_filter_method"
    )

    # # genotox_final_outcome
    # genotox_final_outcome_exact_include = django_filters.CharFilter(
    #     field_name="genotox_final_outcome", lookup_expr="exact"
    # )
    # genotox_final_outcome_exact_exclude = django_filters.CharFilter(
    #     method="filter_genotox_final_outcome_exact_exclude"
    # )

    # def filter_genotox_final_outcome_exact_exclude(self, queryset, name, value):
    #     return queryset.exclude(genotox_final_outcome__exact=value)
