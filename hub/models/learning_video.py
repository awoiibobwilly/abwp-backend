from django.db import models
from django.utils.text import slugify

from core.models import BasePortfolioModel

from .knowledge_theme import KnowledgeTheme
from .knowledge_tag import KnowledgeTag


# ==========================================================
# LEARNING VIDEO
# CURATED EDUCATIONAL VIDEO
# ==========================================================

class LearningVideo(BasePortfolioModel):

    class VideoPlatform(models.TextChoices):

        YOUTUBE = "youtube", "YouTube"

        VIMEO = "vimeo", "Vimeo"

        MICROSOFT = "microsoft", "Microsoft Learn"

        COURSERA = "coursera", "Coursera"

        LINKEDIN = "linkedin", "LinkedIn Learning"

        UDEMY = "udemy", "Udemy"

        OTHER = "other", "Other"

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        max_length=280,
        unique=True,
        blank=True
    )

    summary = models.TextField()

    description = models.TextField(
        blank=True
    )

    thumbnail = models.ImageField(
        upload_to="portfolio/hub/videos/thumbnails/",
        blank=True,
        null=True
    )

    platform = models.CharField(
        max_length=30,
        choices=VideoPlatform.choices,
        default=VideoPlatform.YOUTUBE
    )

    video_url = models.URLField()

    presenter = models.CharField(
        max_length=255,
        blank=True
    )

    duration_minutes = models.PositiveIntegerField(
        default=10
    )

    published_at = models.DateField(
        blank=True,
        null=True
    )

    themes = models.ManyToManyField(
        KnowledgeTheme,
        related_name="learning_videos",
        blank=True
    )

    tags = models.ManyToManyField(
        KnowledgeTag,
        related_name="learning_videos",
        blank=True
    )

    class Meta:

        ordering = [
            "display_order",
            "title",
        ]

        verbose_name = "Learning Video"

        verbose_name_plural = "Learning Videos"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title