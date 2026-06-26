from django.db import models
from django.db.models import Prefetch


# ==========================================================
# Base Portfolio QuerySet
# ==========================================================

class BasePortfolioQuerySet(models.QuerySet):
    """
    Base QuerySet shared across portfolio models.
    """

    def active(self):
        """
        Return active records.
        """

        if hasattr(self.model, "is_active"):

            return self.filter(
                is_active=True,
            )

        return self

    def featured(self):
        """
        Return featured records.
        """

        if hasattr(self.model, "featured"):

            return self.filter(
                featured=True,
            )

        return self

    def optimized(self):
        """
        Default optimization.

        Override in child QuerySets.
        """

        return self


# ==========================================================
# Technology
# ==========================================================

class TechnologyQuerySet(BasePortfolioQuerySet):

    def optimized(self):

        return self.order_by(

            "display_order",

            "name",

        )


# ==========================================================
# Project Category
# ==========================================================

class ProjectCategoryQuerySet(BasePortfolioQuerySet):

    def optimized(self):

        return self.order_by(

            "display_order",

            "name",

        )


# ==========================================================
# Journey
# ==========================================================

class JourneyQuerySet(BasePortfolioQuerySet):

    def optimized(self):

        return self.order_by(

            "-started_at",

            "display_order",

        )


# ==========================================================
# Project
# ==========================================================

class ProjectQuerySet(BasePortfolioQuerySet):

    def optimized(self):

        from .models import ProjectMedia

        return (

            self

            .select_related(

                "category",

            )

            .prefetch_related(

                "technologies",

                Prefetch(

                    "media",

                    queryset=ProjectMedia.objects.order_by(

                        "display_order",

                    ),

                ),

            )

        )


# ==========================================================
# Research
# ==========================================================

class ResearchQuerySet(BasePortfolioQuerySet):

    def optimized(self):

        return self


# ==========================================================
# Testimonial
# ==========================================================

class TestimonialQuerySet(BasePortfolioQuerySet):

    def optimized(self):

        return self


# ==========================================================
# Statistic
# ==========================================================

class StatisticQuerySet(BasePortfolioQuerySet):

    def optimized(self):

        return self.order_by(

            "display_order",

        )


# ==========================================================
# Highlight
# ==========================================================

class HighlightQuerySet(BasePortfolioQuerySet):

    def optimized(self):

        return self.order_by(

            "display_order",

        )


# ==========================================================
# Expertise
# ==========================================================

class ExpertiseQuerySet(BasePortfolioQuerySet):

    def optimized(self):

        return self.order_by(

            "display_order",

            "title",

        )