from django.db import models


# ==========================================================
# INSIGHT PAGE HERO
# HERO CONTENT FOR THE INSIGHTS PAGE
# ==========================================================

class InsightPageHero(models.Model):
    insight = models.OneToOneField(
        "insights.Insight",
        on_delete=models.CASCADE,
        related_name="hero"
    )
    eyebrow = models.CharField(
        max_length=120,
        blank=True,
        default="Insights & Perspectives"
    )
    title = models.CharField(
        max_length=255,
        help_text="Main hero title for the Insights page."
    )
    subtitle = models.TextField(
        blank=True,
        help_text="Supporting hero subtitle / description."
    )

    description = models.TextField(
        blank=True,
        help_text="Supporting hero subtitle / description."
    )

    class Meta:
        verbose_name = "Insight Page Hero"
        verbose_name_plural = "Insight Page Hero"

    def __str__(self):
        return f"Hero - {self.insight.title}"