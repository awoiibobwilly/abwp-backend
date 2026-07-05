from django.db import models


class SelectedAchievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.CharField(
        max_length=100,
        blank=True,
        default="",
    )
    year = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Selected Achievement"
        verbose_name_plural = "Selected Achievements"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title