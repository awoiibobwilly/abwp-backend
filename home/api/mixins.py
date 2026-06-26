from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)


class FeaturedQuerysetMixin:
    """
    Return featured objects only.
    """

    featured_field = "featured"

    def get_queryset(self):

        queryset = super().get_queryset()

        return queryset.filter(
            **{
                self.featured_field: True,
            }
        )


class ActiveQuerysetMixin:
    """
    Return active objects only.
    """

    active_field = "is_active"

    def get_queryset(self):

        queryset = super().get_queryset()

        return queryset.filter(
            **{
                self.active_field: True,
            }
        )


class OrderedQuerysetMixin:
    """
    Apply default ordering.
    """

    ordering = (
        "display_order",
        "-created_at",
    )

    def get_queryset(self):

        queryset = super().get_queryset()

        return queryset.order_by(
            *self.ordering
        )


class PortfolioFilterMixin:
    """
    Common filter backends.
    """

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )


class PortfolioOrderingMixin:
    """
    Shared ordering configuration.
    """

    ordering_fields = (
        "created_at",
        "updated_at",
        "display_order",
        "title",
    )

    ordering = (
        "display_order",
    )