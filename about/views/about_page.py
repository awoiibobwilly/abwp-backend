from rest_framework.response import Response
from rest_framework.views import APIView

from about.models import (
    AboutHero,
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
            "who_i_am": who_i_am,
            "professional_dna": professional_dna,
            "core_values": core_values,
            "selected_achievements": selected_achievements,
            "education_credentials": education_credentials,
            "certification_credentials": certification_credentials,
            "skills": skills,
        }

        serializer = AboutPageSerializer(payload)

        return Response(serializer.data)