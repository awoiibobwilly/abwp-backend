from django.contrib import admin

from about.models import SelectedAchievement


@admin.register(SelectedAchievement)
class SelectedAchievementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "year",
        "display_order",
        "is_active",
    )
    list_editable = (
        "display_order",
        "is_active",
    )
    list_filter = ("is_active", "category", "year")
    search_fields = ("title", "description", "category", "year")
    ordering = ("display_order", "id")

    fieldsets = (
        (
            "Achievement Content",
            {
                "fields": (
                    "title",
                    "description",
                    "category",
                    "year",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_active",
                )
            },
        ),
    )