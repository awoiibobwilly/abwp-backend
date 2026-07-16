from django.contrib import admin
from django.utils.html import format_html

from hub.models import LearningVideo


# ==========================================================
# LEARNING VIDEO ADMIN
# ==========================================================

@admin.register(LearningVideo)
class LearningVideoAdmin(admin.ModelAdmin):

    # ======================================================
    # LIST VIEW
    # ======================================================

    list_display = (
        "title",
        "platform",
        "presenter",
        "duration_minutes",
        "display_order",
        "is_active",
    )

    list_display_links = (
        "title",
    )

    search_fields = (
        "title",
        "summary",
        "presenter",
    )

    list_filter = (
        "platform",
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
        "thumbnail_preview",
        "created_at",
        "updated_at",
    )

    # ======================================================
    # FIELDSETS
    # ======================================================

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "platform",
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
                    "thumbnail",
                    "thumbnail_preview",
                    "video_url",
                )
            },
        ),

        (
            "Video Information",
            {
                "fields": (
                    "presenter",
                    "duration_minutes",
                    "published_at",
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

    # ======================================================
    # THUMBNAIL PREVIEW
    # ======================================================

    @admin.display(description="Thumbnail Preview")
    def thumbnail_preview(self, obj):

        if obj.thumbnail:

            return format_html(
                """
                <img
                    src="{}"
                    style="
                        max-height:140px;
                        border-radius:10px;
                        box-shadow:0 4px 12px rgba(0,0,0,.15);
                    "
                />
                """,
                obj.thumbnail.url,
            )

        return "No thumbnail uploaded"