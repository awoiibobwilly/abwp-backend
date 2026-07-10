from rest_framework import serializers
from insights.models import Newsletter


# ==========================================================
# NEWSLETTER SERIALIZER
# ==========================================================

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = [
            "eyebrow",
            "title",
            "description",
            "placeholder",
            "button_text",
        ]