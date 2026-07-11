from rest_framework import serializers

from insights.models import Thought


class ThoughtSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Thought

        fields = (
            "id",
            "title",
            "content",
            "display_order",
        )