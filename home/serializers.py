from rest_framework import serializers

from .models import Statistic

from .models import Expertise

from .models import Highlight

from .models import Technology


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


class HighlightSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Highlight

        fields = "__all__"


class TechnologySerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Technology

        fields = "__all__"