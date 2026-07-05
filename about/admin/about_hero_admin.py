from django.contrib import admin

from about.models import AboutHero


@admin.register(AboutHero)
class AboutHeroAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "eyebrow",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active", "updated_at")
    search_fields = ("title", "eyebrow", "description")
    readonly_fields = ("updated_at",)

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
            "Hero Media",
            {
                "fields": (
                    "image",
                    "image_alt",
                )
            },
        ),
        (
            "Hero Supporting Content",
            {
                "fields": (
                    "stats",
                    "highlights",
                ),
                "description": (
                    "Stats and highlights are stored as JSON lists."
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