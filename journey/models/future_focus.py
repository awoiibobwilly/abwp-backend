from django.db import models


class FutureFocus(models.Model):
    title = models.CharField(
        max_length=150,
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Frontend icon key, e.g. healthcare, digital-health, ai, research, leadership, global",
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
        verbose_name = "Future Focus"
        verbose_name_plural = "Future Focus"
        ordering = ("display_order", "id")

    def __str__(self):
        return self.title