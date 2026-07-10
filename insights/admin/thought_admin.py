from django.contrib import admin
from insights.models import Thought


# ==========================================================
# THOUGHT ADMIN
# ==========================================================

@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "insight",
        "category",
        "published_at",
        "display_order",
        "is_active",
    )
    list_filter = (
        "insight",
        "category",
        "is_active",
        "published_at",
    )
    search_fields = (
        "title",
        "slug",
        "category",
        "excerpt",
        "insight__title",
    )
    list_editable = (
        "display_order",
        "is_active",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }
    ordering = (
        "insight",
        "display_order",
        "-published_at",
        "title",
    )