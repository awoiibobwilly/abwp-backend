from django.db import models


# ==========================================================
# QUOTE
# QUOTE / REFLECTION BLOCK FOR THE INSIGHTS PAGE
# ==========================================================

class Quote(models.Model):
    insight = models.ForeignKey(
        "insights.Insight",
        on_delete=models.CASCADE,
        related_name="quotes"
    )
    quote = models.TextField(
        help_text="The quote or reflection text."
    )
    author = models.CharField(
        max_length=120,
        default="Awoii Bob Willy"
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "id"]
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
        return f"{self.author} - {self.quote[:60]}"