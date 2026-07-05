from django.db import models


class AboutHero(models.Model):
    eyebrow = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    description = models.TextField()

    image = models.ImageField(
        upload_to="about/hero/",
        blank=True,
        null=True,
    )
    image_alt = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    stats = models.JSONField(
        default=list,
        blank=True,
        help_text=(
            "List of stat objects. Example: "
            '[{"value":"10+","label":"Years Experience"}]'
        ),
    )

    highlights = models.JSONField(
        default=list,
        blank=True,
        help_text=(
            "List of highlight strings or objects. Example: "
            '["Healthcare Leadership", "Software Engineering"]'
        ),
    )

    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Hero"
        verbose_name_plural = "About Hero"

    def __str__(self):
        return self.title