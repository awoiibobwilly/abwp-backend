from django.contrib import admin

from .models import Statistic

from .models import Expertise

from .models import Highlight

from .models import Technology


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
