from django.db import models


class JourneyHero(models.Model):
    eyebrow = models.CharField(
        max_length=120,
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField()

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
        verbose_name = "Journey Hero"
        verbose_name_plural = "Journey Hero"

    def __str__(self):
        return self.title