from django.contrib import admin

from .models import (
    
    Statistic,
    
    Expertise,
    
    Highlight,
    
    Technology,
    
    ProjectCategory,

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
