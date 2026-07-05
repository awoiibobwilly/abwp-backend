from rest_framework import serializers

from about.models import Credential


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = [
            "id",
            "group",
            "title",
            "institution",
            "period",
            "note",
            "display_order",
            "is_active",
        ]