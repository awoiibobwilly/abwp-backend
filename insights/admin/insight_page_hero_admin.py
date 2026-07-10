from django.contrib import admin
from insights.models import InsightPageHero


# ==========================================================
# INSIGHT PAGE HERO ADMIN
# ==========================================================

@admin.register(InsightPageHero)
class InsightPageHeroAdmin(admin.ModelAdmin):
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