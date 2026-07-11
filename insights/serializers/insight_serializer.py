from rest_framework import serializers

from insights.models import Insight

from .featured_article_serializer import (
    FeaturedArticleSerializer,
)
from .insight_category_serializer import (
    InsightCategorySerializer,
)
from .insight_hero_stat_serializer import (
    InsightHeroStatSerializer,
)
from .insight_page_hero_serializer import (
    InsightPageHeroSerializer,
)
from .insight_section_intro_serializer import (
    InsightSectionIntroSerializer,
)
from .newsletter_serializer import (
    NewsletterSerializer,
)
from .quote_serializer import (
    QuoteSerializer,
)
from .thought_serializer import (
    ThoughtSerializer,
)


class InsightSerializer(
    serializers.ModelSerializer
):
    hero = InsightPageHeroSerializer(
        read_only=True
    )

    hero_stats = InsightHeroStatSerializer(
        many=True,
        source="hero.stats",
        read_only=True,
    )

    section_intros = InsightSectionIntroSerializer(
        many=True,
        read_only=True,
    )

    categories = InsightCategorySerializer(
        many=True,
        read_only=True,
    )

    featured_articles = FeaturedArticleSerializer(
        many=True,
        read_only=True,
    )

    thoughts = ThoughtSerializer(
        many=True,
        read_only=True,
    )

    quotes = QuoteSerializer(
        many=True,
        read_only=True,
    )

    newsletter = NewsletterSerializer(
        read_only=True,
    )

    class Meta:
        model = Insight

        fields = (
            "id",
            "title",
            "hero",
            "hero_stats",
            "section_intros",
            "categories",
            "featured_articles",
            "thoughts",
            "quotes",
            "newsletter",
        )