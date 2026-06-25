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

        ProjectListAPIView.as_view(),

        name="journey",

    ),

]
