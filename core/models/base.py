from django.db import models


# ==========================================================
# BASE PORTFOLIO MODEL
# ABSTRACT MODEL
#
# Shared by all portfolio applications.
# Provides common audit and publishing fields.
# ==========================================================

class BasePortfolioModel(models.Model):

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Controls display ordering."
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Controls visibility."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True