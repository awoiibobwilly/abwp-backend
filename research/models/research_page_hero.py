from django.core.exceptions import ValidationError
from django.db import models


class ResearchPageHero(models.Model):
    """
    Hero content for the Research page.

    This behaves like a soft singleton:
    - multiple records can exist for drafting/history
    - only one record should be active at a time
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
        ordering = ["-updated_at", "-id"]
        verbose_name = "Research Page Hero"
        verbose_name_plural = "Research Page Hero"

    def clean(self):
        """
        Ensure only one active hero exists at a time.
        """
        if self.is_active:
            existing_active = (
                ResearchPageHero.objects
                .filter(is_active=True)
                .exclude(pk=self.pk)
                .exists()
            )
            if existing_active:
                raise ValidationError(
                    "Only one Research Page Hero can be active at a time."
                )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title