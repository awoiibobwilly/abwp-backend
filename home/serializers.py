from rest_framework import serializers

from .models import (
    
    Statistic,
    
    Expertise,
    
    Highlight,
    
    Technology,

    ProjectCategory,

)


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

# ================================
    # PROJECT CATEGORY
# ================================


class ProjectCategorySerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = ProjectCategory

        fields = "__all__"