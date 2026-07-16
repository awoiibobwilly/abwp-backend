from django.contrib import admin
from django.utils.html import format_html

from hub.models import ResearchContribution


# ==========================================================
# RESEARCH CONTRIBUTION ADMIN
# ==========================================================

@admin.register(ResearchContribution)
class ResearchContributionAdmin(admin.ModelAdmin):

    # ======================================================
    # LIST VIEW
    # ======================================================

    list_display = (
        "title",
        "cover_preview",
        "contribution_type",
        "publication",
        "publication_date",
        "display_order",
        "is_active",
    )

    list_display_links = (
        "title",
    )

    search_fields = (
        "title",
        "summary",
        "abstract",
        "publication",
        "doi",
    )

    list_filter = (
        "contribution_type",
        "publication_date",
        "is_active",
    )

    ordering = (
        "-publication_date",
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
                    "contribution_type",
                )
            },
        ),

        (
            "Research Content",
            {
                "fields": (
                    "summary",
                    "abstract",
                )
            },
        ),

        (
            "Publication Details",
            {
                "fields": (
                    "publication",
                    "publication_date",
                    "doi",
                )
            },
        ),

        (
            "Media",
            {
                "fields": (
                    "cover_image",
                    "cover_preview",
                    "document",
                    "external_url",
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
    # COVER PREVIEW
    # ======================================================

    @admin.display(description="Cover")
    def cover_preview(self, obj):

        if obj.cover_image:

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
                obj.cover_image.url,
            )

        return "No cover uploaded"