from django.contrib import admin

from journey.models import JourneyHero


@admin.register(JourneyHero)
class JourneyHeroAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "eyebrow",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "title",
        "eyebrow",
        "description",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Journey Hero Content",
            {
                "fields": (
                    "eyebrow",
                    "title",
                    "description",
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