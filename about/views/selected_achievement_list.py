from rest_framework import generics

from about.models import SelectedAchievement
from about.serializers import SelectedAchievementSerializer


class SelectedAchievementListAPIView(generics.ListAPIView):
    serializer_class = SelectedAchievementSerializer

    def get_queryset(self):
        return SelectedAchievement.objects.filter(
            is_active=True
        ).order_by("display_order", "id")