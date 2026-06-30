from django.urls import path

from .views import (

    StatisticListView,

    ExpertiseListView,

    HighlightListView,

    TechnologyListView,

    ProjectCategoryListView,

    ProjectDetailAPIView,

    ProjectListAPIView,

    FeaturedProjectListAPIView,

    JourneyListAPIView,

    FeaturedTestimonialListAPIView,

    TestimonialListView,

)


urlpatterns = [

    path(

        "statistics/",

        StatisticListView.as_view(),

        name="statistics"

    ),

    path(

        "expertise/",

        ExpertiseListView.as_view(),

        name="expertise-list",

    ),

    path(

        "highlights/",

        HighlightListView.as_view(),

        name="highlight-list",

    ),

    path(

        "technologies/",

        TechnologyListView.as_view(),

        name="technology-list",

    ),

    path(

        "project-categories/",

        ProjectCategoryListView.as_view(),

        name="project-category-list",

    ),

    path(

        "projects/<slug:slug>/",

        ProjectDetailAPIView.as_view(),

        name="project-detail",

    ),

    path(

        "projects/",

        ProjectListAPIView.as_view(),

        name="project-list",

    ),

    path('featured-projects/', FeaturedProjectListAPIView.as_view(), name='featured-project-list'),

    path(

        "journey/",

        JourneyListAPIView.as_view(),

        name="journey",

    ),

]


from django.urls import path

from .views import (
    # Projects
    FeaturedProjectListAPIView,
    ProjectListAPIView,
    ProjectDetailAPIView,
    ProjectCategoryListView,

    # Journey
    # FeaturedJourneyAPIView, To be uncommented later
    JourneyListAPIView,
    # JourneyDetailAPIView, To be uncommented

    # Existing Home APIs
    StatisticListView,
    ExpertiseListView,
    HighlightListView,
    TechnologyListView,
)

urlpatterns = [

    # ==========================================================
    # Projects
    # ==========================================================

    path(
        "featured-projects/",
        FeaturedProjectListAPIView.as_view(),
        name="featured-projects",
    ),

    path(
        "projects/",
        ProjectListAPIView.as_view(),
        name="projects",
    ),

    path(
        "projects/<slug:slug>/",
        ProjectDetailAPIView.as_view(),
        name="project-detail",
    ),

    path(
        "project-categories/",
        ProjectCategoryListView.as_view(),
        name="project-category-list",

    ),

    # ----------------------------------------------------------
    # Legacy (temporary compatibility)
    # Remove after frontend migration
    # ----------------------------------------------------------

    path(
        "project/",
        ProjectListAPIView.as_view(),
        name="project-list-legacy",
    ),

    path(
        "project/<slug:slug>/",
        ProjectDetailAPIView.as_view(),
        name="project-detail-legacy",
    ),

    # ==========================================================
    # Journey
    # ==========================================================

    # path(
    #     "featured-journey/",
    #     FeaturedJourneyAPIView.as_view(),
    #     name="featured-journey",
    # ),

    path(
        "journey/",
        JourneyListAPIView.as_view(),
        name="journey",
    ),

    # path(
    #     "journey/<slug:slug>/",
    #     JourneyDetailAPIView.as_view(),
    #     name="journey-detail",
    # ),

    # ==========================================================
    # Homepage Content
    # ==========================================================

    path(
        "statistics/",
        StatisticListView.as_view(),
        name="statistics",
    ),

    path(
        "expertise/",
        ExpertiseListView.as_view(),
        name="expertise",
    ),

    path(
        "highlights/",
        HighlightListView.as_view(),
        name="highlights",
    ),

    path(

        "technologies/",
        TechnologyListView.as_view(),
        name="technology-list",

    ),

    # ==========================================================
# FEATURED TESTIMONIALS
# ==========================================================

    path(

        "home/testimonials/",

        FeaturedTestimonialListAPIView.as_view(),

        name="featured-testimonials",

    ),

    # ==========================================================
    # TESTIMONIALS
    # ==========================================================

    path(

        "testimonials/",

        TestimonialListView.as_view(),

        name="testimonials",

    ),

]
