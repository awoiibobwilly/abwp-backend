from django.db import models

from django.utils.text import slugify


class ResearchCategory(models.Model):
    """
    Categories used to organise research publications.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="React Icon name e.g. FaHeartbeat",
    )

    color = models.CharField(
        max_length=7,
        default="#2563EB",
        help_text="Hex colour",
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

        verbose_name = "Research Category"

        verbose_name_plural = "Research Categories"

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