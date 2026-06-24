from rest_framework import generics

from .models import Statistic

from .serializers import StatisticSerializer


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
