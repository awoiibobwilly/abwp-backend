from django.db import models


# ==========================================================
# PROJECT STAT MODEL
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectStat(models.Model):
    value = models.CharField(
        max_length=50,
        help_text="Stat value, e.g. 20+, 100%."
    )

    label = models.CharField(
        max_length=100,
        help_text="Stat label, e.g. Projects, Technologies."
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["display_order", "label"]
        verbose_name = "Project Stat"
        verbose_name_plural = "Project Stats"

    def __str__(self):
        return f"{self.value} {self.label}"