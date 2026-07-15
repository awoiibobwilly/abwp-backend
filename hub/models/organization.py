from django.db import models
from django.utils.text import slugify

from core.models import BasePortfolioModel

from .knowledge_theme import KnowledgeTheme
from .knowledge_tag import KnowledgeTag


# ==========================================================
# ORGANIZATION
# TRUSTED KNOWLEDGE SOURCE
# ==========================================================

class Organization(BasePortfolioModel):

    class OrganizationType(models.TextChoices):

        UNIVERSITY = "university", "University"

        HEALTHCARE = "healthcare", "Healthcare Organization"

        RESEARCH = "research", "Research Institution"

        TECHNOLOGY = "technology", "Technology Company"

        LEARNING = "learning", "Learning Platform"

        PROFESSIONAL = "professional", "Professional Body"

        GOVERNMENT = "government", "Government Agency"

        NGO = "ngo", "NGO"

        OTHER = "other", "Other"

    name = models.CharField(
        max_length=255,
        unique=True
    )

    slug = models.SlugField(
        max_length=280,
        unique=True,
        blank=True
    )

    organization_type = models.CharField(
        max_length=30,
        choices=OrganizationType.choices,
        default=OrganizationType.OTHER
    )

    description = models.TextField(
        blank=True
    )

    logo = models.ImageField(
        upload_to="portfolio/hub/organizations/logos/",
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True
    )

    country = models.CharField(
        max_length=120,
        blank=True
    )

    themes = models.ManyToManyField(
        KnowledgeTheme,
        related_name="organizations",
        blank=True
    )

    tags = models.ManyToManyField(
        KnowledgeTag,
        related_name="organizations",
        blank=True
    )

    class Meta:

        ordering = [
            "display_order",
            "name",
        ]

        verbose_name = "Organization"

        verbose_name_plural = "Organizations"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name