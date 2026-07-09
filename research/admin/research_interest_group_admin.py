from django.contrib import admin

from ..models import (
    ResearchInterestGroup,
    ResearchInterest,
)


class ResearchInterestInline(admin.TabularInline):
    model = ResearchInterest
    extra = 1
    fields = (
        "name",
        "display_order",
        "is_active",
    )
    ordering = (
        "display_order",
        "name",
    )


@admin.register(ResearchInterestGroup)
class ResearchInterestGroupAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "slug",
    )

    ordering = (
        "display_order",
        "title",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "display_order",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        ResearchInterestInline,
    ]

    fieldsets = (
        (
            "Research Interest Group",
            {
                "fields": (
                    "title",
                    "slug",
                    "description",
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