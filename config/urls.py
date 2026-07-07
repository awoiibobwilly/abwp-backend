from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "api/",
        include("contact.urls"),
    ),

    path(
        "api/home/",
        include("home.urls"),
    ),

    # ==========================================
    # Research APIs
    # ==========================================

    path(
        "api/home/",
        include("research.urls.home_urls"),
    ),

    path(
        "api/research/",
        include("research.urls.research_urls"),
    ),

    path("api/about/", include("about.urls.about_urls")),


    path("api/journey/", include("journey.urls.journey_urls")),

    path("api/projects/", include("projects.urls")),

]


# ==========================================================
# Media Files (Development)
# ==========================================================

if settings.DEBUG:

    urlpatterns += static(

        settings.MEDIA_URL,

        document_root=settings.MEDIA_ROOT,

    )