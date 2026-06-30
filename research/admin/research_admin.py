from django.contrib import admin

from ..models import Research


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):

    list_display = (

        "title",

        "category",

        "publication_type",

        "year",

        "status",

        "featured",

        "published",

    )

    list_filter = (

        "category",

        "publication_type",

        "status",

        "featured",

        "published",

        "year",

    )

    search_fields = (

        "title",

        "authors",

        "institution",

        "journal",

        "publisher",

    )

    ordering = (

        "display_order",

        "-year",

    )

    prepopulated_fields = {

        "slug": ("title",)

    }

    list_editable = (

        "featured",

        "published",

    )

    filter_horizontal = (

        "keywords",

    )

    readonly_fields = (

        "created_at",

        "updated_at",

    )

    fieldsets = (

        (

            "Research",

            {

                "fields": (

                    "title",

                    "slug",

                    "category",

                    "publication_type",

                )

            },

        ),

        (

            "Publication",

            {

                "fields": (

                    "authors",

                    "institution",

                    "journal",

                    "publisher",

                    "year",

                )

            },

        ),

        (

            "Content",

            {

                "fields": (

                    "summary",

                    "abstract",

                    "keywords",

                )

            },

        ),

        (

            "Resources",

            {

                "fields": (

                    "featured_image",

                    "pdf",

                    "doi",

                    "external_url",

                )

            },

        ),

        (

            "Publishing",

            {

                "fields": (

                    "status",

                    "featured",

                    "published",

                    "display_order",

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