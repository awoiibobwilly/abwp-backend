from django.db import models
from django.utils.text import slugify

from core.models import BasePortfolioModel


# ==========================================================
# KNOWLEDGE TAG
#
# Fine-grained classification for knowledge assets.
# ==========================================================

class KnowledgeTag(BasePortfolioModel):

    name = models.CharField(
        max_length=120,
        unique=True,
        help_text="Tag name."
    )

    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True
    )

    description = models.TextField(
        blank=True,
        help_text="Optional description of the tag."
    )

    class Meta:

        ordering = [
            "name",
        ]

        verbose_name = "Knowledge Tag"

        verbose_name_plural = "Knowledge Tags"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name