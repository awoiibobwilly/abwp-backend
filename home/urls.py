from django.urls import path

from .views import (

    StatisticListView,

    ExpertiseListView,

    HighlightListView,

    TechnologyListView,

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


]
