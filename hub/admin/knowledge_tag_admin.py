from django.contrib import admin

from hub.models import KnowledgeTag


# ==========================================================
# KNOWLEDGE TAG ADMIN
# ==========================================================

@admin.register(KnowledgeTag)
class KnowledgeTagAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "display_order",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "name",
    )

    search_fields = (
        "name",
        "description",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "slug",
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