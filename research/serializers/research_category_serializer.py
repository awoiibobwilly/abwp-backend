from rest_framework import serializers

from ..models import ResearchCategory


class ResearchCategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = ResearchCategory

        fields = (

            "id",

            "name",

            "slug",

            "description",

            "icon",

            "color",

        )