from rest_framework import serializers

from insights.models import Thought


# ==========================================================
# THOUGHT SERIALIZER
# LATEST THOUGHTS
# ==========================================================

class ThoughtSerializer(serializers.ModelSerializer):

    class Meta:

        model = Thought

        fields = (

            "id",

            "title",

            "slug",

            "category",

            "excerpt",

            "published_at",

            "external_url",

            "display_order",

        )