from django.contrib import admin

from insights.models import InsightHeroStat


# ==========================================================
# INSIGHT HERO STAT INLINE
# ==========================================================

class InsightHeroStatInline(
    admin.TabularInline
):

    model = InsightHeroStat

    extra = 1

    ordering = (
        "display_order",
    )

    fields = (
        "value",
        "label",
        "display_order",
        "is_active",
    )