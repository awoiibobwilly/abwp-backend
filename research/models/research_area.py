from django.db import models
from django.utils.text import slugify


class ResearchArea(models.Model):
    """
    Strategic research domains displayed on the Research page.
    These are broader page-content domains, not necessarily
    identical to publication categories.
    """

    title = models.CharField(
        max_length=150,
        unique=True,
    )

    slug = models.SlugField(
        max_length=180,
        unique=True,
        blank=True,
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="React icon name e.g. FaMicroscope",
    )

    accent_color = models.CharField(
        max_length=7,
        default="#2563EB",
        help_text="Hex colour used for this area card.",
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
        ordering = ["display_order", "title"]
        verbose_name = "Research Area"
        verbose_name_plural = "Research Areas"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title