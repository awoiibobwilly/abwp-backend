from django.contrib import admin
from django.urls import include, path

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

]