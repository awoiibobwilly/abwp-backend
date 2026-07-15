from django.db import models
from django.utils.text import slugify

from core.models import BasePortfolioModel

from .knowledge_theme import KnowledgeTheme
from .knowledge_tag import KnowledgeTag


# ==========================================================
# RESEARCH CONTRIBUTION
# ORIGINAL SCHOLARLY WORK
# ==========================================================

class ResearchContribution(BasePortfolioModel):

    class ContributionType(models.TextChoices):

        JOURNAL = "journal", "Journal Article"

        CONFERENCE = "conference", "Conference Paper"

        THESIS = "thesis", "Thesis"

        DISSERTATION = "dissertation", "Dissertation"

        TECHNICAL_REPORT = (
            "technical_report",
            "Technical Report",
        )

        CASE_STUDY = "case_study", "Case Study"

        WHITE_PAPER = "white_paper", "White Paper"

        RESEARCH_REPORT = (
            "research_report",
            "Research Report",
        )

        OTHER = "other", "Other"

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        max_length=280,
        unique=True,
        blank=True
    )

    contribution_type = models.CharField(
        max_length=30,
        choices=ContributionType.choices,
        default=ContributionType.JOURNAL
    )

    summary = models.TextField()

    abstract = models.TextField(
        blank=True
    )

    publication = models.CharField(
        max_length=255,
        blank=True,
        help_text="Journal, conference or publisher."
    )

    publication_date = models.DateField(
        blank=True,
        null=True
    )

    cover_image = models.ImageField(
        upload_to="portfolio/hub/research/covers/",
        blank=True,
        null=True
    )

    document = models.FileField(
        upload_to="portfolio/hub/research/documents/",
        blank=True,
        null=True
    )

    external_url = models.URLField(
        blank=True
    )

    doi = models.CharField(
        max_length=120,
        blank=True
    )

    themes = models.ManyToManyField(
        KnowledgeTheme,
        related_name="research_contributions",
        blank=True
    )

    tags = models.ManyToManyField(
        KnowledgeTag,
        related_name="research_contributions",
        blank=True
    )

    class Meta:

        ordering = [
            "display_order",
            "-publication_date",
            "title",
        ]

        verbose_name = "Research Contribution"

        verbose_name_plural = "Research Contributions"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title