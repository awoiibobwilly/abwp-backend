from rest_framework import serializers

from about.models import AboutHero


class AboutHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHero
        fields = [
            "id",
            "eyebrow",
            "title",
            "description",
            "image",
            "image_alt",
            "stats",
            "highlights",
            "is_active",
            "updated_at",
        ]