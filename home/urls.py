from django.urls import path

from .views import StatisticListView

from .views import ExpertiseListView

from .views import HighlightListView


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


]
