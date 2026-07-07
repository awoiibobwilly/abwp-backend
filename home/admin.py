from django.contrib import admin

from django.utils.html import format_html


from .models import (
    Statistic,
    Expertise,
    Highlight,
    Technology,
    ProjectCategory,
    Project,
    ProjectMedia,
    Journey,
    Testimonial,
    TechnologyGroup,
)

# ==========================================================
# STATISTICS
# ==========================================================

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "value",
        "suffix",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "display_order",
    )


# ==========================================================
# EXPERTISE
# ==========================================================

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "display_order",
    )


# ==========================================================
# HIGHLIGHTS
# ==========================================================

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "display_order",
    )


# ==========================================================
# TECHNOLOGIES
# ==========================================================

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "group",
        "proficiency",
        "display_order",
        "is_active",
    )

    list_display_links = (
        "name",
    )

    list_filter = (
        "group",
        "proficiency",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "display_order",
        "name",
    )

    list_per_page = 25

    prepopulated_fields = {
        "slug": ("name",),
    }


# ==========================================================
# TECHNOLOGY GROUPS
# ==========================================================


@admin.register(TechnologyGroup)
class TechnologyGroupAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "display_order",
        "is_active",
        "updated_at",
    )

    list_display_links = (
        "name",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "display_order",
        "name",
    )

    list_per_page = 25

    prepopulated_fields = {
        "slug": ("name",),
    }


# ==========================================================
# PROJECT CATEGORIES
# ==========================================================

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "display_order",
        "is_active",
        "created_at",
    )

    list_display_links = (
        "name",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "display_order",
        "name",
    )

    date_hierarchy = "created_at"

    list_per_page = 25

    prepopulated_fields = {
        "slug": ("name",),
    }


# ==========================================================
# JOURNEY
# ==========================================================

@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "journey_type",
        "started_at",
        "is_current",
        "featured",
        "is_active",
    )

    list_display_links = (
        "title",
    )

    list_filter = (
        "journey_type",
        "featured",
        "is_current",
        "is_active",
    )

    search_fields = (
        "title",
        "organization",
        "summary",
    )

    ordering = (
        "-started_at",
    )

    date_hierarchy = "started_at"

    list_per_page = 25

# ==========================================================
# PROJECT MEDIA INLINE
# ==========================================================

