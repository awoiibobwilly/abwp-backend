from rest_framework import serializers

from about.models import ProfessionalDNA


class ProfessionalDNASerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalDNA
        fields = [
            "id",
            "title",
            "description",
            "icon",
            "highlights",
            "display_order",
            "is_active",
        ]