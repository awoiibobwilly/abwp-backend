from rest_framework import serializers
from journey.models import JourneySectionIntro


class JourneySectionIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = JourneySectionIntro
        fields = (
            "id",
            "section_key",
            "eyebrow",
            "title",
            "intro",
        )