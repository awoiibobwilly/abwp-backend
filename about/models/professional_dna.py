from django.db import models


class ProfessionalDNA(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(
        max_length=100,
        blank=True,
        default="",
        help_text="Frontend icon key, e.g. FaChartLine",
    )

    highlights = models.JSONField(
        default=list,
        blank=True,
        help_text=(
            "List of short bullet highlights for this DNA pillar."
        ),
    )

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Professional DNA Item"
        verbose_name_plural = "Professional DNA Items"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title