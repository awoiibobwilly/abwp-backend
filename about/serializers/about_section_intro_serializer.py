from rest_framework import serializers

from about.models import AboutSectionIntro


class AboutSectionIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSectionIntro
        fields = [
            "id",
            "section_key",
            "eyebrow",
            "title",
            "intro",
            "is_active",
            "updated_at",
        ]