from django.contrib import admin

from journey.models import JourneySectionIntro


@admin.register(JourneySectionIntro)
class JourneySectionIntroAdmin(admin.ModelAdmin):
    list_display = (
        "section_key",
        "title",
        "eyebrow",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "section_key",
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "section_key",
        "title",
        "eyebrow",
        "intro",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Section Intro Content",
            {
                "fields": (
                    "section_key",
                    "eyebrow",
                    "title",
                    "intro",
                    "is_active",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": ("collapse",),
            },
        ),
    )