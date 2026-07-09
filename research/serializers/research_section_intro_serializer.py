from rest_framework import serializers
from ..models import ResearchSectionIntro


class ResearchSectionIntroSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResearchSectionIntro
        fields = (
            "id",
            "section_key",
            "eyebrow",
            "title",
            "intro",
        )