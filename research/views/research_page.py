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


# ==========================================================
# HELPERS
# ==========================================================

def serialize_section_intro(section_intros, section_key):
    """
    Safely serialize a section intro by its section key.

    Returns:
        - serialized section intro object if found
        - None if no intro exists for that section
    """
    intro = section_intros.get(section_key)

    if not intro:
        return None

    return ResearchSectionIntroSerializer(intro).data


def serialize_optional_instance(serializer_class, instance, **kwargs):
    """
    Safely serialize a single optional model instance.

    Returns:
        - serialized object if instance exists
        - None if instance is missing
    """
    if not instance:
        return None

    return serializer_class(instance, **kwargs).data


# ==========================================================
# RESEARCH PAGE API VIEW
# ==========================================================

class ResearchPageAPIView(APIView):
    """
    Returns the full Research page payload.
    """

    def get(self, request, *args, **kwargs):
        # ==================================================
        # HERO
        # ==================================================

        hero = (
            ResearchPageHero.objects
            .filter(is_active=True)
            .order_by("-updated_at", "-id")
            .first()
        )

        # ==================================================
        # SECTION INTROS
        # ==================================================

        section_intros = {
            intro.section_key: intro
            for intro in ResearchSectionIntro.objects.filter(
                is_active=True
            )
        }

        # ==================================================
        # RESEARCH AREAS
        # ==================================================

        areas = (
            ResearchArea.objects
            .filter(is_active=True)
            .order_by("display_order", "title")
        )

        # ==================================================
        # METHODOLOGIES
        # ==================================================

        methodology_groups = (
            ResearchMethodologyGroup.objects
            .filter(is_active=True)
            .order_by("display_order", "title")
        )

        # ==================================================
        # RESEARCH INTERESTS
        # ==================================================

        interest_groups = (
            ResearchInterestGroup.objects
            .filter(is_active=True)
            .order_by("display_order", "title")
        )

        # ==================================================
        # RESEARCH PHILOSOPHY
        # ==================================================

        philosophy_points = (
            ResearchPhilosophyPoint.objects
            .filter(is_active=True)
            .order_by("display_order", "title")
        )

        # ==================================================
        # PUBLICATIONS
        # ==================================================

        featured_publications = (
            Research.objects
            .filter(
                published=True,
                featured=True,
            )
            .select_related("category")
            .prefetch_related("keywords")
            .order_by("display_order", "-year", "title")
        )

        all_publications = (
            Research.objects
            .filter(published=True)
            .select_related("category")
            .prefetch_related("keywords")
            .order_by("display_order", "-year", "title")
        )

        # ==================================================
        # RESPONSE PAYLOAD
        # ==================================================

        data = {
            "hero": serialize_optional_instance(
                ResearchPageHeroSerializer,
                hero,
                context={"request": request},
            ),

            "areas_intro": serialize_section_intro(
                section_intros,
                "areas",
            ),
            "areas": ResearchAreaSerializer(
                areas,
                many=True,
            ).data,

            "publications_intro": serialize_section_intro(
                section_intros,
                "publications",
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

            "methodologies_intro": serialize_section_intro(
                section_intros,
                "methodologies",
            ),
            "methodology_groups": ResearchMethodologyGroupSerializer(
                methodology_groups,
                many=True,
            ).data,

            "interests_intro": serialize_section_intro(
                section_intros,
                "interests",
            ),
            "interest_groups": ResearchInterestGroupSerializer(
                interest_groups,
                many=True,
            ).data,

            "philosophy_intro": serialize_section_intro(
                section_intros,
                "philosophy",
            ),
            "philosophy_points": ResearchPhilosophyPointSerializer(
                philosophy_points,
                many=True,
            ).data,
        }

        return Response(data)