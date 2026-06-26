from rest_framework.pagination import PageNumberPagination


class PortfolioPagination(PageNumberPagination):
    """
    Default pagination for portfolio APIs.
    """

    page_size = 12

    page_size_query_param = "page_size"

    max_page_size = 50