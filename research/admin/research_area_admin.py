from django.contrib import admin
from ..models import ResearchArea


@admin.register(ResearchArea)
class ResearchAreaAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "slug",
    )

    ordering = (
        "display_order",
        "title",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "display_order",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Research Area",
            {
                "fields": (
                    "title",
                    "slug",
                    "description",
                )
            },
        ),
        (
            "Appearance",
            {
                "fields": (
                    "icon",
                    "accent_color",
                )
            },
        ),
        (
            "Display",
            {
                "fields": (
                    "display_order",
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