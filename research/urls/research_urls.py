from django.urls import path

from ..views import (
    ResearchListAPIView,
    ResearchDetailAPIView,
)

urlpatterns = [

    path(

        "",

        ResearchListAPIView.as_view(),

        name="research-list",

    ),

    path(

        "<slug:slug>/",

        ResearchDetailAPIView.as_view(),

        name="research-detail",

    ),

]
