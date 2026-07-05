from django.urls import path

from about.views import (
    AboutPageAPIView,
    AboutHeroListAPIView,
    WhoIAmListAPIView,
    ProfessionalDNAListAPIView,
    CoreValuesDetailAPIView,
    SelectedAchievementListAPIView,
    CredentialListAPIView,
    SkillCategoryListAPIView,
)

urlpatterns = [
    path(
        "",
        AboutPageAPIView.as_view(),
        name="about-page",
    ),
    path(
        "hero/",
        AboutHeroListAPIView.as_view(),
        name="about-hero-list",
    ),
    path(
        "who-i-am/",
        WhoIAmListAPIView.as_view(),
        name="who-i-am-list",
    ),
    path(
        "professional-dna/",
        ProfessionalDNAListAPIView.as_view(),
        name="professional-dna-list",
    ),
    path(
        "core-values/",
        CoreValuesDetailAPIView.as_view(),
        name="core-values-detail",
    ),
    path(
        "achievements/",
        SelectedAchievementListAPIView.as_view(),
        name="selected-achievement-list",
    ),
    path(
        "credentials/",
        CredentialListAPIView.as_view(),
        name="credential-list",
    ),
    path(
        "skills/",
        SkillCategoryListAPIView.as_view(),
        name="skill-category-list",
    ),
]