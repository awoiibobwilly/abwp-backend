from django.contrib import admin

from projects.models import ProjectsSectionIntro


# ==========================================================
# PROJECTS SECTION INTRO ADMIN
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

@admin.register(ProjectsSectionIntro)
class ProjectsSectionIntroAdmin(admin.ModelAdmin):
    list_display = (
        "section_key",
        "title",
        "eyebrow",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "section_key",
        "is_active",
    )

    search_fields = (
        "title",
        "eyebrow",
        "intro",
    )