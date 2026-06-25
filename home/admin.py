from django.contrib import admin

from .models import (
    Statistic,
    Expertise,
    Highlight,
    Technology,
    ProjectCategory,
    Project,

)


@admin.register(

    Statistic

)
class StatisticAdmin(

    admin.ModelAdmin

):

    list_display = (

        "title",

        "value",

        "suffix",

        "display_order",

        "is_active",

    )

    list_filter = (

        "is_active",

    )

    search_fields = (

        "title",

    )

    ordering = (

        "display_order",

    )


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):

    list_display = (

        "title",

        "display_order",

        "is_active",

    )

    list_filter = (

        "is_active",

    )

    search_fields = (

        "title",

        "description",

    )

    ordering = (

        "display_order",

    )


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):

    list_display = (

        "title",

        "display_order",

        "is_active",

    )

    list_filter = (

        "is_active",

    )

    search_fields = (

        "title",

        "description",

    )

    ordering = (

        "display_order",

    )


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (

        "name",

        "proficiency",

        "display_order",

        "is_active",

    )

    list_filter = (

        "is_active",

    )

    search_fields = (

        "name",

        "description",

    )

    ordering = (

        "display_order",

        "name",

    )

    prepopulated_fields = {

        "slug": ("name",),

    }

# =================================
    # PROJECT CATEGORY
# =================================

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):

    list_display = (

        "name",

        "display_order",

        "is_active",

    )

    list_filter = (

        "is_active",

    )

    search_fields = (

        "name",

        "description",

    )

    ordering = (

        "display_order",

        "name",

    )

    prepopulated_fields = {

        "slug": ("name",),

    }

# ======================================
    # PROJECT
# ======================================


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    # ==========================
    # List View
    # ==========================

    list_display = (

        "title",

        "category",

        "status",

        "featured",

        "is_open_source",

        "is_active",

        "display_order",

        "created_at",

    )

    list_display_links = (

        "title",

    )

    list_editable = (

        "featured",

        "is_active",

        "display_order",

    )

    list_filter = (

        "category",

        "status",

        "featured",

        "is_open_source",

        "is_active",

        "technologies",

    )

    search_fields = (

        "title",

        "client",

        "organization",

        "role",

        "short_description",

        "description",

        "meta_title",

        "meta_description",

        "keywords",

    )

    ordering = (

        "display_order",

        "-created_at",

    )

    filter_horizontal = (

        "technologies",

    )

    prepopulated_fields = {

        "slug": ("title",),

    }

    readonly_fields = (

        "created_at",

        "updated_at",

    )

    save_on_top = True

    # ==========================
    # Form Layout
    # ==========================

    fieldsets = (

        (
            "Project Information",
            {
                "fields": (

                    "title",

                    "slug",

                    "category",

                    "technologies",

                    "short_description",

                    "description",

                )
            },
        ),

        (
            "Media",
            {
                "fields": (

                    "thumbnail",

                )
            },
        ),

        (
            "Project Details",
            {
                "fields": (

                    "client",

                    "organization",

                    "role",

                    "status",

                    "started_at",

                    "completed_at",

                )
            },
        ),

        (
            "Project Links",
            {
                "fields": (

                    "github_url",

                    "live_url",

                    "documentation_url",

                )
            },
        ),

        (
            "SEO & Social Sharing",
            {
                "classes": ("collapse",),

                "fields": (

                    "meta_title",

                    "meta_description",

                    "keywords",

                    "canonical_url",

                    "og_image",

                ),
            },
        ),

        (
            "Publishing",
            {
                "fields": (

                    "featured",

                    "is_open_source",

                    "is_active",

                    "display_order",

                )
            },
        ),

        (
            "Audit Information",
            {
                "classes": ("collapse",),

                "fields": (

                    "created_at",

                    "updated_at",

                ),
            },
        ),

    )