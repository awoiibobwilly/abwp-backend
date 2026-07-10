from django.contrib import admin
from insights.models import Insight


# ==========================================================
# INSIGHT ADMIN
# MAIN PAGE CONTAINER
# ==========================================================

@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "is_active",
        "updated_at",
    )
    list_filter = (
        "is_active",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "title",
        "slug",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }