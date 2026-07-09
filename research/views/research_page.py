from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import (
    Research,
    ResearchPageHero,
    ResearchSectionIntro,
    ResearchArea,
    ResearchMethodologyGroup,
    ResearchInterestGroup,
    ResearchPhilosophyPoint,
)

from ..serializers import (
    ResearchSerializer,
    ResearchPageHeroSerializer,
    ResearchSectionIntroSerializer,
    ResearchAreaSerializer,
    ResearchMethodologyGroupSerializer,
    ResearchInterestGroupSerializer,
    ResearchPhilosophyPointSerializer,
)


class ResearchPageAPIView(APIView):
    """
    Returns the full Research page payload.
    """

    def get(self, request, *args, **kwargs):
        hero = (
            ResearchPageHero.objects
            .filter(is_active=True)
            .order_by("-id")
            .first()
        )

        section_intros = {
            intro.section_key: intro
            for intro in ResearchSectionIntro.objects.filter(
                is_active=True
            )
        }

        areas = (
            ResearchArea.objects
            .filter(is_active=True)
            .order_by("display_order", "title")
        )

        methodology_groups = (
            ResearchMethodologyGroup.objects
            .filter(is_active=True)
            .prefetch_related("items")
            .order_by("display_order", "title")
        )

        interest_groups = (
            ResearchInterestGroup.objects
            .filter(is_active=True)
            .prefetch_related("items")
            .order_by("display_order", "title")
        )

        philosophy_points = (
            ResearchPhilosophyPoint.objects
            .filter(is_active=True)
            .order_by("display_order", "title")
        )

        featured_publications = (
            Research.objects
            .filter(
                published=True,
                featured=True,
            )
            .select_related("category")
            .prefetch_related("keywords")
            .order_by("display_order", "-year")
        )

        all_publications = (
            Research.objects
            .filter(published=True)
            .select_related("category")
            .prefetch_related("keywords")
            .order_by("display_order", "-year")
        )

        data = {
            "hero": (
                ResearchPageHeroSerializer(
                    hero,
                    context={"request": request},
                ).data
                if hero else None
            ),

            "areas_intro": (
                ResearchSectionIntroSerializer(
                    section_intros.get("areas")
                ).data
                if section_intros.get("areas") else None
            ),
            "areas": ResearchAreaSerializer(
                areas,
                many=True,
            ).data,

            "publications_intro": (
                ResearchSectionIntroSerializer(
                    section_intros.get("publications")
                ).data
                if section_intros.get("publications") else None
            ),
            "featured_publications": ResearchSerializer(
                featured_publications,
                many=True,
                context={"request": request},
            ).data,
            "all_publications": ResearchSerializer(
                all_publications,
                many=True,
                context={"request": request},
            ).data,

            "methodologies_intro": (
                ResearchSectionIntroSerializer(
                    section_intros.get("methodologies")
                ).data
                if section_intros.get("methodologies") else None
            ),
            "methodology_groups": ResearchMethodologyGroupSerializer(
                methodology_groups,
                many=True,
            ).data,

            "interests_intro": (
                ResearchSectionIntroSerializer(
                    section_intros.get("interests")
                ).data
                if section_intros.get("interests") else None
            ),
            "interest_groups": ResearchInterestGroupSerializer(
                interest_groups,
                many=True,
            ).data,

            "philosophy_intro": (
                ResearchSectionIntroSerializer(
                    section_intros.get("philosophy")
                ).data
                if section_intros.get("philosophy") else None
            ),
            "philosophy_points": ResearchPhilosophyPointSerializer(
                philosophy_points,
                many=True,
            ).data,
        }

        return Response(data)