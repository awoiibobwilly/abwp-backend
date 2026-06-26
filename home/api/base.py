from rest_framework import generics

from .pagination import PortfolioPagination

from .permissions import PublicPermission


class PublicListAPIView(
    generics.ListAPIView,
):
    """
    Base public list endpoint.
    """

    permission_classes = (
        PublicPermission,
    )

    authentication_classes = ()

    pagination_class = PortfolioPagination


class PublicRetrieveAPIView(
    generics.RetrieveAPIView,
):
    """
    Base public detail endpoint.
    """

    permission_classes = (
        PublicPermission,
    )

    authentication_classes = ()

    lookup_field = "slug"