from rest_framework import generics

from about.models import ProfessionalDNA
from about.serializers import ProfessionalDNASerializer


class ProfessionalDNAListAPIView(generics.ListAPIView):
    serializer_class = ProfessionalDNASerializer

    def get_queryset(self):
        return ProfessionalDNA.objects.filter(
            is_active=True
        ).order_by("display_order", "id")