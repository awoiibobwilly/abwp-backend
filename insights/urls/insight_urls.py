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
        "insights/",
        InsightListAPIView.as_view(),
        name="insight-list",
    ),
    path(
        "insights/<slug:slug>/",
        InsightDetailAPIView.as_view(),
        name="insight-detail",
    ),
    path(
        "insights/preview/<int:pk>/",
        InsightPreviewAPIView.as_view(),
        name="insight-preview",
    ),
]