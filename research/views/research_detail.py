from rest_framework import generics

from ..models import Research
from ..serializers import ResearchSerializer


class ResearchDetailAPIView(generics.RetrieveAPIView):

    serializer_class = ResearchSerializer

    lookup_field = "slug"

    queryset = (

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

    )