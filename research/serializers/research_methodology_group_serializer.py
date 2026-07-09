from rest_framework import serializers
from ..models import (
    ResearchMethodologyGroup,
    ResearchMethodologyItem,
)


class ResearchMethodologyItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResearchMethodologyItem
        fields = (
            "id",
            "name",
            "display_order",
        )


class ResearchMethodologyGroupSerializer(serializers.ModelSerializer):
    items = ResearchMethodologyItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = ResearchMethodologyGroup
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "icon",
            "display_order",
            "items",
        )