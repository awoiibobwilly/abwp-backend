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
    items = serializers.SerializerMethodField()

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

    def get_items(self, obj):
        queryset = obj.items.filter(
            is_active=True,
        ).order_by(
            "display_order",
            "name",
        )
        return ResearchInterestSerializer(
            queryset,
            many=True,
        ).data