from django.urls import path

from ..views import ResearchPreviewAPIView

urlpatterns = [

    path(

        "research/",

        ResearchPreviewAPIView.as_view(),

        name="home-research",

    ),

]