from django.contrib import admin

from about.models import CoreValues


@admin.register(CoreValues)
class CoreValuesAdmin(admin.ModelAdmin):
    list_display = (
        "section_title",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active", "updated_at")
    search_fields = (
        "section_title",
        "section_description",
        "mission_title",
        "mission_description",
        "vision_title",
        "vision_description",
    )
    readonly_fields = ("updated_at",)

    fieldsets = (
        (
            "Section Intro",
            {
                "fields": (
                    "section_title",
                    "section_description",
                )
            },
        ),
        (
            "Mission",
            {
                "fields": (
                    "mission_title",
                    "mission_description",
                )
            },
        ),
        (
            "Vision",
            {
                "fields": (
                    "vision_title",
                    "vision_description",
                )
            },
        ),
        (
            "Values",
            {
                "fields": ("values",),
                "description": (
                    "Values should be stored as a JSON list of objects."
                ),
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "is_active",
                    "updated_at",
                )
            },
        ),
    )