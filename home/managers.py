from django.db import models

from .querysets import (
    ProjectQuerySet,
    JourneyQuerySet,
    ResearchQuerySet,
    TestimonialQuerySet,
    ExpertiseQuerySet,
    ExpertiseQuerySet,
    HighlightQuerySet,
    JourneyQuerySet,
    ProjectCategoryQuerySet,
    ProjectQuerySet,
    ResearchQuerySet,
    StatisticQuerySet,
    TechnologyQuerySet,
    TestimonialQuerySet,
)


# ==========================================================
# Project Manager
# ==========================================================

class ProjectManager(
    models.Manager.from_queryset(ProjectQuerySet)
):
    """
    Manager for Project.
    """
    pass


# ==========================================================
# Project Category Manager
# ==========================================================

class ProjectCategoryManager(
    models.Manager.from_queryset(ProjectCategoryQuerySet)
):
    """
    Manager for ProjectCategory.
    """
    pass


# ==========================================================
# Technology Manager
# ==========================================================

class TechnologyManager(
    models.Manager.from_queryset(TechnologyQuerySet)
):
    """
    Manager for Technology.
    """
    pass


# ==========================================================
# Journey Manager
# ==========================================================

class JourneyManager(
    models.Manager.from_queryset(JourneyQuerySet)
):
    """
    Manager for Journey.
    """
    pass


# ==========================================================
# Research Manager
# ==========================================================

class ResearchManager(
    models.Manager.from_queryset(ResearchQuerySet)
):
    """
    Manager for Research.
    """
    pass


# ==========================================================
# Testimonial Manager
# ==========================================================

class TestimonialManager(
    models.Manager.from_queryset(TestimonialQuerySet)
):
    """
    Manager for Testimonial.
    """
    pass


# ==========================================================
# Highlight Manager
# ==========================================================

class HighlightManager(
    models.Manager.from_queryset(HighlightQuerySet)
):
    """
    Manager for Highlight.
    """
    pass


# ==========================================================
# Expertise Manager
# ==========================================================

class ExpertiseManager(
    models.Manager.from_queryset(ExpertiseQuerySet)
):
    """
    Manager for Expertise.
    """
    pass


# ==========================================================
# Statistic Manager
# ==========================================================

class StatisticManager(
    models.Manager.from_queryset(StatisticQuerySet)
):
    """
    Manager for Statistic.
    """
    pass