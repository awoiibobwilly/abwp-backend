from django.db import models

from django.utils.text import slugify

from .research_category import ResearchCategory


class Research(models.Model):

    STATUS_CHOICES = [

        ("published", "Published"),

        ("accepted", "Accepted"),

        ("under_review", "Under Review"),

        ("draft", "Draft"),

        ("archived", "Archived"),

    ]

    PUBLICATION_TYPES = [

        ("journal_article", "Journal Article"),

        ("conference_paper", "Conference Paper"),

        ("book_chapter", "Book Chapter"),

        ("technical_report", "Technical Report"),

        ("case_study", "Case Study"),

        ("white_paper", "White Paper"),

        ("research_proposal", "Research Proposal"),

        ("dissertation", "Dissertation"),

    ]

    title = models.CharField(

        max_length=255,

    )

    slug = models.SlugField(

        unique=True,

        blank=True,

    )

    category = models.ForeignKey(

        ResearchCategory,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="research",

    )

    publication_type = models.CharField(

        max_length=50,

        choices=PUBLICATION_TYPES,

    )

    authors = models.CharField(

        max_length=500,

    )

    institution = models.CharField(

        max_length=255,

        blank=True,

    )

    journal = models.CharField(

        max_length=255,

        blank=True,

    )

    publisher = models.CharField(

        max_length=255,

        blank=True,

    )

    year = models.PositiveIntegerField()

    abstract = models.TextField()

    summary = models.TextField(

        help_text="Short summary for homepage previews.",

    )

    keywords = models.ManyToManyField(

        "ResearchKeyword",

        blank=True,

        related_name="research",

    )

    featured_image = models.ImageField(

        upload_to="research/images/",

        blank=True,

        null=True,

    )

    pdf = models.FileField(

        upload_to="research/papers/",

        blank=True,

        null=True,

    )

    doi = models.CharField(

        max_length=255,

        blank=True,

    )

    external_url = models.URLField(

        blank=True,

    )

    status = models.CharField(

        max_length=30,

        choices=STATUS_CHOICES,

        default="published",

    )

    featured = models.BooleanField(

        default=False,

    )

    published = models.BooleanField(

        default=True,

    )

    display_order = models.PositiveIntegerField(

        default=0,

    )

    created_at = models.DateTimeField(

        auto_now_add=True,

    )

    updated_at = models.DateTimeField(

        auto_now=True,

    )

    class Meta:

        ordering = [

            "display_order",

            "-year",

            "-created_at",

        ]

        verbose_name = "Research"

        verbose_name_plural = "Research"

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(

                self.title

            )

        super().save(

            *args,

            **kwargs,

        )

    def __str__(self):

        return self.title