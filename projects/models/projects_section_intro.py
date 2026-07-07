from django.db import models


# ==========================================================
# PROJECTS SECTION INTRO MODEL
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectsSectionIntro(models.Model):
    FEATURED = "featured"
    CATEGORIES = "categories"
    TECHNOLOGIES = "technologies"
    BEYOND = "beyond"

    SECTION_CHOICES = [
        (FEATURED, "Featured Projects"),
        (CATEGORIES, "Project Categories"),
        (TECHNOLOGIES, "Technologies"),
        (BEYOND, "Beyond Projects"),
    ]

    section_key = models.CharField(
        max_length=50,
        choices=SECTION_CHOICES,
        unique=True,
        help_text="Unique key for a Projects page section intro."
    )

    eyebrow = models.CharField(
        max_length=100,
        blank=True,
        help_text="Small label above the section title."
    )

    title = models.CharField(
        max_length=255,
        help_text="Main section heading."
    )

    intro = models.TextField(
        blank=True,
        help_text="Supporting copy for the section."
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
        ordering = ["section_key"]
        verbose_name = "Projects Section Intro"
        verbose_name_plural = "Projects Section Intros"

    def __str__(self):
        return f"{self.get_section_key_display()} Intro"