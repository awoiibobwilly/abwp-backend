from django.db.models import Count, Q
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import (
    Project,
    ProjectCategory,
    TechnologyGroup,
)

from projects.models import (
    ProjectsHero,
    ProjectsSectionIntro,
    ProjectContribution,
    ProjectStat,
)

from projects.serializers import (
    ProjectsPageSerializer,
)


# ==========================================================
# PROJECTS PAGE VIEW
# PROJECTS PAGE
# ABW PORTFOLIO
# ==========================================================

class ProjectsPageView(APIView):
    """
    Returns the full Projects page payload.
    """

    def get(self, request, *args, **kwargs):

        # ==================================================
        # PAGE CONTENT
        # ==================================================
        hero = (
            ProjectsHero.objects
            .filter(is_active=True)
            .order_by("-updated_at")
            .first()
        )

        featured_intro = (
            ProjectsSectionIntro.objects
            .filter(
                section_key=ProjectsSectionIntro.FEATURED,
                is_active=True,
            )
            .first()
        )

        categories_intro = (
            ProjectsSectionIntro.objects
            .filter(
                section_key=ProjectsSectionIntro.CATEGORIES,
                is_active=True,
            )
            .first()
        )

        technologies_intro = (
            ProjectsSectionIntro.objects
            .filter(
                section_key=ProjectsSectionIntro.TECHNOLOGIES,
                is_active=True,
            )
            .first()
        )

        beyond_intro = (
            ProjectsSectionIntro.objects
            .filter(
                section_key=ProjectsSectionIntro.BEYOND,
                is_active=True,
            )
            .first()
        )

        beyond_stats = (
            ProjectStat.objects
            .filter(is_active=True)
            .order_by("display_order", "label")
        )

        beyond_items = (
            ProjectContribution.objects
            .filter(is_active=True)
            .order_by("display_order", "title")
        )

        # ==================================================
        # FEATURED PROJECTS
        # ==================================================
        featured_projects = (
            Project.objects
            .filter(
                is_active=True,
                featured=True,
            )
            .select_related("category")
            .prefetch_related(
                "technologies",
                "media",
            )
            .order_by("display_order", "-created_at")
        )

        # ==================================================
        # PROJECT CATEGORIES
        # ==================================================
        categories = (
            ProjectCategory.objects
            .filter(is_active=True)
            .annotate(
                project_count=Count(
                    "projects",
                    filter=Q(projects__is_active=True),
                )
            )
            .order_by("display_order", "name")
        )

        # ==================================================
        # TECHNOLOGY GROUPS
        # ==================================================
        technology_groups = (
            TechnologyGroup.objects
            .filter(is_active=True)
            .prefetch_related("technologies")
            .order_by("display_order", "name")
        )

        # ==================================================
        # RESPONSE PAYLOAD
        # ==================================================
        payload = {
            "hero": hero,
            "featured_intro": featured_intro,
            "featured_projects": featured_projects,
            "categories_intro": categories_intro,
            "categories": categories,
            "technologies_intro": technologies_intro,
            "technology_groups": technology_groups,
            "beyond_intro": beyond_intro,
            "beyond_stats": beyond_stats,
            "beyond_items": beyond_items,
        }

        serializer = ProjectsPageSerializer(
            payload,
            context={"request": request},
        )

        return Response(serializer.data)