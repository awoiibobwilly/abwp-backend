from django.db import models


# ==========================================================
# PROJECTS HERO MODEL
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectsHero(models.Model):
    eyebrow = models.CharField(
        max_length=100,
        blank=True,
        help_text="Small label above the Projects page title."
    )

    title = models.CharField(
        max_length=255,
        help_text="Main hero heading for the Projects page."
    )

    description = models.TextField(
        blank=True,
        help_text="Supporting hero copy for the Projects page."
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
        verbose_name = "Projects Hero"
        verbose_name_plural = "Projects Hero"

    def __str__(self):
        return self.title