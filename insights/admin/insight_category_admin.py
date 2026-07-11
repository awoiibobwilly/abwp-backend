from django.contrib import admin

from insights.models import InsightCategory


@admin.register(InsightCategory)
class InsightCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "display_order",
        "accent_color",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    list_editable = (
        "display_order",
        "accent_color",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "display_order",
        "name",
    )