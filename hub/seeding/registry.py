"""
Knowledge Hub Verification Registry
===================================

Central registry describing every model managed by the
Knowledge Hub seeding infrastructure.

The registry is consumed by:

• seed_hub.py
• verification pipeline
• automated tests

This module intentionally contains no business logic.

Author
------
Awoii Bob Willy Portfolio
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from hub.models import (
    KnowledgeHub,
    KnowledgeTheme,
    KnowledgeTag,
    Organization,
    LibraryResource,
    LearningVideo,
    PracticalResource,
    ResearchContribution,
    SearchConfiguration,
)

# ==========================================================
# REGISTRY ENTRY
# ==========================================================

@dataclass(frozen=True, slots=True)
class RegistryEntry:
    """
    Describes one model participating in the
    Knowledge Hub seeding pipeline.
    """

    #
    # Human-readable label.
    #

    label: str

    #
    # Django model.
    #

    model: Type

    #
    # Expected minimum records.
    #
    # Used by verification.
    #

    minimum_records: int = 1

    #
    # Whether this model should always exist.
    #

    required: bool = True


# ==========================================================
# MODEL REGISTRY
# ==========================================================

MODEL_REGISTRY = [

    RegistryEntry(

        label="Knowledge Hub",

        model=KnowledgeHub,

        minimum_records=1,

    ),

    RegistryEntry(

        label="Knowledge Themes",

        model=KnowledgeTheme,

        minimum_records=12,

    ),

    RegistryEntry(

        label="Knowledge Tags",

        model=KnowledgeTag,

        minimum_records=120,

    ),

    RegistryEntry(

        label="Organizations",

        model=Organization,

        minimum_records=24,

    ),

    RegistryEntry(

        label="Library Resources",

        model=LibraryResource,

        minimum_records=32,

    ),

    RegistryEntry(

        label="Learning Videos",

        model=LearningVideo,

        minimum_records=32,

    ),

    RegistryEntry(

        label="Practical Resources",

        model=PracticalResource,

        minimum_records=32,

    ),

    RegistryEntry(

        label="Research Contributions",

        model=ResearchContribution,

        minimum_records=32,

    ),

    RegistryEntry(

        label="Search Configuration",

        model=SearchConfiguration,

        minimum_records=1,

    ),

]

# ==========================================================
# HELPERS
# ==========================================================

def get_registry() -> list[RegistryEntry]:
    """
    Return the complete registry.
    """

    return MODEL_REGISTRY.copy()


def required_models() -> list[RegistryEntry]:
    """
    Return required models only.
    """

    return [

        entry

        for entry in MODEL_REGISTRY

        if entry.required

    ]


def registry_size() -> int:
    """
    Number of registered models.
    """

    return len(MODEL_REGISTRY)


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "RegistryEntry",

    "MODEL_REGISTRY",

    "get_registry",

    "required_models",

    "registry_size",

]