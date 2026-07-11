from rest_framework import serializers

from insights.models import InsightHeroStat


# ==========================================================
# INSIGHT HERO STAT SERIALIZER
# ==========================================================

class InsightHeroStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = InsightHeroStat

        fields = (
            "id",
            "value",
            "label",
            "display_order",
        )