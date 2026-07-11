from rest_framework import serializers

from insights.models import InsightCategory


class InsightCategorySerializer(
    serializers.ModelSerializer
):
    article_count = serializers.SerializerMethodField()

    class Meta:
        model = InsightCategory

        fields = (
            "id",
            "name",
            "slug",
            "description",
            "accent_color",
            "article_count",
        )

    def get_article_count(self, obj):
        return obj.featured_articles.filter(
            is_active=True
        ).count()
		