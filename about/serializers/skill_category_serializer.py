from rest_framework import serializers

from about.models import SkillCategory


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = [
            "id",
            "title",
            "skills",
            "display_order",
            "is_active",
        ]