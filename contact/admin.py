from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "subject",
        "message",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20

    fieldsets = (

        ("Sender Information", {

            "fields": (
                "full_name",
                "email",
            )

        }),

        ("Message Details", {

            "fields": (
                "subject",
                "message",
            )

        }),

        ("Status", {

            "fields": (
                "is_read",
                "created_at",
            )

        }),

    )
