from django.contrib import admin

from projects.models import ProjectContribution


# ==========================================================
# PROJECT CONTRIBUTION ADMIN
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

@admin.register(ProjectContribution)
class ProjectContributionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "icon",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "icon",
    )

    ordering = (
        "display_order",
        "title",
    )