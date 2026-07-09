from django.contrib import admin
from ..models import ResearchPhilosophyPoint


@admin.register(ResearchPhilosophyPoint)
class ResearchPhilosophyPointAdmin(admin.ModelAdmin):

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
    )

    ordering = (
        "display_order",
        "title",
    )

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
            "Philosophy Point",
            {
                "fields": (
                    "title",
                    "description",
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