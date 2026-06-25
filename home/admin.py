from django.contrib import admin

from copy import deepcopy

from django.utils.html import format_html

from django.utils.safestring import mark_safe

from .models import (
    Statistic,
    Expertise,
    Highlight,
    Technology,
    ProjectCategory,
    Project,
    ProjectMedia,
    Journey,

)


@admin.register(

    Statistic

)
class StatisticAdmin(

    admin.ModelAdmin

):

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


class ProjectMediaInline(admin.StackedInline):

    @admin.display(description="Preview")
    def preview(self, obj):

        if obj.file and obj.media_type == "image":

            return format_html(

                '<img src="{}" style="height:120px;border-radius:8px;" />',

                obj.file.url,

            )

        return "-"

    model = ProjectMedia

    extra = 1

    ordering = (

        "display_order",

    )

    readonly_fields = (

        "preview",

    )

    fields = (
        "media_type",

        "file",

        "preview",

        "thumbnail",

        "title",

        "caption",

        "alt_text",
    )

    show_change_link = True


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    @admin.action(description="Duplicate selected projects")
    def duplicate_projects(self, request, queryset):

        for project in queryset:

            technologies = list(

                project.technologies.all()

            )

            media = list(

                project.media.all()

            )

            project.pk = None

            project.slug = f"{project.slug}-copy"

            project.title = f"{project.title} (Copy)"

            project.save()

            project.technologies.set(

                technologies

            )

            for item in media:

                item.pk = None

                item.project = project

                item.save()

    @admin.action(description="Archive selected projects")
    def archive_projects(self, request, queryset):

        queryset.update(

            status="archived"

        )

    @admin.action(description="Unpublish selected projects")
    def unpublish_projects(self, request, queryset):

        queryset.update(

            is_active=False

        )

    @admin.action(description="Publish selected projects")
    def publish_projects(self, request, queryset):

        queryset.update(

            is_active=True

        )

    @admin.action(description="Mark selected projects as Featured")
    def mark_featured(self, request, queryset):

        queryset.update(

            featured=True

        )

    actions = [

        "mark_featured",

        "publish_projects",

        "unpublish_projects",

        "archive_projects",

        "duplicate_projects",

    ]

    @admin.display(description="Status")
    def colored_status(self, obj):

        colors = {

            "planning": "#6b7280",

            "in_progress": "#2563eb",

            "completed": "#16a34a",

            "maintenance": "#ea580c",

            "archived": "#dc2626",

        }

        color = colors.get(

            obj.status,

            "#374151",

        )

        return format_html(

            '<strong style="color:{};">{}</strong>',

            color,

            obj.get_status_display(),

        )

# ==========================================================
    # Thumbnail Preview
# ==========================================================

    @admin.display(description="Thumbnail")
    def thumbnail_preview(self, obj):

        if obj.thumbnail:

            return format_html(

                '<img src="{}" style="height:70px;border-radius:8px;" />',

                obj.thumbnail.url,

            )

        return "-"

    # ==========================================================
    # Inline Models
    # ==========================================================

    inlines = (ProjectMediaInline,
        )

    # ==========================================================
    # List View
    # ==========================================================

    readonly_fields = (

        "thumbnail_preview",

        "created_at",

        "updated_at",

    )

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

    list_display_links = (
        "title",
    )

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

    ordering = (
        "display_order",
        "-created_at",
    )

    date_hierarchy = "created_at"

    list_per_page = 20

    list_select_related = (
        "category",
    )

    # ==========================================================
    # Form Configuration
    # ==========================================================

    autocomplete_fields = (
        "category",
    )

    filter_horizontal = (
        "technologies",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    save_on_top = True

    # ==========================================================
    # Fieldsets
    # ==========================================================

    fieldsets = (

        (
            "Project Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "technologies",
                    "short_description",
                    "description",
                ),
            },
        ),

        (
            "Media",
            {
                "fields": (
                    "thumbnail",

                    "thumbnail_preview",
                ),
            },
        ),

        (
            "Project Details",
            {
                "fields": (
                    "client",
                    "organization",
                    "role",
                    "status",
                    "started_at",
                    "completed_at",
                ),
            },
        ),

        (
            "Project Links",
            {
                "fields": (
                    "github_url",
                    "live_url",
                    "documentation_url",
                ),
            },
        ),

        (
            "SEO & Social Sharing",
            {
                "classes": ("collapse",),
                "fields": (
                    "meta_title",
                    "meta_description",
                    "keywords",
                    "canonical_url",
                    "og_image",
                ),
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "featured",
                    "is_open_source",
                    "is_active",
                    "display_order",
                ),
            },
        ),

        (
            "Audit Information",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
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

    date_hierarchy = "created_at"

    list_per_page = 20

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "proficiency",
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

    list_per_page = 20

    prepopulated_fields = {
        "slug": ("name",),
    }


class ProjectMediaInline(admin.StackedInline):

    model = ProjectMedia

    extra = 1

    ordering = (
        "display_order",
    )

    show_change_link = True

    fieldsets = (

        (
            None,
            {
                "fields": (
                    "media_type",
                    "file",
                    "thumbnail",
                    "title",
                    "caption",
                    "alt_text",
                ),
            },
        ),

        (
            "Display Options",
            {
                "fields": (
                    "display_order",
                    "featured_on_home",
                    "is_featured",
                ),
            },
        ),

    )

# ========================================
    # JOURNEY
# ========================================


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