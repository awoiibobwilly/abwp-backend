from rest_framework import serializers

from insights.models import FeaturedArticle

from .insight_category_serializer import (
    InsightCategorySerializer,
)


class FeaturedArticleSerializer(
    serializers.ModelSerializer
):
    category = InsightCategorySerializer(
        read_only=True
    )

    read_time = serializers.SerializerMethodField()

    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = FeaturedArticle

        fields = (
            "id",
            "title",
            "slug",
            "category",
            "excerpt",
            "cover_image",
            "read_time",
            "published_at",
            "external_url",
        )

    def get_read_time(self, obj):
        return f"{obj.read_time_minutes} min read"

    def get_cover_image(self, obj):
        request = self.context.get("request")

        if not obj.cover_image:
            return None

        if request:
            return request.build_absolute_uri(
                obj.cover_image.url
            )

        return obj.cover_image.url
		