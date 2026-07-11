from rest_framework import serializers

from insights.models import Quote


class QuoteSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Quote

        fields = (
            "id",
            "quote",
            "author",
            "display_order",
        )