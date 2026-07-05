from django.contrib import admin

from about.models import WhoIAm


@admin.register(WhoIAm)
class WhoIAmAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "display_order",
        "is_active",
    )
    list_editable = (
        "display_order",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("title", "description", "icon")
    ordering = ("display_order", "id")

    fieldsets = (
        (
            "Who I Am Item",
            {
                "fields": (
                    "title",
                    "description",
                    "icon",
                )
            },
        ),
        (
            "Display Settings",
            {
                "fields": (
                    "display_order",
                    "is_active",
                )
            },
        ),
    )