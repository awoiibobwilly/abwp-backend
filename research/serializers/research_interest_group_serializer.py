from rest_framework import serializers
from ..models import (
    ResearchInterestGroup,
    ResearchInterest,
)


class ResearchInterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResearchInterest
        fields = (
            "id",
            "name",
            "display_order",
        )


class ResearchInterestGroupSerializer(serializers.ModelSerializer):
    items = ResearchInterestSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = ResearchInterestGroup
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "display_order",
            "items",
        )