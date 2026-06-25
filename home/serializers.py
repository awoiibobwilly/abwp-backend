from rest_framework import serializers

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


class StatisticSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Statistic

        fields = "__all__"


class ExpertiseSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Expertise

        fields = "__all__"


class HighlightSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = Highlight

        fields = "__all__"


# ================================
    # PROJECT CATEGORY
# ================================


class ProjectCategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = ProjectCategory

        fields = (

            "id",

            "name",

            "slug",

            "icon",

            "color",

            "description",

        )

# ===================================
    # TECHNOLOGY
# ===================================


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:

        model = Technology

        fields = (

            "id",

            "name",

            "slug",

            "icon",

            "color",

            "proficiency",

        )

# =======================================
    # PROJECT MEDIA
# =======================================


class ProjectMediaSerializer(serializers.ModelSerializer):

    file = serializers.SerializerMethodField()

    thumbnail = serializers.SerializerMethodField()

    class Meta:

        model = ProjectMedia

        fields = (

            "id",

            "media_type",

            "file",

            "thumbnail",

            "title",

            "caption",

            "alt_text",

            "display_order",

            "featured_on_home",

            "is_featured",

            "created_at",

        )

    def get_file(self, obj):

        request = self.context.get("request")

        if obj.file:

            if request:

                return request.build_absolute_uri(obj.file.url)

            return obj.file.url

        return None

    def get_thumbnail(self, obj):

        request = self.context.get("request")

        if obj.thumbnail:

            if request:

                return request.build_absolute_uri(
                    obj.thumbnail.url
                )

            return obj.thumbnail.url

        return None

# ===========================================
    # PROJECT
# ===========================================


class ProjectSerializer(serializers.ModelSerializer):

    hero_media = serializers.SerializerMethodField()

    category = ProjectCategorySerializer(

        read_only=True

    )

    technologies = TechnologySerializer(

        many=True,

        read_only=True

    )

    media = ProjectMediaSerializer(

        many=True,

        read_only=True

    )

    thumbnail = serializers.SerializerMethodField()

    og_image = serializers.SerializerMethodField()

    class Meta:

        model = Project

        fields = (

            "id",

            "title",

            "slug",

            "category",

            "technologies",

            "short_description",

            "description",

            "thumbnail",

            "client",

            "organization",

            "role",

            "github_url",

            "live_url",

            "documentation_url",

            "featured",

            "is_open_source",

            "status",

            "started_at",

            "completed_at",

            "meta_title",

            "meta_description",

            "keywords",

            "canonical_url",

            "og_image",

            "hero_media",

            "media",

        )

    def get_hero_media(self, obj):

        request = self.context.get("request")

        media = next(

            (

                item

                for item in obj.media.all()

                if item.is_featured

            ),

            None,

        )

        if media is None:

            media = obj.media.first()

        if media is None:

            return None

        file_url = (

            request.build_absolute_uri(

                media.file.url

            )

            if request and media.file

            else media.file.url

        )

        return {

            "type": media.media_type,

            "file": file_url,

            "title": media.title,

            "caption": media.caption,

        }

    def get_thumbnail(self, obj):

        request = self.context.get("request")

        if obj.thumbnail:

            if request:

                return request.build_absolute_uri(
                    obj.thumbnail.url
                )

            return obj.thumbnail.url

        return None

    def get_og_image(self, obj):

        request = self.context.get("request")

        if obj.og_image:

            if request:

                return request.build_absolute_uri(
                    obj.og_image.url
                )

            return obj.og_image.url

        return None
    
# =====================================
        # FEATURED PROJECT
# =====================================


class FeaturedProjectSerializer(serializers.ModelSerializer):

    category = ProjectCategorySerializer(
        read_only=True,
    )

    technologies = TechnologySerializer(
        many=True,
        read_only=True,
    )

    home_media = serializers.SerializerMethodField()

    class Meta:

        model = Project

        fields = (
            "id",
            "title",
            "slug",
            "category",
            "technologies",
            "short_description",
            "featured",
            "status",
            "live_url",
            "github_url",
            "home_media",
        )

    def get_home_media(self, obj):

        request = self.context.get("request")

        media = next(
            (
                item
                for item in obj.media.all()
                if item.featured_on_home
            ),
            None,
        )

        if media is None and obj.media.all():
            media = obj.media.all()[0]

        if media is None:
            return None

        file_url = (
            request.build_absolute_uri(media.file.url)
            if request and media.file
            else media.file.url if media.file else None
        )

        return {
            "type": media.media_type,
            "file": file_url,
            "title": media.title,
            "caption": media.caption,
        }

# ==============================
    # JOURNEY
# ==============================


class JourneySerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:

        model = Journey

        fields = (
            "id",
            "title",
            "organization",
            "location",
            "journey_type",
            "summary",
            "image",
            "started_at",
            "ended_at",
            "is_current",
            "featured",
            "slug",
        )

    def get_image(self, obj):

        request = self.context.get("request")

        if obj.image:

            if request:

                return request.build_absolute_uri(
                    obj.image.url
                )

            return obj.image.url

        return None