from django.contrib import admin

from about.models import SkillCategory


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "display_order",
        "is_active",
    )
    list_editable = (
        "display_order",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("title",)
    ordering = ("display_order", "id")

    fieldsets = (
        (
            "Skill Category",
            {
                "fields": (
                    "title",
                    "skills",
                ),
                "description": (
                    "Skills should be stored as a JSON list of strings."
                ),
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