from rest_framework import generics

from about.models import WhoIAm
from about.serializers import WhoIAmSerializer


class WhoIAmListAPIView(generics.ListAPIView):
    serializer_class = WhoIAmSerializer

    def get_queryset(self):
        return WhoIAm.objects.filter(
            is_active=True
        ).order_by("display_order", "id")