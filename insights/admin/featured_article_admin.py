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
        "excerpt",
        "insight__title",
        "category__name",
    )

    list_editable = (
        "display_order",
        "is_featured",
        "is_active",
    )

    autocomplete_fields = (
        "category",
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

    fieldsets = (
        (
            "Article Information",
            {
                "fields": (
                    "insight",
                    "title",
                    "slug",
                    "category",
                    "excerpt",
                )
            },
        ),
        (
            "Media & Publication",
            {
                "fields": (
                    "cover_image",
                    "external_url",
                    "published_at",
                    "read_time_minutes",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_featured",
                    "is_active",
                )
            },
        ),
    )