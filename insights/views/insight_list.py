from rest_framework import generics

from insights.models import Insight
from insights.serializers import InsightSerializer


# ==========================================================
# INSIGHT LIST VIEW
# RETURNS ALL INSIGHT PAGE CONFIGURATIONS
# ==========================================================

class InsightListAPIView(generics.ListAPIView):

    queryset = (
        Insight.objects.all()
        .order_by("title")
    )

    serializer_class = InsightSerializer