from django.contrib import admin
from django.utils.html import format_html

from hub.models import Organization


# ==========================================================
# ORGANIZATION ADMIN
# ==========================================================

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    # ======================================================
    # LIST VIEW
    # ======================================================

    list_display = (
        "name",
        "logo_preview",
        "organization_type",
        "country",
        "display_order",
        "is_active",
    )

    list_display_links = (
        "name",
    )

    search_fields = (
        "name",
        "description",
        "country",
    )

    list_filter = (
        "organization_type",
        "country",
        "is_active",
    )

    ordering = (
        "display_order",
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    filter_horizontal = (
        "themes",
        "tags",
    )

    readonly_fields = (
        "logo_preview",
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
                    "name",
                    "slug",
                    "organization_type",
                )
            },
        ),

        (
            "Description",
            {
                "fields": (
                    "description",
                )
            },
        ),

        (
            "Branding",
            {
                "fields": (
                    "logo",
                    "logo_preview",
                    "website",
                    "country",
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
    # LOGO PREVIEW
    # ======================================================

    @admin.display(description="Logo")
    def logo_preview(self, obj):

        if obj.logo:

            return format_html(
                """
                <img
                    src="{}"
                    style="
                        max-height:70px;
                        max-width:140px;
                        object-fit:contain;
                        background:#ffffff;
                        padding:8px;
                        border:1px solid #e2e8f0;
                        border-radius:8px;
                    "
                />
                """,
                obj.logo.url,
            )

        return "No logo uploaded"