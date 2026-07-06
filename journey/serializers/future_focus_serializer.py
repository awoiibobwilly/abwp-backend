from rest_framework import serializers
from journey.models import FutureFocus


class FutureFocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FutureFocus
        fields = (
            "id",
            "title",
            "description",
            "icon",
            "display_order",
        )