from rest_framework import generics

from insights.models import Insight
from insights.serializers import InsightSerializer


# ==========================================================
# INSIGHT PREVIEW VIEW
# RETURNS A SINGLE INSIGHT PAGE BY ID
# INCLUDING INACTIVE / DRAFT CONFIGS
# ==========================================================

class InsightPreviewAPIView(generics.RetrieveAPIView):
    queryset = (
        Insight.objects.all()
        .prefetch_related(
            "section_intros",
            "categories",
            "featured_articles",
            "thoughts",
            "quotes",
        )
        .select_related("hero", "newsletter")
    )
    serializer_class = InsightSerializer
    lookup_field = "pk"