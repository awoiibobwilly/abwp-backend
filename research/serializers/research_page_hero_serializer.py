from rest_framework import serializers
from ..models import ResearchPageHero


class ResearchPageHeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResearchPageHero
        fields = (
            "id",
            "eyebrow",
            "title",
            "description",
        )