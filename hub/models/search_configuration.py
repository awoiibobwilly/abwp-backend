from django.db import models

from core.models import BasePortfolioModel

from .knowledge_hub import KnowledgeHub


# ==========================================================
# SEARCH CONFIGURATION
# KNOWLEDGE HUB SEARCH SETTINGS
# ==========================================================

class SearchConfiguration(BasePortfolioModel):

    knowledge_hub = models.OneToOneField(
        KnowledgeHub,
        on_delete=models.CASCADE,
        related_name="search_configuration"
    )

    placeholder = models.CharField(
        max_length=255,
        default="Search knowledge, resources, videos..."
    )

    heading = models.CharField(
        max_length=255,
        default="Search the Knowledge Hub"
    )

    description = models.TextField(
        blank=True
    )

    popular_searches = models.CharField(
        max_length=500,
        blank=True,
        help_text="Comma-separated search suggestions."
    )

    empty_state_title = models.CharField(
        max_length=255,
        default="Start Exploring"
    )

    empty_state_message = models.TextField(
        blank=True,
        default=(
            "Search across resources, research, "
            "videos, toolkits and organizations."
        )
    )

    no_results_title = models.CharField(
        max_length=255,
        default="No Results Found"
    )

    no_results_message = models.TextField(
        blank=True,
        default=(
            "Try a different keyword or browse "
            "knowledge themes."
        )
    )

    class Meta:

        verbose_name = "Search Configuration"

        verbose_name_plural = "Search Configuration"

    def __str__(self):
        return "Knowledge Hub Search Configuration"