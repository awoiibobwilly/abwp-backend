from django.db import models
from django.utils.text import slugify


class ResearchMethodologyGroup(models.Model):
    """
    Group headings such as:
    - Research Methodologies
    - Tools & Platforms
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
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="React icon name e.g. FaFlask",
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
        verbose_name = "Research Methodology Group"
        verbose_name_plural = "Research Methodology Groups"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ResearchMethodologyItem(models.Model):
    """
    Individual methodology/tool item belonging to a group.
    """

    group = models.ForeignKey(
        ResearchMethodologyGroup,
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
        verbose_name = "Research Methodology Item"
        verbose_name_plural = "Research Methodology Items"

    def __str__(self):
        return self.name