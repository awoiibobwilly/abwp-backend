from rest_framework import serializers

from home.models import (
    Project,
    ProjectCategory,
    TechnologyGroup,
)

from home.serializers import (
    FeaturedProjectSerializer,
)

from projects.models import (
    ProjectsHero,
    ProjectsSectionIntro,
    ProjectContribution,
    ProjectStat,
)


# ==========================================================
# PROJECTS HERO SERIALIZER
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectsHeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectsHero
        fields = (
            "id",
            "eyebrow",
            "title",
            "description",
        )


# ==========================================================
# PROJECTS SECTION INTRO SERIALIZER
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectsSectionIntroSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectsSectionIntro
        fields = (
            "id",
            "section_key",
            "eyebrow",
            "title",
            "intro",
        )


# ==========================================================
# PROJECT CONTRIBUTION SERIALIZER
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectContributionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectContribution
        fields = (
            "id",
            "title",
            "description",
            "icon",
            "display_order",
        )


# ==========================================================
# PROJECT STAT SERIALIZER
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectStat
        fields = (
            "id",
            "value",
            "label",
            "display_order",
        )


# ==========================================================
# PROJECT CATEGORY CARD SERIALIZER
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectCategoryCardSerializer(serializers.ModelSerializer):
    project_count = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = ProjectCategory
        fields = (
            "id",
            "name",
            "slug",
            "icon",
            "color",
            "description",
            "project_count",
        )


# ==========================================================
# TECHNOLOGY ITEM SERIALIZER
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class TechnologyGroupItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.CharField()
    icon = serializers.CharField(
        allow_blank=True
    )
    color = serializers.CharField()
    proficiency = serializers.IntegerField()


# ==========================================================
# TECHNOLOGY GROUP SERIALIZER
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class TechnologyGroupSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        source="name"
    )
    items = serializers.SerializerMethodField()

    class Meta:
        model = TechnologyGroup
        fields = (
            "id",
            "title",
            "slug",
            "items",
        )

    def get_items(self, obj):
        technologies = (
            obj.technologies
            .filter(is_active=True)
            .order_by("display_order", "name")
        )

        return [
            {
                "id": tech.id,
                "name": tech.name,
                "slug": tech.slug,
                "icon": tech.icon,
                "color": tech.color,
                "proficiency": tech.proficiency,
            }
            for tech in technologies
        ]


# ==========================================================
# PROJECTS PAGE SERIALIZER
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectsPageSerializer(serializers.Serializer):
    hero = ProjectsHeroSerializer(
        allow_null=True
    )

    featured_intro = ProjectsSectionIntroSerializer(
        allow_null=True
    )

    featured_projects = FeaturedProjectSerializer(
        many=True
    )

    categories_intro = ProjectsSectionIntroSerializer(
        allow_null=True
    )

    categories = ProjectCategoryCardSerializer(
        many=True
    )

    technologies_intro = ProjectsSectionIntroSerializer(
        allow_null=True
    )

    technology_groups = TechnologyGroupSerializer(
        many=True
    )

    beyond_intro = ProjectsSectionIntroSerializer(
        allow_null=True
    )

    beyond_stats = ProjectStatSerializer(
        many=True
    )

    beyond_items = ProjectContributionSerializer(
        many=True
    )