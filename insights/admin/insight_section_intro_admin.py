from django.contrib import admin
from insights.models import InsightSectionIntro


# ==========================================================
# INSIGHT SECTION INTRO ADMIN
# ==========================================================

@admin.register(InsightSectionIntro)
class InsightSectionIntroAdmin(admin.ModelAdmin):
    list_display = (
        "insight",
        "section_key",
        "title",
        "display_order",
    )
    list_filter = (
        "section_key",
    )
    search_fields = (
        "insight__title",
        "eyebrow",
        "title",
        "intro",
    )
    ordering = (
        "insight",
        "display_order",
        "id",
    )