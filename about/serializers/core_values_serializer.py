from rest_framework import serializers

from about.models import CoreValues


class CoreValuesSerializer(serializers.ModelSerializer):
    mission = serializers.SerializerMethodField()
    vision = serializers.SerializerMethodField()

    class Meta:
        model = CoreValues
        fields = [
            "id",
            "section_title",
            "section_description",
            "mission",
            "vision",
            "values",
            "is_active",
            "updated_at",
        ]

    def get_mission(self, obj):
        return {
            "title": obj.mission_title,
            "description": obj.mission_description,
        }

    def get_vision(self, obj):
        return {
            "title": obj.vision_title,
            "description": obj.vision_description,
        }