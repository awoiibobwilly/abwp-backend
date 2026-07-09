from rest_framework import serializers
from ..models import ResearchArea


class ResearchAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResearchArea
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "icon",
            "accent_color",
            "display_order",
        )