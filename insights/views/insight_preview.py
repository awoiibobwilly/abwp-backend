from rest_framework import generics

from insights.models import Insight
from insights.serializers import InsightSerializer


# ==========================================================
# INSIGHT PREVIEW VIEW
# RETURNS A SINGLE INSIGHT PAGE BY ID
# INCLUDING DRAFTS
# ==========================================================

class InsightPreviewAPIView(generics.RetrieveAPIView):

    queryset = (

        Insight.objects

        .select_related(
            "hero",
            "newsletter",
        )

        .prefetch_related(

            "hero__stats",

            "section_intros",

            "categories",

            "featured_articles",

            "thoughts",

            "quotes",

        )

    )

    serializer_class = InsightSerializer

    lookup_field = "pk"