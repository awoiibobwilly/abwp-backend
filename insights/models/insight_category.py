from django.db import models
from django.utils.text import slugify


# ==========================================================
# INSIGHT CATEGORY
# CATEGORY / TOPIC PILL FOR INSIGHTS PAGE
# ==========================================================

class InsightCategory(models.Model):
    insight = models.ForeignKey(
        "insights.Insight",
        on_delete=models.CASCADE,
        related_name="categories"
    )
    name = models.CharField(max_length=120)
    slug = models.SlugField(
        max_length=140,
        blank=True
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Insight Category"
        verbose_name_plural = "Insight Categories"
        unique_together = ("insight", "slug")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name