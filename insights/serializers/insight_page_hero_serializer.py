from rest_framework import serializers
from insights.models import InsightPageHero


# ==========================================================
# INSIGHT PAGE HERO SERIALIZER
# ==========================================================

class InsightPageHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsightPageHero
        fields = [
            "eyebrow",
            "title",
            "subtitle",
        ]