from django.db import models


class Statistic(

    models.Model

):

    title = models.CharField(

        max_length=100

    )

    value = models.PositiveIntegerField()

    suffix = models.CharField(

        max_length=10,

        blank=True,

        default=""

    )

    icon = models.CharField(

        max_length=50,

        blank=True

    )

    display_order = models.PositiveIntegerField(

        default=1

    )

    is_active = models.BooleanField(

        default=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = [

            "display_order"

        ]

        verbose_name = "Statistic"

        verbose_name_plural = "Statistics"

    def __str__(

        self

    ):

        return self.title


class Expertise(models.Model):

    title = models.CharField(

        max_length=150

    )

    description = models.TextField()

    icon = models.CharField(

        max_length=100,

        help_text="React Icon name e.g. FaLaptopCode"

    )

    display_order = models.PositiveIntegerField(

        default=0

    )

    is_active = models.BooleanField(

        default=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = [

            "display_order",

            "title",

        ]

    def __str__(self):

        return self.title


class Highlight(models.Model):

    title = models.CharField(
        max_length=100
    )

    value = models.PositiveIntegerField()

    suffix = models.CharField(
        max_length=10,
        default="+"
    )

    icon = models.CharField(
        max_length=100
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "display_order"
        ]

    def __str__(self):

        return self.title

# ========================================
    # TECHNOLOGY MODEL
# ========================================


class Technology(models.Model):

    name = models.CharField(

        max_length=100,

        unique=True,

        help_text="Technology name (e.g., React, Django, PostgreSQL)"

    )

    slug = models.SlugField(

        unique=True

    )

    icon = models.CharField(

        max_length=100,

        help_text="React icon name (e.g., FaReact)",

        blank=True,

    )

    color = models.CharField(

        max_length=20,

        default="#2563eb",

        help_text="Primary brand color (Hex code)"

    )

    website = models.URLField(

        blank=True

    )

    description = models.TextField(

        blank=True

    )

    proficiency = models.PositiveSmallIntegerField(

        default=80,

        help_text="Proficiency percentage (0–100)"

    )

    display_order = models.PositiveIntegerField(

        default=0

    )

    is_active = models.BooleanField(

        default=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = [

            "display_order",

            "name",

        ]

        verbose_name = "Technology"

        verbose_name_plural = "Technologies"

    def __str__(self):

        return self.name
    
# ==================================
    # PROJECT CATEGORY MODEL
# ==================================


class ProjectCategory(models.Model):

    name = models.CharField(

        max_length=100,

        unique=True,

        help_text="Category name (e.g. Healthcare, Web Development)"

    )

    slug = models.SlugField(

        unique=True

    )

    icon = models.CharField(

        max_length=100,

        blank=True,

        help_text="React icon name (e.g. FaHospital)"

    )

    color = models.CharField(

        max_length=20,

        default="#2563eb",

        help_text="Hex color used for badges"

    )

    description = models.TextField(

        blank=True

    )

    display_order = models.PositiveIntegerField(

        default=0

    )

    is_active = models.BooleanField(

        default=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = [

            "display_order",

            "name",

        ]

        verbose_name = "Project Category"

        verbose_name_plural = "Project Categories"

    def __str__(self):

        return self.name
    
# =======================================
    # PROJECT MODEL
# =======================================


class Project(models.Model):

    STATUS_CHOICES = [

        ("planning", "Planning"),

        ("in_progress", "In Progress"),

        ("completed", "Completed"),

        ("maintenance", "Maintenance"),

        ("archived", "Archived"),

    ]

    title = models.CharField(

        max_length=200

    )

    slug = models.SlugField(

        unique=True

    )

    category = models.ForeignKey(

        ProjectCategory,

        on_delete=models.PROTECT,

        related_name="projects"

    )

    technologies = models.ManyToManyField(

        Technology,

        blank=True,

        related_name="projects"

    )

    short_description = models.CharField(

        max_length=300,

        help_text="Displayed on project cards."

    )

    description = models.TextField(

        help_text="Full project description."

    )

    thumbnail = models.ImageField(

        upload_to="projects/thumbnails/",

        blank=True,

        null=True,

    )

    client = models.CharField(

        max_length=200,

        blank=True

    )

    organization = models.CharField(

        max_length=200,

        blank=True

    )

    role = models.CharField(

        max_length=200,

        blank=True,

        help_text="Your role in this project."

    )

    github_url = models.URLField(

        blank=True

    )

    live_url = models.URLField(

        blank=True

    )

    # ==========================
    # SEO & Social Sharing
    # ==========================

    meta_title = models.CharField(

        max_length=70,

        blank=True,

        help_text="SEO title (recommended: 50–60 characters)."

    )

    meta_description = models.CharField(

        max_length=160,

        blank=True,

        help_text="SEO description (recommended: 150–160 characters)."

    )

    keywords = models.CharField(

        max_length=300,

        blank=True,

        help_text="Comma-separated SEO keywords."

    )

    canonical_url = models.URLField(

        blank=True,

        help_text="Optional canonical URL."

    )

    og_image = models.ImageField(

        upload_to="projects/og/",

        blank=True,

        null=True,

        help_text="Open Graph image used for LinkedIn, Facebook, WhatsApp, etc."

    )

    documentation_url = models.URLField(

        blank=True

    )

    featured = models.BooleanField(

        default=False

    )

    is_open_source = models.BooleanField(

        default=False

    )

    is_active = models.BooleanField(

        default=True

    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="completed",

    )

    started_at = models.DateField(

        blank=True,

        null=True

    )

    completed_at = models.DateField(

        blank=True,

        null=True

    )

    display_order = models.PositiveIntegerField(

        default=0

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = [

            "display_order",

            "-created_at",

        ]

        verbose_name = "Project"

        verbose_name_plural = "Projects"

    def __str__(self):

        return self.title
    
# ======================================
    # PROJECT MEDIA
# ======================================


class ProjectMedia(models.Model):

    MEDIA_TYPE_CHOICES = [

        ("image", "Image"),

        ("video", "Video"),

        ("document", "Document"),

    ]

    project = models.ForeignKey(

        Project,

        on_delete=models.CASCADE,

        related_name="media"

    )

    media_type = models.CharField(

        max_length=20,

        choices=MEDIA_TYPE_CHOICES,

        default="image"

    )

    file = models.FileField(

        upload_to="projects/media/"

    )

    thumbnail = models.ImageField(

        upload_to="projects/media/thumbnails/",

        blank=True,

        null=True,

        help_text="Thumbnail used for videos or documents."

    )

    title = models.CharField(

        max_length=200,

        blank=True

    )

    caption = models.TextField(

        blank=True

    )

    alt_text = models.CharField(

        max_length=200,

        blank=True,

        help_text="Accessibility text."

    )

    display_order = models.PositiveIntegerField(

        default=0

    )

    featured_on_home = models.BooleanField(

        default=False,

        help_text="Use this media as the preview on the Home page."

    )

    is_featured = models.BooleanField(

        default=False,

        help_text="Primary media for the Project Detail page."

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )

    class Meta:

        ordering = [

            "display_order",

            "created_at",

        ]

        verbose_name = "Project Media"

        verbose_name_plural = "Project Media"

    def __str__(self):

        return f"{self.project.title} - {self.title or self.media_type}"

# ========================================
    # JOURNEY MODEL
# ========================================


class Journey(models.Model):

    JOURNEY_TYPES = (
        ("education", "Education"),
        ("employment", "Employment"),
        ("leadership", "Leadership"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("award", "Award"),
        ("project", "Major Project"),
        ("milestone", "Career Milestone"),
    )

    title = models.CharField(
        max_length=255,
    )

    organization = models.CharField(
        max_length=255,
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    journey_type = models.CharField(
        max_length=20,
        choices=JOURNEY_TYPES,
    )

    summary = models.TextField()

    image = models.ImageField(
        upload_to="journey/",
        blank=True,
        null=True,
    )

    started_at = models.DateField()

    ended_at = models.DateField(
        blank=True,
        null=True,
    )

    is_current = models.BooleanField(
        default=False,
    )

    featured = models.BooleanField(
        default=False,
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
    slug = models.SlugField(
        unique=True,
    )

    class Meta:

        ordering = (
            "-started_at",
            "display_order",
        )

    def __str__(self):

        return self.title