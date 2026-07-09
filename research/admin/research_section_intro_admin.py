from django.contrib import admin
from ..models import ResearchSectionIntro


@admin.register(ResearchSectionIntro)
class ResearchSectionIntroAdmin(admin.ModelAdmin):

    list_display = (
        "section_key",
        "title",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "section_key",
        "is_active",
    )

    search_fields = (
        "title",
        "eyebrow",
        "intro",
    )

    list_editable = (
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Section Intro",
            {
                "fields": (
                    "section_key",
                    "eyebrow",
                    "title",
                    "intro",
                )
            },
        ),
        (
            "Display",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
        (
            "Audit",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )