from rest_framework import serializers

from about.models import SelectedAchievement


class SelectedAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedAchievement
        fields = [
            "id",
            "title",
            "description",
            "category",
            "year",
            "display_order",
            "is_active",
        ]