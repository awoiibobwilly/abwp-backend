from django.db import models
from django.utils.text import slugify


# ==========================================================
# FEATURED ARTICLE
# MAIN FEATURED ARTICLES FOR THE INSIGHTS PAGE
# ==========================================================

class FeaturedArticle(models.Model):
    insight = models.ForeignKey(
        "insights.Insight",
        on_delete=models.CASCADE,
        related_name="featured_articles"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        blank=True
    )
    category = models.CharField(
        max_length=120,
        blank=True,
        help_text="Primary category label shown on the card."
    )
    excerpt = models.TextField(
        blank=True,
        help_text="Short summary or excerpt for the article."
    )
    cover_image = models.ImageField(
        upload_to="portfolio/insights/featured_articles/",
        blank=True,
        null=True
    )
    read_time = models.CharField(
        max_length=50,
        blank=True,
        help_text='Example: "6 min read"'
    )
    published_at = models.DateField(
        blank=True,
        null=True
    )
    external_url = models.URLField(
        blank=True,
        help_text="Optional external article URL."
    )
    is_featured = models.BooleanField(
        default=True,
        help_text="Marks the article as part of the featured article section."
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "-published_at", "title"]
        verbose_name = "Featured Article"
        verbose_name_plural = "Featured Articles"
        unique_together = ("insight", "slug")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title