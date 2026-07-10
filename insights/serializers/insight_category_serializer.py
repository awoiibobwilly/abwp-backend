from rest_framework import serializers
from insights.models import InsightCategory


# ==========================================================
# INSIGHT CATEGORY SERIALIZER
# ==========================================================

class InsightCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsightCategory
        fields = [
            "id",
            "name",
            "slug",
            "display_order",
        ]