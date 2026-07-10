from rest_framework import serializers
from insights.models import Quote


# ==========================================================
# QUOTE SERIALIZER
# ==========================================================

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = [
            "id",
            "quote",
            "author",
            "display_order",
        ]