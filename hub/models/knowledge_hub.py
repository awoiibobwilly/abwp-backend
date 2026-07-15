from django.db import models

from core.models import BasePortfolioModel


# ==========================================================
# KNOWLEDGE HUB
# PAGE CONFIGURATION
# ==========================================================

class KnowledgeHub(BasePortfolioModel):

    # ======================================================
    # HERO
    # ======================================================

    eyebrow = models.CharField(
        max_length=120,
        default="Knowledge Hub"
    )

    title = models.CharField(
        max_length=255
    )

    subtitle = models.CharField(
        max_length=255,
        blank=True
    )

    description = models.TextField()

    search_placeholder = models.CharField(
        max_length=255,
        default="Search knowledge, resources, frameworks..."
    )

    hero_background = models.ImageField(
        upload_to="portfolio/hub/hero/",
        blank=True,
        null=True
    )

    # ======================================================
    # CALL TO ACTION
    # ======================================================

    cta_title = models.CharField(
        max_length=255,
        blank=True
    )

    cta_description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ["display_order"]
        verbose_name = "Knowledge Hub"
        verbose_name_plural = "Knowledge Hub"

    def __str__(self):
        return self.title