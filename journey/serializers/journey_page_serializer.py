from rest_framework import serializers

from journey.serializers.journey_hero_serializer import JourneyHeroSerializer
from journey.serializers.journey_section_intro_serializer import (
    JourneySectionIntroSerializer,
)
from journey.serializers.future_focus_serializer import FutureFocusSerializer

from home.serializers import JourneySerializer


class JourneyPageSerializer(serializers.Serializer):
    hero = JourneyHeroSerializer(
        allow_null=True,
    )

    timeline_intro = JourneySectionIntroSerializer(
        allow_null=True,
    )

    timeline = JourneySerializer(
        many=True,
    )

    future_intro = JourneySectionIntroSerializer(
        allow_null=True,
    )

    future_focus = FutureFocusSerializer(
        many=True,
    )