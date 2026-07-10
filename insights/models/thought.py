from django.db import models
from django.utils.text import slugify


# ==========================================================
# THOUGHT
# SHORT INSIGHT / REFLECTION CARD
# ==========================================================

class Thought(models.Model):
    insight = models.ForeignKey(
        "insights.Insight",
        on_delete=models.CASCADE,
        related_name="thoughts"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        blank=True
    )
    category = models.CharField(
        max_length=120,
        blank=True,
        help_text="Category label for the thought card."
    )
    excerpt = models.TextField(
        blank=True,
        help_text="Short reflection or excerpt."
    )
    published_at = models.DateField(
        blank=True,
        null=True
    )
    external_url = models.URLField(
        blank=True,
        help_text="Optional external link for the full thought/article."
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "-published_at", "title"]
        verbose_name = "Thought"
        verbose_name_plural = "Thoughts"
        unique_together = ("insight", "slug")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title