from rest_framework.response import Response
from rest_framework.views import APIView

from journey.models import (
    JourneyHero,
    JourneySectionIntro,
    FutureFocus,
)
from journey.serializers import JourneyPageSerializer

from home.models import Journey


class JourneyPageAPIView(APIView):
    """
    Returns the full Journey page payload:
    - hero
    - timeline intro
    - timeline entries (from home.Journey)
    - future intro
    - future focus cards
    """

    def get(self, request, *args, **kwargs):
        hero = (
            JourneyHero.objects
            .filter(is_active=True)
            .order_by("-updated_at", "-id")
            .first()
        )

        timeline_intro = (
            JourneySectionIntro.objects
            .filter(
                section_key="timeline",
                is_active=True,
            )
            .first()
        )

        future_intro = (
            JourneySectionIntro.objects
            .filter(
                section_key="future",
                is_active=True,
            )
            .first()
        )

        timeline = (
            Journey.objects
            .active()
            .optimized()
            .order_by("started_at", "display_order")
        )

        future_focus = (
            FutureFocus.objects
            .filter(is_active=True)
            .order_by("display_order", "id")
        )

        payload = {
            "hero": hero,
            "timeline_intro": timeline_intro,
            "timeline": timeline,
            "future_intro": future_intro,
            "future_focus": future_focus,
        }

        serializer = JourneyPageSerializer(payload)

        return Response(serializer.data)