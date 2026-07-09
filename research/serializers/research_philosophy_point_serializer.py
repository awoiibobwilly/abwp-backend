from rest_framework import serializers
from ..models import ResearchPhilosophyPoint


class ResearchPhilosophyPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResearchPhilosophyPoint
        fields = (
            "id",
            "title",
            "description",
            "icon",
            "accent_color",
            "display_order",
        )