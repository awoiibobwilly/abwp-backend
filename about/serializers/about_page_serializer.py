from rest_framework import serializers

from about.serializers.about_hero_serializer import AboutHeroSerializer
from about.serializers.who_i_am_serializer import WhoIAmSerializer
from about.serializers.professional_dna_serializer import ProfessionalDNASerializer
from about.serializers.core_values_serializer import CoreValuesSerializer
from about.serializers.selected_achievement_serializer import SelectedAchievementSerializer
from about.serializers.credential_serializer import CredentialSerializer
from about.serializers.skill_category_serializer import SkillCategorySerializer
from about.serializers.about_section_intro_serializer import AboutSectionIntroSerializer


class AboutPageSerializer(serializers.Serializer):
    hero = AboutHeroSerializer(allow_null=True)

    who_i_am_intro = AboutSectionIntroSerializer(allow_null=True)
    who_i_am = WhoIAmSerializer(many=True)

    professional_dna_intro = AboutSectionIntroSerializer(allow_null=True)
    professional_dna = ProfessionalDNASerializer(many=True)

    core_values_intro = AboutSectionIntroSerializer(allow_null=True)
    core_values = CoreValuesSerializer(allow_null=True)

    selected_achievements_intro = AboutSectionIntroSerializer(allow_null=True)
    selected_achievements = SelectedAchievementSerializer(many=True)

    credentials_intro = AboutSectionIntroSerializer(allow_null=True)
    skills_intro = AboutSectionIntroSerializer(allow_null=True)

    credentials = serializers.SerializerMethodField()
    skills = SkillCategorySerializer(many=True)

    def get_credentials(self, obj):
        education = obj.get("education_credentials", [])
        certification = obj.get("certification_credentials", [])

        return {
            "education": CredentialSerializer(education, many=True).data,
            "certifications": CredentialSerializer(certification, many=True).data,
        }