from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)

from .api.base import (
    PublicListAPIView,
    PublicRetrieveAPIView,
)

# Future Architecture
# from .api.mixins import (
#     FeaturedQuerysetMixin,
#     ActiveQuerysetMixin,
#     OrderedQuerysetMixin,
#     PortfolioFilterMixin,
#     PortfolioOrderingMixin,
# )

from .filters import ProjectFilter

from .models import (
    Expertise,
    Statistic,
    Highlight,
    Technology,
    ProjectCategory,
    Project,
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

# ==========================================================
# Future Pagination
# ==========================================================

# from .pagination import ProjectPagination


# ==========================================================
# STATISTICS
# ==========================================================

class StatisticListView(PublicListAPIView):

    serializer_class = StatisticSerializer

    queryset = (
        Statistic.objects
        .active()
        .optimized()
    )


# ==========================================================
# EXPERTISE
# ==========================================================

class ExpertiseListView(PublicListAPIView):

    serializer_class = ExpertiseSerializer

    queryset = (
        Expertise.objects
        .active()
        .optimized()
    )


# ==========================================================
# HIGHLIGHTS
# ==========================================================

class HighlightListView(PublicListAPIView):

    serializer_class = HighlightSerializer

    queryset = (
        Highlight.objects
        .active()
        .optimized()
    )


# ==========================================================
# TECHNOLOGIES
# ==========================================================

class TechnologyListView(PublicListAPIView):

    serializer_class = TechnologySerializer

    queryset = (
        Technology.objects
        .active()
        .optimized()
    )


# ==========================================================
# PROJECT CATEGORIES
# ==========================================================

class ProjectCategoryListView(PublicListAPIView):

    serializer_class = ProjectCategorySerializer

    queryset = (
        ProjectCategory.objects
        .active()
        .optimized()
    )


# ==========================================================
# FEATURED PROJECTS
# ==========================================================

class FeaturedProjectListAPIView(PublicListAPIView):

    serializer_class = FeaturedProjectSerializer

    queryset = (
        Project.objects
        .active()
        .featured()
        .optimized()
    )


# ==========================================================
# PROJECT DETAIL
# ==========================================================

class ProjectDetailAPIView(PublicRetrieveAPIView):

    serializer_class = ProjectSerializer

    queryset = (
        Project.objects
        .active()
        .optimized()
    )


# ==========================================================
# PROJECTS
# ==========================================================

class ProjectListAPIView(PublicListAPIView):

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

    queryset = (
        Project.objects
        .active()
        .optimized()
        .distinct()
    )


# ==========================================================
# JOURNEY
# ==========================================================

class JourneyListAPIView(PublicListAPIView):

    serializer_class = JourneySerializer

    # throttle_scope = "home"

    queryset = (
        Journey.objects
        .active()
        .optimized()
    )


# ==========================================================
# FEATURED JOURNEY
# ==========================================================

class FeaturedJourneyListAPIView(PublicListAPIView):

    serializer_class = JourneySerializer

    queryset = (
        Journey.objects
        .active()
        .featured()
        .optimized()
    )


# ==========================================================
# JOURNEY DETAIL
# ==========================================================

class JourneyDetailAPIView(PublicRetrieveAPIView):

    serializer_class = JourneySerializer

    queryset = (
        Journey.objects
        .active()
        .optimized()
    )