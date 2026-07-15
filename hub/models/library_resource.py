from django.db import models
from django.utils.text import slugify

from core.models import BasePortfolioModel

from .knowledge_theme import KnowledgeTheme
from .knowledge_tag import KnowledgeTag


# ==========================================================
# LIBRARY RESOURCE
# ==========================================================

class LibraryResource(BasePortfolioModel):

    class ResourceType(models.TextChoices):
        BOOK = "book", "Book"
        GUIDE = "guide", "Guide"
        WHITE_PAPER = "white_paper", "White Paper"
        FRAMEWORK = "framework", "Framework"
        TEMPLATE = "template", "Template"
        TOOLKIT = "toolkit", "Toolkit"
        REPORT = "report", "Report"
        ARTICLE = "article", "Article"
        MANUAL = "manual", "Manual"
        DOCUMENTATION = "documentation", "Documentation"
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
        default=ResourceType.ARTICLE
    )

    summary = models.TextField()

    description = models.TextField(
        blank=True
    )

    cover_image = models.ImageField(
        upload_to="portfolio/hub/library/covers/",
        blank=True,
        null=True
    )

    resource_file = models.FileField(
        upload_to="portfolio/hub/library/files/",
        blank=True,
        null=True
    )

    external_url = models.URLField(
        blank=True
    )

    author = models.CharField(
        max_length=255,
        blank=True
    )

    publisher = models.CharField(
        max_length=255,
        blank=True
    )

    publication_date = models.DateField(
        blank=True,
        null=True
    )

    estimated_read_time = models.PositiveIntegerField(
        default=10,
        help_text="Estimated reading time in minutes."
    )

    themes = models.ManyToManyField(
        KnowledgeTheme,
        related_name="library_resources",
        blank=True
    )

    tags = models.ManyToManyField(
        KnowledgeTag,
        related_name="library_resources",
        blank=True
    )

    class Meta:

        ordering = [
            "display_order",
            "title",
        ]

        verbose_name = "Library Resource"

        verbose_name_plural = "Library Resources"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title