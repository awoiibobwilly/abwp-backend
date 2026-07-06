from django.urls import path

from journey.views import JourneyPageAPIView


urlpatterns = [
    path(
        "",
        JourneyPageAPIView.as_view(),
        name="journey-page",
    ),
]