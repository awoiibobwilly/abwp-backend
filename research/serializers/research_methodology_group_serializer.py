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
    items = serializers.SerializerMethodField()

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

    def get_items(self, obj):
        queryset = obj.items.filter(
            is_active=True,
        ).order_by(
            "display_order",
            "name",
        )
        return ResearchMethodologyItemSerializer(
            queryset,
            many=True,
        ).data