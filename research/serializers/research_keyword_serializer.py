from rest_framework import serializers

from ..models import ResearchKeyword


class ResearchKeywordSerializer(serializers.ModelSerializer):

    class Meta:

        model = ResearchKeyword

        fields = (

            "id",

            "name",

            "slug",

            "icon",

            "color",

        )