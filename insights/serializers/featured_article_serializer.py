from rest_framework import serializers

from insights.models import FeaturedArticle

from .insight_category_serializer import (
    InsightCategorySerializer,
)


# ==========================================================
# FEATURED ARTICLE SERIALIZER
# ==========================================================

class FeaturedArticleSerializer(
    serializers.ModelSerializer
):
    category = InsightCategorySerializer(
        read_only=True
    )

    cover_image = serializers.SerializerMethodField()

    read_time = serializers.SerializerMethodField()

    class Meta:
        model = FeaturedArticle

        fields = (
            "id",
            "title",
            "slug",
            "category",
            "excerpt",
            "cover_image",
            "published_at",
            "read_time",
            "external_url",
        )

    def get_cover_image(self, obj):
        request = self.context.get("request")

        if not obj.cover_image:
            return None

        if request:
            return request.build_absolute_uri(
                obj.cover_image.url
            )

        return obj.cover_image.url

    def get_read_time(self, obj):
        return (
            f"{obj.read_time_minutes} min read"
        )