from django.db import models


class ResearchPageHero(models.Model):
    """
    Hero content for the Research page.
    Usually a single record.
    """

    eyebrow = models.CharField(
        max_length=120,
        default="Research & Inquiry",
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField()

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Research Page Hero"
        verbose_name_plural = "Research Page Hero"

    def __str__(self):
        return self.title