from rest_framework import generics

from about.models import SkillCategory
from about.serializers import SkillCategorySerializer


class SkillCategoryListAPIView(generics.ListAPIView):
    serializer_class = SkillCategorySerializer

    def get_queryset(self):
        return SkillCategory.objects.filter(
            is_active=True
        ).order_by("display_order", "id")