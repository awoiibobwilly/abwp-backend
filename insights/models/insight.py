from django.db import models
from django.utils.text import slugify


# ==========================================================
# INSIGHT
# MAIN PAGE CONTAINER FOR THE INSIGHTS PAGE
# ==========================================================

class Insight(models.Model):
    title = models.CharField(
        max_length=200,
        default="Insights Page",
        help_text="Administrative title for the Insights page."
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        help_text="Unique slug for the Insights page."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Marks this Insights page configuration as active."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Insight Page"
        verbose_name_plural = "Insight Pages"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) or "insights-page"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title