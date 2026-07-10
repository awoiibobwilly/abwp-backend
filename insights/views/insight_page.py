from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from insights.models import Insight
from insights.serializers import InsightSerializer


# ==========================================================
# INSIGHT PAGE VIEW
# RETURNS THE ACTIVE INSIGHTS PAGE PAYLOAD
# ==========================================================

class InsightPageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        insight = (
            Insight.objects.filter(is_active=True)
            .prefetch_related(
                "section_intros",
                "categories",
                "featured_articles",
                "thoughts",
                "quotes",
            )
            .select_related("hero", "newsletter")
            .first()
        )

        if not insight:
            return Response(
                {
                    "detail": "No active Insights page found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = InsightSerializer(
            insight,
            context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)