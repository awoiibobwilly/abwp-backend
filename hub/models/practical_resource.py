from django.db import models
from django.utils.text import slugify

from core.models import BasePortfolioModel

from .knowledge_theme import KnowledgeTheme
from .knowledge_tag import KnowledgeTag


# ==========================================================
# PRACTICAL RESOURCE
# ACTIONABLE KNOWLEDGE ASSET
# ==========================================================

class PracticalResource(BasePortfolioModel):

    class ResourceType(models.TextChoices):

        TEMPLATE = "template", "Template"

        TOOLKIT = "toolkit", "Toolkit"

        CHECKLIST = "checklist", "Checklist"

        FRAMEWORK = "framework", "Framework"

        DASHBOARD = "dashboard", "Dashboard"

        SOP = "sop", "Standard Operating Procedure"

        POLICY = "policy", "Policy"

        QUESTIONNAIRE = "questionnaire", "Questionnaire"

        SPREADSHEET = "spreadsheet", "Spreadsheet"

        OTHER = "other", "Other"

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        max_length=280,
        unique=True,
        blank=True
    )

    resource_type = models.CharField(
        max_length=30,
        choices=ResourceType.choices,
        default=ResourceType.TEMPLATE
    )

    summary = models.TextField()

    description = models.TextField(
        blank=True
    )

    thumbnail = models.ImageField(
        upload_to="portfolio/hub/practical_resources/thumbnails/",
        blank=True,
        null=True
    )

    resource_file = models.FileField(
        upload_to="portfolio/hub/practical_resources/files/",
        blank=True,
        null=True
    )

    external_url = models.URLField(
        blank=True
    )

    version = models.CharField(
        max_length=30,
        blank=True,
        help_text="Optional version number."
    )

    themes = models.ManyToManyField(
        KnowledgeTheme,
        related_name="practical_resources",
        blank=True
    )

    tags = models.ManyToManyField(
        KnowledgeTag,
        related_name="practical_resources",
        blank=True
    )

    class Meta:

        ordering = [
            "display_order",
            "title",
        ]

        verbose_name = "Practical Resource"

        verbose_name_plural = "Practical Resources"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title