from django.db import models
from django.utils.text import slugify


class ResearchInterestGroup(models.Model):
    """
    Cluster heading for ongoing research interests.
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

    description = models.TextField(
        blank=True,
        help_text="Optional supporting description for this research interest cluster.",
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
        verbose_name = "Research Interest Group"
        verbose_name_plural = "Research Interest Groups"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ResearchInterest(models.Model):
    """
    Individual research interest item belonging to a group.
    """

    group = models.ForeignKey(
        ResearchInterestGroup,
        on_delete=models.CASCADE,
        related_name="items",
    )

    name = models.CharField(
        max_length=150,
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
        ordering = ["display_order", "name"]
        verbose_name = "Research Interest"
        verbose_name_plural = "Research Interests"

    def __str__(self):
        return self.name