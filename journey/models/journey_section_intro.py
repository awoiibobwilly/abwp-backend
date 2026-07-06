from django.db import models


class JourneySectionIntro(models.Model):
    SECTION_CHOICES = (
        ("timeline", "Timeline"),
        ("future", "Future Vision"),
    )

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

    intro = models.TextField(
        blank=True,
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
        verbose_name = "Journey Section Intro"
        verbose_name_plural = "Journey Section Intros"
        ordering = ("section_key",)

    def __str__(self):
        return f"{self.get_section_key_display()} Intro"