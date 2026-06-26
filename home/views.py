from .api.mixins import (
    FeaturedQuerysetMixin,
    # ActiveQuerysetMixin,
    OrderedQuerysetMixin,
    # PortfolioFilterMixin,
    # PortfolioOrderingMixin,
)

from .api.base import (
    PublicListAPIView,
    # PublicRetrieveAPIView,
)


from rest_framework import generics
from django.db.models import Prefetch
# from .pagination import ProjectPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import (

    OrderingFilter,

    SearchFilter,

)


from .filters import ProjectFilter

from .models import (
    Expertise,
    Statistic,
    Highlight,
    Technology,
    ProjectCategory,
    Project,
    ProjectMedia,
    Journey,
)

from .serializers import (

    StatisticSerializer,
    ExpertiseSerializer,
    HighlightSerializer,
    TechnologySerializer,
    ProjectCategorySerializer,
    FeaturedProjectSerializer,
    ProjectSerializer,
    JourneySerializer,

)

# pagination_class = ProjectPagination


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

# ================================
    #FEATURED PROJECT
# ================================


class FeaturedProjectListAPIView(

    FeaturedQuerysetMixin,

    OrderedQuerysetMixin,

    PublicListAPIView,

):

    serializer_class = FeaturedProjectSerializer

    queryset = Project.objects.select_related(
        "category",
    ).prefetch_related(
        "technologies",
        "media",
    )
    
#=============================================
    #PROJECT DETAIL
#=============================================


class ProjectDetailAPIView(

    generics.RetrieveAPIView

):

    serializer_class = ProjectSerializer

    lookup_field = "slug"

    def get_queryset(self):

        return (

            Project.objects

            .filter(

                is_active=True,

            )

            .select_related(

                "category",

            )

            .prefetch_related(

                "technologies",

                Prefetch(

                    "media",

                    queryset=ProjectMedia.objects.order_by(

                        "display_order",

                    ),

                ),

            )

        )


class ProjectListAPIView(generics.ListAPIView):

    serializer_class = ProjectSerializer

    # pagination_class = ProjectPagination

    # throttle_scope = "projects"

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = ProjectFilter

    search_fields = (
        "title",
        "short_description",
        "description",
        "client",
        "organization",
    )

    ordering_fields = (
        "created_at",
        "completed_at",
        "title",
        "display_order",
    )

    ordering = (
        "display_order",
    )

    def get_queryset(self):

        return (
            Project.objects
            .filter(
                is_active=True,
            )
            .select_related(
                "category",
            )
            .prefetch_related(
                "technologies",
                Prefetch(
                    "media",
                    queryset=ProjectMedia.objects.order_by(
                        "display_order",
                    ),
                ),
            )
            .distinct()
        )

# =================================
    # JOURNEY
# =================================


class JourneyListAPIView(generics.ListAPIView):

    serializer_class = JourneySerializer

    throttle_scope = "home"

    def get_queryset(self):

        return Journey.objects.filter(
            is_active=True,
        )