from django.contrib import admin
from insights.models import InsightCategory


# ==========================================================
# INSIGHT CATEGORY ADMIN
# ==========================================================

@admin.register(InsightCategory)
class InsightCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "insight",
        "slug",
        "display_order",
        "is_active",
    )
    list_filter = (
        "is_active",
        "insight",
    )
    search_fields = (
        "name",
        "slug",
        "insight__title",
    )
    list_editable = (
        "display_order",
        "is_active",
    )
    prepopulated_fields = {
        "slug": ("name",),
    }
    ordering = (
        "insight",
        "display_order",
        "name",
    )