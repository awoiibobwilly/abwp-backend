from django.db import models


# ==========================================================
# NEWSLETTER
# NEWSLETTER / SUBSCRIPTION BLOCK FOR INSIGHTS PAGE
# ==========================================================

class Newsletter(models.Model):
    insight = models.OneToOneField(
        "insights.Insight",
        on_delete=models.CASCADE,
        related_name="newsletter"
    )
    eyebrow = models.CharField(
        max_length=120,
        blank=True,
        default="Stay Connected"
    )
    title = models.CharField(
        max_length=255,
        help_text="Newsletter section title."
    )
    description = models.TextField(
        blank=True,
        help_text="Supporting copy for the newsletter block."
    )
    placeholder = models.CharField(
        max_length=150,
        blank=True,
        default="Enter your email address"
    )
    button_text = models.CharField(
        max_length=80,
        blank=True,
        default="Subscribe"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletter"

    def __str__(self):
        return f"Newsletter - {self.insight.title}"