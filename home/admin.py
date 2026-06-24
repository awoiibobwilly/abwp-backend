from django.contrib import admin

from .models import Statistic


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
