from django.contrib import admin

from projects.models import ProjectsHero


# ==========================================================
# PROJECTS HERO ADMIN
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

@admin.register(ProjectsHero)
class ProjectsHeroAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "eyebrow",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "eyebrow",
        "description",
    )