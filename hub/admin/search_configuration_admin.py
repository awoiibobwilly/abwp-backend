from django.contrib import admin

from hub.models import SearchConfiguration


# ==========================================================
# SEARCH CONFIGURATION ADMIN
# ==========================================================

@admin.register(SearchConfiguration)
class SearchConfigurationAdmin(admin.ModelAdmin):

    # ======================================================
    # LIST VIEW
    # ======================================================

    list_display = (
        "knowledge_hub",
        "placeholder",
        "updated_at",
    )

    list_display_links = (
        "knowledge_hub",
    )

    search_fields = (
        "placeholder",
        "heading",
        "description",
    )

    ordering = (
        "-updated_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    # ======================================================
    # FIELDSETS
    # ======================================================

    fieldsets = (

        (
            "Knowledge Hub",
            {
                "fields": (
                    "knowledge_hub",
                )
            },
        ),

        (
            "Search Experience",
            {
                "fields": (
                    "heading",
                    "placeholder",
                    "description",
                )
            },
        ),

        (
            "Popular Searches",
            {
                "description": (
                    "Enter search suggestions separated by commas."
                ),
                "fields": (
                    "popular_searches",
                )
            },
        ),

        (
            "Empty Search State",
            {
                "fields": (
                    "empty_state_title",
                    "empty_state_message",
                )
            },
        ),

        (
            "No Results State",
            {
                "fields": (
                    "no_results_title",
                    "no_results_message",
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