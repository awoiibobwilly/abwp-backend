from rest_framework import serializers
from journey.models import JourneyHero


class JourneyHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = JourneyHero
        fields = (
            "id",
            "eyebrow",
            "title",
            "description",
        )