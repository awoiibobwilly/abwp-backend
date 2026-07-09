from django.contrib import admin
from ..models import ResearchPageHero


@admin.register(ResearchPageHero)
class ResearchPageHeroAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "eyebrow",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "eyebrow",
        "description",
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
            "Hero Content",
            {
                "fields": (
                    "eyebrow",
                    "title",
                    "description",
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