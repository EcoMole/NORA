import django_filters


class NovelFoodFilter(django_filters.FilterSet):
    # title
    title_exact_include = django_filters.CharFilter(
        field_name="title", lookup_expr="exact"
    )
    title_exact_exclude = django_filters.CharFilter(method="filter_title_exact_exclude")

    def filter_title_exact_exclude(self, queryset, name, value):
        return queryset.exclude(title__exact=value)

    title_icontains_include = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains"
    )

    title_icontains_exclude = django_filters.CharFilter(
        method="filter_title_icontains_exclude"
    )

    def filter_title_icontains_exclude(self, queryset, name, value):
        return queryset.exclude(title__icontains=value)

    # nf_code
    nf_code_exact_include = django_filters.CharFilter(
        field_name="nf_code", lookup_expr="exact"
    )
    nf_code_exact_exclude = django_filters.CharFilter(
        method="filter_nf_code_exact_exclude"
    )

    def filter_nf_code_exact_exclude(self, queryset, name, value):
        return queryset.exclude(nf_code__exact=value)

    nf_code_icontains_include = django_filters.CharFilter(
        field_name="nf_code", lookup_expr="icontains"
    )

    nf_code_icontains_exclude = django_filters.CharFilter(
        method="filter_nf_code_icontains_exclude"
    )

    def filter_nf_code_icontains_exclude(self, queryset, name, value):
        return queryset.exclude(nf_code__icontains=value)

    # tox_study_required
    tox_study_required_exact_include = django_filters.CharFilter(
        field_name="tox_study_required", lookup_expr="exact"
    )
    tox_study_required_exact_exclude = django_filters.CharFilter(
        method="filter_tox_study_required_exact_exclude"
    )

    def filter_tox_study_required_exact_exclude(self, queryset, name, value):
        return queryset.exclude(tox_study_required__exact=value)
