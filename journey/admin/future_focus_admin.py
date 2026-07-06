from django.contrib import admin

from journey.models import FutureFocus


@admin.register(FutureFocus)
class FutureFocusAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "icon",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "title",
        "description",
        "icon",
    )

    ordering = (
        "display_order",
        "id",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Future Focus Content",
            {
                "fields": (
                    "title",
                    "description",
                    "icon",
                    "display_order",
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