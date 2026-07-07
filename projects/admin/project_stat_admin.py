from django.contrib import admin

from projects.models import ProjectStat


# ==========================================================
# PROJECT STAT ADMIN
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

@admin.register(ProjectStat)
class ProjectStatAdmin(admin.ModelAdmin):
    list_display = (
        "value",
        "label",
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
        "value",
        "label",
    )

    ordering = (
        "display_order",
        "label",
    )