from rest_framework import generics

from ..models import Research
from ..serializers import ResearchSerializer


class ResearchListAPIView(generics.ListAPIView):

    serializer_class = ResearchSerializer

    def get_queryset(self):

        return (

            Research.objects

            .filter(

                published=True,

            )

            .select_related(

                "category",

            )

            .prefetch_related(

                "keywords",

            )

            .order_by(

                "display_order",

                "-year",

            )

        )