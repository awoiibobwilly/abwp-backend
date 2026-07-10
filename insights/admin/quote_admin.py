from django.contrib import admin
from insights.models import Quote


# ==========================================================
# QUOTE ADMIN
# ==========================================================

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        "short_quote",
        "author",
        "insight",
        "display_order",
        "is_active",
    )
    list_filter = (
        "insight",
        "is_active",
    )
    search_fields = (
        "quote",
        "author",
        "insight__title",
    )
    list_editable = (
        "display_order",
        "is_active",
    )
    ordering = (
        "insight",
        "display_order",
        "id",
    )

    def short_quote(self, obj):
        return obj.quote[:80] + "..." if len(obj.quote) > 80 else obj.quote

    short_quote.short_description = "Quote"