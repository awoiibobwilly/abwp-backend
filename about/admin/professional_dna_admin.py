from django.contrib import admin

from about.models import ProfessionalDNA


@admin.register(ProfessionalDNA)
class ProfessionalDNAAdmin(admin.ModelAdmin):
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
            "Professional DNA Item",
            {
                "fields": (
                    "title",
                    "description",
                    "icon",
                    "highlights",
                ),
                "description": (
                    "Highlights should be stored as a JSON list."
                ),
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