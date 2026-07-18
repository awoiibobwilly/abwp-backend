from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from django.db.models import Model

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

@dataclass(frozen=True)
class RegistryEntry:

    label: str

    model: Type[Model]

    minimum_records: int

    unique_fields: tuple[str, ...] = ()

    required_fields: tuple[str, ...] = ()

    relationship_fields: tuple[
        tuple[str, str, bool],
        ...
    ] = ()


# ==========================================================
# MODEL REGISTRY
# ==========================================================

MODEL_REGISTRY = [

    RegistryEntry(
        label="Knowledge Hub",
        model=KnowledgeHub,
        minimum_records=1,
        required_fields=(
            "title",
            "description",
        ),
    ),

    RegistryEntry(
        label="Knowledge Themes",
        model=KnowledgeTheme,
        minimum_records=12,
        unique_fields=(
            "slug",
            "title",
        ),
        required_fields=(
            "title",
        ),
    ),

    RegistryEntry(
        label="Knowledge Tags",
        model=KnowledgeTag,
        minimum_records=120,
        unique_fields=(
            "slug",
            "name",
        ),
        required_fields=(
            "name",
        ),
    ),

    RegistryEntry(
        label="Organizations",
        model=Organization,
        minimum_records=24,
        unique_fields=(
            "slug",
            "name",
        ),
        required_fields=(
            "name",
        ),
        relationship_fields=(
            ("themes", "hub.knowledgetheme", True),
            ("tags", "hub.knowledgetag", True),
        ),
    ),

    RegistryEntry(
        label="Library Resources",
        model=LibraryResource,
        minimum_records=32,
        unique_fields=(
            "slug",
            "title",
        ),
        required_fields=(
            "title",
            "summary",
        ),
        relationship_fields=(
            ("themes", "hub.knowledgetheme", True),
            ("tags", "hub.knowledgetag", True),
        ),
    ),

    RegistryEntry(
        label="Learning Videos",
        model=LearningVideo,
        minimum_records=32,
        unique_fields=(
            "slug",
            "title",
        ),
        required_fields=(
            "title",
            "summary",
            "video_url",
        ),
        relationship_fields=(
            ("themes", "hub.knowledgetheme", True),
            ("tags", "hub.knowledgetag", True),
        ),
    ),

    RegistryEntry(
        label="Practical Resources",
        model=PracticalResource,
        minimum_records=32,
        unique_fields=(
            "slug",
            "title",
        ),
        required_fields=(
            "title",
            "summary",
        ),
        relationship_fields=(
            ("themes", "hub.knowledgetheme", True),
            ("tags", "hub.knowledgetag", True),
        ),
    ),

    RegistryEntry(
        label="Research Contributions",
        model=ResearchContribution,
        minimum_records=32,
        unique_fields=(
            "slug",
            "title",
        ),
        required_fields=(
            "title",
            "summary",
        ),
        relationship_fields=(
            ("themes", "hub.knowledgetheme", True),
            ("tags", "hub.knowledgetag", True),
        ),
    ),

    RegistryEntry(
        label="Search Configuration",
        model=SearchConfiguration,
        minimum_records=1,
        required_fields=(
            "knowledge_hub",
            "placeholder",
            "heading",
        ),
        relationship_fields=(
            ("knowledge_hub", "hub.knowledgehub", False),
        ),
    ),

]

# ==========================================================
# REGISTRY LOOKUP
# ==========================================================

MODEL_LOOKUP = {
    entry.model._meta.label_lower: entry
    for entry in MODEL_REGISTRY
}