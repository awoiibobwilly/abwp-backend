from rest_framework import serializers

from about.models import WhoIAm


class WhoIAmSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoIAm
        fields = [
            "id",
            "title",
            "description",
            "icon",
            "display_order",
            "is_active",
        ]