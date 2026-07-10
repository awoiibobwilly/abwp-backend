from django.db import models


# ==========================================================
# INSIGHT SECTION INTRO
# REUSABLE INTRO BLOCK FOR INSIGHTS PAGE SECTIONS
# ==========================================================

class InsightSectionIntro(models.Model):
    SECTION_FEATURED_ARTICLES = "featured_articles"
    SECTION_CATEGORIES = "categories"
    SECTION_THOUGHTS = "thoughts"
    SECTION_QUOTES = "quotes"

    SECTION_CHOICES = [
        (SECTION_FEATURED_ARTICLES, "Featured Articles"),
        (SECTION_CATEGORIES, "Categories"),
        (SECTION_THOUGHTS, "Thoughts"),
        (SECTION_QUOTES, "Quotes"),
    ]

    insight = models.ForeignKey(
        "insights.Insight",
        on_delete=models.CASCADE,
        related_name="section_intros"
    )
    section_key = models.CharField(
        max_length=50,
        choices=SECTION_CHOICES,
        help_text="The section this intro belongs to."
    )
    eyebrow = models.CharField(
        max_length=120,
        blank=True,
        default=""
    )
    title = models.CharField(
        max_length=255
    )
    intro = models.TextField(
        blank=True
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Controls section intro ordering where needed."
    )

    class Meta:
        ordering = ["display_order", "id"]
        verbose_name = "Insight Section Intro"
        verbose_name_plural = "Insight Section Intros"
        unique_together = ("insight", "section_key")

    def __str__(self):
        return f"{self.insight.title} - {self.get_section_key_display()}"