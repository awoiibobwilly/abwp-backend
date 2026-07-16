from django.contrib import admin
from django.utils.html import format_html

from hub.models import LibraryResource


# ==========================================================
# LIBRARY RESOURCE ADMIN
# ==========================================================

@admin.register(LibraryResource)
class LibraryResourceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "resource_type",
        "author",
        "display_order",
        "is_active",
    )

    list_display_links = (
        "title",
    )

    search_fields = (
        "title",
        "summary",
        "author",
        "publisher",
    )

    list_filter = (
        "resource_type",
        "is_active",
    )

    ordering = (
        "display_order",
        "title",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    filter_horizontal = (
        "themes",
        "tags",
    )

    readonly_fields = (
        "cover_preview",
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "resource_type",
                )
            },
        ),

        (
            "Content",
            {
                "fields": (
                    "summary",
                    "description",
                )
            },
        ),

        (
            "Media",
            {
                "fields": (
                    "cover_image",
                    "cover_preview",
                    "resource_file",
                    "external_url",
                )
            },
        ),

        (
            "Publication",
            {
                "fields": (
                    "author",
                    "publisher",
                    "publication_date",
                    "estimated_read_time",
                )
            },
        ),

        (
            "Classification",
            {
                "fields": (
                    "themes",
                    "tags",
                )
            },
        ),

        (
            "Management",
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
                )
            },
        ),
    )

    @admin.display(description="Cover Preview")
    def cover_preview(self, obj):

        if obj.cover_image:

            return format_html(
                '<img src="{}" '
                'style="max-height:140px; border-radius:10px;" />',
                obj.cover_image.url,
            )

        return "No image uploaded"