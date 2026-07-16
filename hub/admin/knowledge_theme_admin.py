from django.contrib import admin
from django.utils.html import format_html

from hub.models import KnowledgeTheme


# ==========================================================
# KNOWLEDGE THEME ADMIN
# ==========================================================

@admin.register(KnowledgeTheme)
class KnowledgeThemeAdmin(admin.ModelAdmin):

    # ======================================================
    # LIST VIEW
    # ======================================================

    list_display = (
        "title",
        "color_preview",
        "display_order",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "title",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "display_order",
        "title",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "cover_preview",
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
                    "icon",
                    "accent_color",
                )
            },
        ),

        (
            "Descriptions",
            {
                "fields": (
                    "short_description",
                    "description",
                )
            },
        ),

        (
            "Cover Image",
            {
                "fields": (
                    "cover_image",
                    "cover_preview",
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
    # COVER PREVIEW
    # ======================================================

    @admin.display(description="Cover Preview")
    def cover_preview(self, obj):

        if obj.cover_image:

            return format_html(
                """
                <img
                    src="{}"
                    style="
                        max-height:180px;
                        border-radius:12px;
                        box-shadow:0 4px 12px rgba(0,0,0,.15);
                    "
                />
                """,
                obj.cover_image.url,
            )

        return "No image uploaded"

    # ======================================================
    # ACCENT COLOR PREVIEW
    # ======================================================

    @admin.display(description="Accent")
    def color_preview(self, obj):

        return format_html(
            """
            <div
                style="
                    width:28px;
                    height:28px;
                    border-radius:50%;
                    background:{};
                    border:1px solid #ddd;
                ">
            </div>
            """,
            obj.accent_color,
        )