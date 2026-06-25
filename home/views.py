from rest_framework import generics

from .models import (
    Expertise,
    Statistic,
    Highlight,
    Technology,
    ProjectCategory,
)

from .serializers import (
    StatisticSerializer,
    ExpertiseSerializer,
    HighlightSerializer,
    TechnologySerializer,
    ProjectCategorySerializer,
)


class StatisticListView(

    generics.ListAPIView

):

    serializer_class = StatisticSerializer

    def get_queryset(

        self

    ):

        return Statistic.objects.filter(

            is_active=True

        )


class ExpertiseListView(

    generics.ListAPIView

):

    serializer_class = ExpertiseSerializer

    queryset = Expertise.objects.filter(

        is_active=True

    ).order_by(

        "display_order"

    )


class HighlightListView(

    generics.ListAPIView

):

    serializer_class = HighlightSerializer

    queryset = Highlight.objects.filter(

        is_active=True

    ).order_by(

        "display_order"

    )

# ================================
    # TECHNOLOGY VIEWS
# ================================


class TechnologyListView(

    generics.ListAPIView

):

    serializer_class = TechnologySerializer

    queryset = Technology.objects.filter(

        is_active=True

    ).order_by(

        "display_order",

        "name",

    )

# ====================================
    # PROJECT CATEGORY
# ====================================


class ProjectCategoryListView(

    generics.ListAPIView

):

    serializer_class = ProjectCategorySerializer

    queryset = ProjectCategory.objects.filter(

        is_active=True

    ).order_by(

        "display_order",

        "name",

    )