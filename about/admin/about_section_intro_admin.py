from django.contrib import admin

from about.models import AboutSectionIntro


@admin.register(AboutSectionIntro)
class AboutSectionIntroAdmin(admin.ModelAdmin):
    list_display = (
        "section_key",
        "eyebrow",
        "title",
        "is_active",
        "updated_at",
    )
    list_filter = ("section_key", "is_active", "updated_at")
    search_fields = ("eyebrow", "title", "intro")
    readonly_fields = ("updated_at",)

    fieldsets = (
        (
            "Section Identification",
            {
                "fields": (
                    "section_key",
                    "is_active",
                )
            },
        ),
        (
            "Section Content",
            {
                "fields": (
                    "eyebrow",
                    "title",
                    "intro",
                )
            },
        ),
        (
            "System",
            {
                "fields": ("updated_at",)
            },
        ),
    )