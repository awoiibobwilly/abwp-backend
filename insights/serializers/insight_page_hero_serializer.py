from rest_framework import serializers

from insights.models import InsightPageHero

from .insight_hero_stat import InsightHeroStatSerializer


# ==========================================================
# INSIGHT PAGE HERO SERIALIZER
# ==========================================================

class InsightPageHeroSerializer(
    serializers.ModelSerializer
):

    stats = InsightHeroStatSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = InsightPageHero

        fields = (
            "id",
            "eyebrow",
            "title",
            "description",
            "stats",
        )