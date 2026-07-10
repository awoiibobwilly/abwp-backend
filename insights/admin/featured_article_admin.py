from django.contrib import admin
from insights.models import FeaturedArticle


# ==========================================================
# FEATURED ARTICLE ADMIN
# ==========================================================

@admin.register(FeaturedArticle)
class FeaturedArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "insight",
        "category",
        "published_at",
        "display_order",
        "is_featured",
        "is_active",
    )
    list_filter = (
        "insight",
        "category",
        "is_featured",
        "is_active",
        "published_at",
    )
    search_fields = (
        "title",
        "slug",
        "category",
        "excerpt",
        "insight__title",
    )
    list_editable = (
        "display_order",
        "is_featured",
        "is_active",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }
    ordering = (
        "insight",
        "display_order",
        "-published_at",
        "title",
    )