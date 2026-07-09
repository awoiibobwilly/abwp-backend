from django.db import models


class ResearchPhilosophyPoint(models.Model):
    """
    Principles that shape the user's research approach.
    """

    title = models.CharField(
        max_length=150,
        unique=True,
    )

    description = models.TextField(
        help_text="Core principle description shown on the Research page.",
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="React icon name e.g. FaLightbulb",
    )

    accent_color = models.CharField(
        max_length=7,
        default="#2563EB",
        help_text="Optional hex colour used by the frontend card UI.",
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

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
        ordering = ["display_order", "title"]
        verbose_name = "Research Philosophy Point"
        verbose_name_plural = "Research Philosophy Points"

    def __str__(self):
        return self.title