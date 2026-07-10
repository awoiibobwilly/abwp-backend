from rest_framework import serializers

from insights.models import Insight
from insights.serializers.insight_page_hero_serializer import (
    InsightPageHeroSerializer,
)
from insights.serializers.insight_section_intro_serializer import (
    InsightSectionIntroSerializer,
)
from insights.serializers.insight_category_serializer import (
    InsightCategorySerializer,
)
from insights.serializers.featured_article_serializer import (
    FeaturedArticleSerializer,
)
from insights.serializers.thought_serializer import ThoughtSerializer
from insights.serializers.quote_serializer import QuoteSerializer
from insights.serializers.newsletter_serializer import NewsletterSerializer


# ==========================================================
# INSIGHT PAGE SERIALIZER
# FULL INSIGHTS PAGE PAYLOAD
# ==========================================================

class InsightSerializer(serializers.ModelSerializer):
    hero = serializers.SerializerMethodField()
    featured_intro = serializers.SerializerMethodField()
    featured_articles = serializers.SerializerMethodField()
    categories_intro = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    thoughts_intro = serializers.SerializerMethodField()
    latest_thoughts = serializers.SerializerMethodField()
    quotes_intro = serializers.SerializerMethodField()
    quotes = serializers.SerializerMethodField()
    newsletter = serializers.SerializerMethodField()

    class Meta:
        model = Insight
        fields = [
            "id",
            "title",
            "slug",
            "hero",
            "featured_intro",
            "featured_articles",
            "categories_intro",
            "categories",
            "thoughts_intro",
            "latest_thoughts",
            "quotes_intro",
            "quotes",
            "newsletter",
        ]

    # ======================================================
    # HERO
    # ======================================================

    def get_hero(self, obj):
        if hasattr(obj, "hero") and obj.hero:
            return InsightPageHeroSerializer(
                obj.hero,
                context=self.context
            ).data
        return None

    # ======================================================
    # SECTION INTRO HELPERS
    # ======================================================

    def _get_section_intro(self, obj, section_key):
        intro = obj.section_intros.filter(
            section_key=section_key
        ).first()

        if intro:
            return InsightSectionIntroSerializer(
                intro,
                context=self.context
            ).data

        return None

    # ======================================================
    # FEATURED ARTICLES
    # ======================================================

    def get_featured_intro(self, obj):
        return self._get_section_intro(
            obj,
            "featured_articles"
        )

    def get_featured_articles(self, obj):
        articles = obj.featured_articles.filter(
            is_active=True,
            is_featured=True
        ).order_by("display_order", "-published_at", "title")

        return FeaturedArticleSerializer(
            articles,
            many=True,
            context=self.context
        ).data

    # ======================================================
    # CATEGORIES
    # ======================================================

    def get_categories_intro(self, obj):
        return self._get_section_intro(
            obj,
            "categories"
        )

    def get_categories(self, obj):
        categories = obj.categories.filter(
            is_active=True
        ).order_by("display_order", "name")

        return InsightCategorySerializer(
            categories,
            many=True,
            context=self.context
        ).data

    # ======================================================
    # THOUGHTS
    # ======================================================

    def get_thoughts_intro(self, obj):
        return self._get_section_intro(
            obj,
            "thoughts"
        )

    def get_latest_thoughts(self, obj):
        thoughts = obj.thoughts.filter(
            is_active=True
        ).order_by("display_order", "-published_at", "title")

        return ThoughtSerializer(
            thoughts,
            many=True,
            context=self.context
        ).data

    # ======================================================
    # QUOTES
    # ======================================================

    def get_quotes_intro(self, obj):
        return self._get_section_intro(
            obj,
            "quotes"
        )

    def get_quotes(self, obj):
        quotes = obj.quotes.filter(
            is_active=True
        ).order_by("display_order", "id")

        return QuoteSerializer(
            quotes,
            many=True,
            context=self.context
        ).data

    # ======================================================
    # NEWSLETTER
    # ======================================================

    def get_newsletter(self, obj):
        if hasattr(obj, "newsletter") and obj.newsletter and obj.newsletter.is_active:
            return NewsletterSerializer(
                obj.newsletter,
                context=self.context
            ).data
        return None