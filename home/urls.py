from django.urls import path

from .views import StatisticListView


urlpatterns = [

    path(

        "statistics/",

        StatisticListView.as_view(),

        name="statistics"

    ),

]
