from django.db import models

from .insight_page_hero import InsightPageHero


# ==========================================================
# INSIGHT HERO STAT
# STATISTICS DISPLAYED IN THE INSIGHTS HERO
# ==========================================================

class InsightHeroStat(models.Model):

    hero = models.ForeignKey(
        InsightPageHero,
        on_delete=models.CASCADE,
        related_name="stats",
    )

    value = models.CharField(
        max_length=30,
    )

    label = models.CharField(
        max_length=120,
    )

    display_order = models.PositiveIntegerField(
        default=1,
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
        ordering = (
            "display_order",
            "id",
        )

        verbose_name = "Insight Hero Statistic"

        verbose_name_plural = "Insight Hero Statistics"

    def __str__(self):
        return self.label