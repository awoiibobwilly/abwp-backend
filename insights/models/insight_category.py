from django.db import models
from django.utils.text import slugify


# ==========================================================
# INSIGHT CATEGORY
# KNOWLEDGE DOMAINS FOR THE INSIGHTS PAGE
# ==========================================================

class InsightCategory(models.Model):
    insight = models.ForeignKey(
        "insights.Insight",
        on_delete=models.CASCADE,
        related_name="categories",
    )

    name = models.CharField(
        max_length=120,
    )

    slug = models.SlugField(
        max_length=120,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    accent_color = models.CharField(
        max_length=20,
        default="#2563EB",
        help_text="Hex color used by the frontend.",
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = (
            "display_order",
            "name",
        )

        unique_together = (
            "insight",
            "slug",
        )

        verbose_name = "Insight Category"
        verbose_name_plural = "Insight Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
