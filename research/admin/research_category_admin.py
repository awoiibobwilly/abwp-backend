from django.contrib import admin

from ..models import ResearchCategory


@admin.register(ResearchCategory)
class ResearchCategoryAdmin(admin.ModelAdmin):

    list_display = (

        "name",

        "display_order",

        "is_active",

        "created_at",

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

        "slug": ("name",)

    }

    list_editable = (

        "display_order",

        "is_active",

    )

    readonly_fields = (

        "created_at",

        "updated_at",

    )

    fieldsets = (

        (

            "Category Information",

            {

                "fields": (

                    "name",

                    "slug",

                    "description",

                )

            },

        ),

        (

            "Appearance",

            {

                "fields": (

                    "icon",

                    "color",

                )

            },

        ),

        (

            "Display",

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

                ),

            },

        ),

    )