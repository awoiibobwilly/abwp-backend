from django.urls import path

from ..views import (
    ResearchListAPIView,
    ResearchDetailAPIView,
    ResearchPageAPIView,
)

urlpatterns = [
    path(
        "page/",
        ResearchPageAPIView.as_view(),
        name="research-page",
    ),

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