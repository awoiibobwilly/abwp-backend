from django.db import models

from django.utils.text import slugify


class ResearchKeyword(models.Model):
    """
    Keywords used to classify research publications.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    color = models.CharField(
        max_length=7,
        default="#2563EB",
        help_text="Hex colour used for badges.",
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional React Icon name.",
    )

    display_order = models.PositiveIntegerField(
        default=0,
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

        ordering = [

            "display_order",

            "name",

        ]

        verbose_name = "Research Keyword"

        verbose_name_plural = "Research Keywords"

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(

                self.name

            )

        super().save(

            *args,

            **kwargs,

        )

    def __str__(self):

        return self.name