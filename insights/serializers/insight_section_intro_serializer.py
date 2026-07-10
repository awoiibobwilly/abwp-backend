from rest_framework import serializers
from insights.models import InsightSectionIntro


# ==========================================================
# INSIGHT SECTION INTRO SERIALIZER
# ==========================================================

class InsightSectionIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsightSectionIntro
        fields = [
            "section_key",
            "eyebrow",
            "title",
            "intro",
            "display_order",
        ]