class ProjectMediaInline(admin.StackedInline):

    model = ProjectMedia

    extra = 1

    show_change_link = True

    ordering = (
        "display_order",
    )

    # ======================================================
    # Read-only Preview
    # ======================================================

    readonly_fields = (
        "media_preview",
    )

    @admin.display(description="Media Preview")
    def media_preview(self, obj):

        if not obj or not obj.pk:

            return "Save this media item to preview it."

        if not obj.file:

            return "No media uploaded."

        if obj.media_type == "image":

            return format_html(
                """
                <img
                    src="{}"
                    style="
                        max-height:160px;
                        border-radius:8px;
                        border:1px solid #ddd;
                        padding:4px;
                        background:#fff;
                    "
                />
                """,
                obj.file.url,
            )

        return format_html(
            '<a href="{}" target="_blank">View File</a>',
            obj.file.url,
        )

    # ======================================================
    # Form Layout
    # ======================================================

    fieldsets = (

        (
            "Media Information",
            {
                "fields": (

                    "media_type",

                    "file",

                    "media_preview",

                    "thumbnail",

                    "title",

                    "caption",

                    "alt_text",

                ),
            },
        ),

        (
            "Display Settings",
            {
                "fields": (

                    "display_order",

                    "featured_on_home",

                    "is_featured",

                ),
            },
        ),

    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    # ==========================
    # Inlines
    # ==========================
    inlines = (ProjectMediaInline,)

    # ==========================
    # Read Only Fields
    # ==========================
    readonly_fields = (
        "thumbnail_preview",
        "created_at",
        "updated_at",
    )

    # ==========================
    # Display Helpers
    # ==========================
    @admin.display(description="Status")
    def colored_status(self, obj):
        colors = {
            "planning": "#6b7280",
            "in_progress": "#2563eb",
            "completed": "#16a34a",
            "maintenance": "#ea580c",
            "archived": "#dc2626",
        }
        return format_html(
            '<strong style="color:{};">{}</strong>',
            colors.get(obj.status, "#374151"),
            obj.get_status_display(),
        )

    @admin.display(description="Thumbnail Preview")
    def thumbnail_preview(self, obj):
        if obj and obj.pk and obj.thumbnail:
            return format_html(
                '<img src="{}" style="max-height:180px;border-radius:8px;border:1px solid #ddd;padding:4px;" />',
                obj.thumbnail.url,
            )
        return "Save the project before previewing the thumbnail."

    # ==========================
    # Actions
    # ==========================
    @admin.action(description="Mark selected projects as Featured")
    def mark_featured(self, request, queryset):
        queryset.update(featured=True)

    @admin.action(description="Publish selected projects")
    def publish_projects(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Unpublish selected projects")
    def unpublish_projects(self, request, queryset):
        queryset.update(is_active=False)

    @admin.action(description="Archive selected projects")
    def archive_projects(self, request, queryset):
        queryset.update(status="archived")

    @admin.action(description="Duplicate selected projects")
    def duplicate_projects(self, request, queryset):
        from django.utils.text import slugify

        for original in queryset:
            technologies = list(original.technologies.all())
            media_items = list(original.media.all())

            copy = original
            copy.pk = None
            copy.title = f"{original.title} (Copy)"

            base_slug = slugify(copy.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                counter += 1
                slug = f"{base_slug}-{counter}"

            copy.slug = slug
            copy.save()
            copy.technologies.set(technologies)

            for media in media_items:
                media.pk = None
                media.project = copy
                media.save()

    actions = (
        "mark_featured",
        "publish_projects",
        "unpublish_projects",
        "archive_projects",
        "duplicate_projects",
    )

    # ==========================
    # List View
    # ==========================
    list_display = (
        "title",
        "category",
        "colored_status",
        "featured",
        "is_open_source",
        "is_active",
        "display_order",
        "created_at",
    )

    list_display_links = ("title",)

    list_editable = (
        "featured",
        "is_active",
        "display_order",
    )

    list_filter = (
        "category",
        "status",
        "featured",
        "is_open_source",
        "is_active",
        "technologies",
    )

    search_fields = (
        "title",
        "client",
        "organization",
        "role",
        "short_description",
        "description",
        "meta_title",
        "meta_description",
        "keywords",
    )

    ordering = ("display_order", "-created_at")

    list_select_related = ("category",)

    date_hierarchy = "created_at"

    list_per_page = 20

    # ==========================
    # Form
    # ==========================
    autocomplete_fields = ("category",)

    filter_horizontal = ("technologies",)

    prepopulated_fields = {
        "slug": ("title",),
    }

    save_on_top = True

    fieldsets = (
        ("Project Information", {
            "fields": (
                "title",
                "slug",
                "category",
                "technologies",
                "short_description",
                "description",
            )
        }),
        ("Media", {
            "fields": (
                "thumbnail",
                "thumbnail_preview",
            )
        }),
        ("Project Details", {
            "fields": (
                "client",
                "organization",
                "role",
                "status",
                "started_at",
                "completed_at",
            )
        }),
        ("Project Links", {
            "fields": (
                "github_url",
                "live_url",
                "documentation_url",
            )
        }),
        ("SEO & Social Sharing", {
            "classes": ("collapse",),
            "fields": (
                "meta_title",
                "meta_description",
                "keywords",
                "canonical_url",
                "og_image",
            )
        }),
        ("Publishing", {
            "fields": (
                "featured",
                "is_open_source",
                "is_active",
                "display_order",
            )
        }),
        ("Audit Information", {
            "classes": ("collapse",),
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )


# ==========================================================
# TESTIMONIALS
# ==========================================================

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (

        "name",

        "organisation",

        "position",

        "rating",

        "featured",

        "published",

        "display_order",

    )

    list_display_links = (

        "name",

    )

    list_editable = (

        "featured",

        "published",

        "display_order",

    )

    list_filter = (

        "featured",

        "published",

        "rating",

    )

    search_fields = (

        "name",

        "organisation",

        "position",

        "quote",

    )

    ordering = (

        "display_order",

        "name",

    )

    prepopulated_fields = {

        "slug": ("name",),

    }

    list_per_page = 25

    date_hierarchy = "created_at"
