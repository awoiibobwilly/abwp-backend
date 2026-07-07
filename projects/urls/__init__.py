from django.urls import path

from projects.views import ProjectsPageView


app_name = "projects"

urlpatterns = [
    path(
        "",
        ProjectsPageView.as_view(),
        name="projects-page",
    ),
]