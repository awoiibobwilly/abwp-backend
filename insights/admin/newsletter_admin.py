from django.contrib import admin
from insights.models import Newsletter


# ==========================================================
# NEWSLETTER ADMIN
# ==========================================================

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "insight",
        "eyebrow",
        "title",
        "is_active",
    )
    list_filter = (
        "is_active",
    )
    search_fields = (
        "insight__title",
        "eyebrow",
        "title",
        "description",
    )