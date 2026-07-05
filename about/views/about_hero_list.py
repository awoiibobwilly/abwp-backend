from rest_framework import generics

from about.models import AboutHero
from about.serializers import AboutHeroSerializer


class AboutHeroListAPIView(generics.ListAPIView):
    serializer_class = AboutHeroSerializer

    def get_queryset(self):
        return AboutHero.objects.filter(
            is_active=True
        ).order_by("-updated_at")