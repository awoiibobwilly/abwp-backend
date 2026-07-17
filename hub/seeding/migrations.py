"""
Knowledge Hub Fixture Migration Registry
========================================

Defines declarative migration rules for all Knowledge Hub
fixture models.

This module contains NO migration logic.

The normalization engine interprets these rules during
fixture normalization.

Supported migration operations
------------------------------

remove_fields
    Remove obsolete fields from legacy fixtures.

rename_fields
    Rename legacy fields.

merge_fields
    Merge multiple legacy fields into one.

choice_mappings
    Convert legacy display values into current model values.

defaults
    Insert default values for newly introduced fields.

Author
------
Awoii Bob Willy Portfolio
"""

from __future__ import annotations


# ==========================================================
# DEFAULT MODEL TEMPLATE
# ==========================================================

EMPTY_MODEL_RULES = {

    "remove_fields": set(),

    "rename_fields": {},

    "merge_fields": {},

    "choice_mappings": {},

    "defaults": {},

}


# ==========================================================
# ORGANIZATION TYPE CONVERSIONS
# ==========================================================

ORGANIZATION_TYPE_CHOICES = {

    "Healthcare Organization": "healthcare",

    "Healthcare": "healthcare",

    "Government Health Agency": "government",

    "Government Agency": "government",

    "Public Health Agency": "government",

    "Research Institution": "research",

    "Technology Company": "technology",

    "Technology": "technology",

    "Learning Platform": "learning",

    "Professional Body": "professional",

    "University": "university",

    "NGO": "ngo",

    "International Organization": "ngo",

    "Other": "other",

}


# ==========================================================
# LIBRARY RESOURCE TYPE CONVERSIONS
# ==========================================================

RESOURCE_TYPE_CHOICES = {

    "Book": "book",

    "Journal": "journal",

    "Article": "article",

    "Guide": "guide",

    "Manual": "manual",

    "White Paper": "whitepaper",

    "Case Study": "case-study",

    "Toolkit": "toolkit",

    "Documentation": "documentation",

    "Website": "website",

    "Course": "course",

    "Other": "other",

}


# ==========================================================
# VIDEO PLATFORM CONVERSIONS
# ==========================================================

VIDEO_PLATFORM_CHOICES = {

    "YouTube": "youtube",

    "Coursera": "coursera",

    "edX": "edx",

    "Udemy": "udemy",

    "LinkedIn Learning": "linkedin",

    "Vimeo": "vimeo",

    "Other": "other",

}


# ==========================================================
# MODEL MIGRATIONS
# ==========================================================

MODEL_MIGRATIONS = {

    # ======================================================
    # KNOWLEDGE HUB
    # ======================================================

    "hub.knowledgehub": {

        **EMPTY_MODEL_RULES,

    },

    # ======================================================
    # KNOWLEDGE THEME
    # ======================================================

    "hub.knowledgetheme": {

        **EMPTY_MODEL_RULES,

    },

    # ======================================================
    # KNOWLEDGE TAG
    # ======================================================

    "hub.knowledgetag": {

        **EMPTY_MODEL_RULES,

    },

    # ======================================================
    # ORGANIZATION
    # ======================================================

    "hub.organization": {

        #
        # Removed fields
        #

        "remove_fields": {

            "short_name",

            "primary_theme",

            "secondary_themes",

            "is_featured",

        },

        #
        # Renamed fields
        #

        "rename_fields": {

        },

        #
        # Merge fields
        #

        "merge_fields": {

            "themes": (

                "primary_theme",

                "secondary_themes",

            ),

        },

        #
        # Choice conversions
        #

        "choice_mappings": {

            "organization_type":

                ORGANIZATION_TYPE_CHOICES,

        },

        #
        # Default fields
        #

        "defaults": {

            "country": "",

            "tags": [],

        },

    },

    # ======================================================
    # LIBRARY RESOURCE
    # ======================================================

    "hub.libraryresource": {

        "remove_fields": set(),

        "rename_fields": {

        },

        "merge_fields": {

        },

        "choice_mappings": {

            "resource_type":

                RESOURCE_TYPE_CHOICES,

        },

        "defaults": {

            "tags": [],

        },

    },

    # ======================================================
    # LEARNING VIDEO
    # ======================================================

    "hub.learningvideo": {

        "remove_fields": set(),

        "rename_fields": {

        },

        "merge_fields": {

        },

        "choice_mappings": {

            "platform":

                VIDEO_PLATFORM_CHOICES,

        },

        "defaults": {

            "tags": [],

        },

    },

    # ======================================================
    # PRACTICAL RESOURCE
    # ======================================================

    "hub.practicalresource": {

        **EMPTY_MODEL_RULES,

    },

    # ======================================================
    # RESEARCH CONTRIBUTION
    # ======================================================

    "hub.researchcontribution": {

        **EMPTY_MODEL_RULES,

    },

    # ======================================================
    # SEARCH CONFIGURATION
    # ======================================================

    "hub.searchconfiguration": {

        **EMPTY_MODEL_RULES,

    },

}


# ==========================================================
# VALID OPERATIONS
# ==========================================================

VALID_RULES = {

    "remove_fields",

    "rename_fields",

    "merge_fields",

    "choice_mappings",

    "defaults",

}


# ==========================================================
# HELPERS
# ==========================================================

def get_model_rules(model: str) -> dict:
    """
    Return migration rules for a model.

    Unknown models return an empty rule set.
    """

    return MODEL_MIGRATIONS.get(

        model,

        EMPTY_MODEL_RULES,

    )


def has_migrations(model: str) -> bool:
    """
    Determine whether a model defines
    any migration rules.
    """

    rules = get_model_rules(model)

    return any(

        bool(value)

        for value in rules.values()

    )


def registered_models() -> list[str]:
    """
    Return all registered migration models.
    """

    return sorted(

        MODEL_MIGRATIONS.keys()

    )


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "EMPTY_MODEL_RULES",

    "MODEL_MIGRATIONS",

    "VALID_RULES",

    "get_model_rules",

    "has_migrations",

    "registered_models",

]