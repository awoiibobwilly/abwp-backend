import django_filters

from .models import Project


class ProjectFilter(django_filters.FilterSet):

    category = django_filters.CharFilter(

        field_name="category__slug",

        lookup_expr="iexact",

    )

    technology = django_filters.CharFilter(

        field_name="technologies__slug",

        lookup_expr="iexact",

    )

    status = django_filters.CharFilter(

        lookup_expr="iexact",

    )

    featured = django_filters.BooleanFilter()

    open_source = django_filters.BooleanFilter(

        field_name="is_open_source",

    )

    class Meta:

        model = Project

        fields = (
            "category",
            "technology",
            "status",
            "featured",
            "open_source",
        )