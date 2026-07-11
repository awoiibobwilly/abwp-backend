from django.contrib import admin

from insights.models import InsightPageHero

from .hero_stat_admin import InsightHeroStatInline


# ==========================================================
# INSIGHT PAGE HERO ADMIN
# ==========================================================

@admin.register(
    InsightPageHero
)
class InsightPageHeroAdmin(
    admin.ModelAdmin
):

    list_display = (
        "insight",
        "eyebrow",
        "title",
    )

    search_fields = (
        "insight__title",
        "eyebrow",
        "title",
        "subtitle",
    )

    inlines = [
        InsightHeroStatInline,
    ]