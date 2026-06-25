from rest_framework import generics

from .models import Expertise

from .models import Statistic

from .models import Highlight

from .serializers import StatisticSerializer

from .serializers import ExpertiseSerializer

from .serializers import HighlightSerializer


class StatisticListView(

    generics.ListAPIView

):

    serializer_class = StatisticSerializer

    def get_queryset(

        self

    ):

        return Statistic.objects.filter(

            is_active=True

        )


class ExpertiseListView(

    generics.ListAPIView

):

    serializer_class = ExpertiseSerializer

    queryset = Expertise.objects.filter(

        is_active=True

    ).order_by(

        "display_order"

    )


class HighlightListView(

    generics.ListAPIView

):

    serializer_class = HighlightSerializer

    queryset = Highlight.objects.filter(

        is_active=True

    ).order_by(

        "display_order"

    )