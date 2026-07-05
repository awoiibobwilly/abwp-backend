from django.db import models


class CoreValues(models.Model):
    section_title = models.CharField(
        max_length=200,
        default="Core Values",
    )
    section_description = models.TextField(blank=True, default="")

    mission_title = models.CharField(
        max_length=150,
        default="Mission",
    )
    mission_description = models.TextField()

    vision_title = models.CharField(
        max_length=150,
        default="Vision",
    )
    vision_description = models.TextField()

    values = models.JSONField(
        default=list,
        blank=True,
        help_text=(
            "List of value objects. Example: "
            '[{"letter":"A","title":"Accountability","description":"..."}]'
        ),
    )

    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Core Values"
        verbose_name_plural = "Core Values"

    def __str__(self):
        return self.section_title