from django.contrib import admin
from django.utils.html import format_html

from hub.models import KnowledgeHub


# ==========================================================
# KNOWLEDGE HUB ADMIN
# ==========================================================

@admin.register(KnowledgeHub)
class KnowledgeHubAdmin(admin.ModelAdmin):

    # ======================================================
    # LIST VIEW
    # ======================================================

    list_display = (
        "title",
        "display_order",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "title",
    )

    ordering = (
        "display_order",
    )

    search_fields = (
        "title",
        "subtitle",
    )

    list_filter = (
        "is_active",
    )

    readonly_fields = (
        "hero_preview",
        "created_at",
        "updated_at",
    )

    # ======================================================
    # FIELDSETS
    # ======================================================

    fieldsets = (

        (
            "Hero",
            {
                "fields": (
                    "eyebrow",
                    "title",
                    "subtitle",
                    "description",
                    "search_placeholder",
                )
            },
        ),

        (
            "Hero Background",
            {
                "fields": (
                    "hero_background",
                    "hero_preview",
                )
            },
        ),

        (
            "Call To Action",
            {
                "fields": (
                    "cta_title",
                    "cta_description",
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
                ),
            },
        ),
    )

    # ======================================================
    # IMAGE PREVIEW
    # ======================================================

    @admin.display(description="Hero Preview")
    def hero_preview(self, obj):

        if obj.hero_background:

            return format_html(
                '<img src="{}" '
                'style="max-height:180px;'
                'border-radius:12px;'
                'box-shadow:0 4px 12px rgba(0,0,0,.15);" />',
                obj.hero_background.url,
            )

        return "No image uploaded"