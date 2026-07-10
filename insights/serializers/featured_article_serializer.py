from rest_framework import serializers
from insights.models import FeaturedArticle


# ==========================================================
# FEATURED ARTICLE SERIALIZER
# ==========================================================

class FeaturedArticleSerializer(serializers.ModelSerializer):
    cover_image_url = serializers.SerializerMethodField()
    published_date = serializers.SerializerMethodField()

    class Meta:
        model = FeaturedArticle
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "excerpt",
            "cover_image_url",
            "read_time",
            "published_date",
            "external_url",
            "is_featured",
            "display_order",
        ]

    def get_cover_image_url(self, obj):
        request = self.context.get("request")
        if obj.cover_image:
            if request:
                return request.build_absolute_uri(obj.cover_image.url)
            return obj.cover_image.url
        return None

    def get_published_date(self, obj):
        if obj.published_at:
            return obj.published_at.strftime("%B %Y")
        return ""