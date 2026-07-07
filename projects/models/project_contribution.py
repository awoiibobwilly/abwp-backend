from django.db import models


# ==========================================================
# PROJECT CONTRIBUTION MODEL
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectContribution(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Contribution card title."
    )

    description = models.TextField(
        help_text="Contribution card description."
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Frontend icon key for the contribution card."
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
        ordering = ["display_order", "title"]
        verbose_name = "Project Contribution"
        verbose_name_plural = "Project Contributions"

    def __str__(self):
        return self.title