from rest_framework import serializers

from .models import Statistic


from .models import Expertise


class StatisticSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Statistic

        fields = "__all__"


class ExpertiseSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Expertise

        fields = "__all__"


