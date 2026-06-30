from rest_framework import serializers

from ..models import Research

from .research_category_serializer import (
    ResearchCategorySerializer,
)

from .research_keyword_serializer import (
    ResearchKeywordSerializer,
)


class ResearchSerializer(serializers.ModelSerializer):

    category = ResearchCategorySerializer(
        read_only=True,
    )

    keywords = ResearchKeywordSerializer(
        many=True,
        read_only=True,
    )

    publication_type_display = serializers.CharField(

        source="get_publication_type_display",

        read_only=True,

    )

    featured_image = serializers.SerializerMethodField()

    pdf = serializers.SerializerMethodField()

    class Meta:

        model = Research

        fields = (

            "id",

            "title",

            "slug",

            "category",

            "publication_type",

            "authors",

            "institution",

            "journal",

            "publisher",

            "year",

            "summary",

            "abstract",

            "keywords",

            "featured_image",

            "pdf",

            "doi",

            "external_url",

            "status",

            "featured",
            
            "publication_type",

            "publication_type_display",

        )

    def get_featured_image(self, obj):

        request = self.context.get("request")

        if obj.featured_image:

            if request:

                return request.build_absolute_uri(
                    obj.featured_image.url
                )

            return obj.featured_image.url

        return None

    def get_pdf(self, obj):

        request = self.context.get("request")

        if obj.pdf:

            if request:

                return request.build_absolute_uri(
                    obj.pdf.url
                )

            return obj.pdf.url

        return None