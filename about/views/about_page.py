from rest_framework.response import Response
from rest_framework.views import APIView

from about.models import (
    AboutHero,
    AboutSectionIntro,
    WhoIAm,
    ProfessionalDNA,
    CoreValues,
    SelectedAchievement,
    Credential,
    SkillCategory,
)
from about.serializers import AboutPageSerializer


class AboutPageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        hero = (
            AboutHero.objects.filter(
                is_active=True
            )
            .order_by("-updated_at")
            .first()
        )

        who_i_am_intro = AboutSectionIntro.objects.filter(
            section_key=AboutSectionIntro.WHO_I_AM,
            is_active=True,
        ).first()

        professional_dna_intro = AboutSectionIntro.objects.filter(
            section_key=AboutSectionIntro.PROFESSIONAL_DNA,
            is_active=True,
        ).first()

        core_values_intro = AboutSectionIntro.objects.filter(
            section_key=AboutSectionIntro.CORE_VALUES,
            is_active=True,
        ).first()

        selected_achievements_intro = AboutSectionIntro.objects.filter(
            section_key=AboutSectionIntro.SELECTED_ACHIEVEMENTS,
            is_active=True,
        ).first()

        credentials_intro = AboutSectionIntro.objects.filter(
            section_key=AboutSectionIntro.CREDENTIALS,
            is_active=True,
        ).first()

        skills_intro = AboutSectionIntro.objects.filter(
            section_key=AboutSectionIntro.SKILLS,
            is_active=True,
        ).first()

        who_i_am = WhoIAm.objects.filter(
            is_active=True
        ).order_by("display_order", "id")

        professional_dna = ProfessionalDNA.objects.filter(
            is_active=True
        ).order_by("display_order", "id")

        core_values = (
            CoreValues.objects.filter(
                is_active=True
            )
            .order_by("-updated_at")
            .first()
        )

        selected_achievements = SelectedAchievement.objects.filter(
            is_active=True
        ).order_by("display_order", "id")

        education_credentials = Credential.objects.filter(
            is_active=True,
            group=Credential.EDUCATION,
        ).order_by("display_order", "id")

        certification_credentials = Credential.objects.filter(
            is_active=True,
            group=Credential.CERTIFICATION,
        ).order_by("display_order", "id")

        skills = SkillCategory.objects.filter(
            is_active=True
        ).order_by("display_order", "id")

        payload = {
            "hero": hero,

            "who_i_am_intro": who_i_am_intro,
            "who_i_am": who_i_am,

            "professional_dna_intro": professional_dna_intro,
            "professional_dna": professional_dna,

            "core_values_intro": core_values_intro,
            "core_values": core_values,

            "selected_achievements_intro": selected_achievements_intro,
            "selected_achievements": selected_achievements,

            "credentials_intro": credentials_intro,
            "education_credentials": education_credentials,
            "certification_credentials": certification_credentials,

            "skills_intro": skills_intro,
            "skills": skills,
        }

        serializer = AboutPageSerializer(payload)

        return Response(serializer.data)