from django.db import models


class ResearchSectionIntro(models.Model):
    """
    Reusable intro content for Research page sections.
    """

    SECTION_CHOICES = [
        ("areas", "Research Areas"),
        ("publications", "Publications"),
        ("methodologies", "Methodologies & Tools"),
        ("interests", "Research Interests"),
        ("philosophy", "Research Philosophy"),
    ]

    section_key = models.CharField(
        max_length=50,
        choices=SECTION_CHOICES,
        unique=True,
    )

    eyebrow = models.CharField(
        max_length=120,
    )

    title = models.CharField(
        max_length=255,
    )

    intro = models.TextField()

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
        ordering = ["section_key"]
        verbose_name = "Research Section Intro"
        verbose_name_plural = "Research Section Intros"

    def __str__(self):
        return f"{self.get_section_key_display()} Intro"