from rest_framework import serializers
from insights.models import Thought


# ==========================================================
# THOUGHT SERIALIZER
# ==========================================================

class ThoughtSerializer(serializers.ModelSerializer):
    published_date = serializers.SerializerMethodField()

    class Meta:
        model = Thought
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "excerpt",
            "published_date",
            "external_url",
            "display_order",
        ]

    def get_published_date(self, obj):
        if obj.published_at:
            return obj.published_at.strftime("%B %Y")
        return ""