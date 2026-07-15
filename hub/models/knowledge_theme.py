from django.db import models
from django.utils.text import slugify

from core.models import BasePortfolioModel


# ==========================================================
# KNOWLEDGE THEME
#
# Represents a major knowledge domain within
# the Knowledge Hub.
# ==========================================================

class KnowledgeTheme(BasePortfolioModel):

    title = models.CharField(
        max_length=150,
        unique=True,
        help_text="Name of the knowledge theme."
    )

    slug = models.SlugField(
        max_length=180,
        unique=True,
        blank=True
    )

    short_description = models.CharField(
        max_length=255,
        blank=True,
        help_text="Short summary displayed on cards."
    )

    description = models.TextField(
        blank=True,
        help_text="Detailed description of the knowledge theme."
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Frontend icon identifier."
    )

    accent_color = models.CharField(
        max_length=20,
        default="#2563EB",
        help_text="Theme accent color."
    )

    cover_image = models.ImageField(
        upload_to="portfolio/hub/themes/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = [
            "display_order",
            "title",
        ]

        verbose_name = "Knowledge Theme"

        verbose_name_plural = "Knowledge Themes"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title