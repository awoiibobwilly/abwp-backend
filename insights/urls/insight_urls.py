from django.urls import path

from insights.views import (
    InsightPageAPIView,
    InsightListAPIView,
    InsightDetailAPIView,
    InsightPreviewAPIView,
)

app_name = "insights"

urlpatterns = [
    path(
        "insights-page/",
        InsightPageAPIView.as_view(),
        name="insight-page",
    ),
    path(
        "",
        InsightListAPIView.as_view(),
        name="insight-list",
    ),
    path(
        "preview/<int:pk>/",
        InsightPreviewAPIView.as_view(),
        name="insight-preview",
    ),
    path(
        "<slug:slug>/",
        InsightDetailAPIView.as_view(),
        name="insight-detail",
    ),
]