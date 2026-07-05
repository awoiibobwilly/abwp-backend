from django.contrib import admin

from about.models import Credential


@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "institution",
        "group",
        "period",
        "display_order",
        "is_active",
    )
    list_editable = (
        "display_order",
        "is_active",
    )
    list_filter = ("group", "is_active")
    search_fields = ("title", "institution", "period", "note")
    ordering = ("group", "display_order", "id")

    fieldsets = (
        (
            "Credential Content",
            {
                "fields": (
                    "group",
                    "title",
                    "institution",
                    "period",
                    "note",
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