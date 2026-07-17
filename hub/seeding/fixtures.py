"""
Knowledge Hub Fixture Registry
==============================

Central registry of all fixture files used by the
Knowledge Hub seeding infrastructure.

This module defines:

• Fixture root directory
• Fixture loading order
• Fixture groupings
• Unified fixture registry

No business logic should exist here.

The seeding engine, normalization engine, and validation
pipeline consume this registry.

Author:
    Awoii Bob Willy Portfolio
"""

from __future__ import annotations

from pathlib import Path


# ==========================================================
# ROOT DIRECTORY
# ==========================================================

FIXTURE_ROOT = Path("hub") / "fixtures"


# ==========================================================
# CORE FIXTURES
# ==========================================================

CORE_FIXTURES = [

    FIXTURE_ROOT / "knowledge_hub.json",

    FIXTURE_ROOT / "knowledge_themes.json",

]


# ==========================================================
# KNOWLEDGE TAGS
# ==========================================================

TAG_FIXTURES = [

    FIXTURE_ROOT / "knowledge_tags" / "healthcare_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "public_health_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "digital_health_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "research_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "software_engineering_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "data_science_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "artificial_intelligence_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "leadership_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "monitoring_evaluation_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "innovation_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "education_tags.json",

    FIXTURE_ROOT / "knowledge_tags" / "professional_development_tags.json",

]


# ==========================================================
# ORGANIZATIONS
# ==========================================================

ORGANIZATION_FIXTURES = [

    FIXTURE_ROOT / "organizations" / "healthcare_organizations.json",

    FIXTURE_ROOT / "organizations" / "academic_organizations.json",

    FIXTURE_ROOT / "organizations" / "technology_organizations.json",

    FIXTURE_ROOT / "organizations" / "learning_platforms.json",

    FIXTURE_ROOT / "organizations" / "professional_bodies.json",

    FIXTURE_ROOT / "organizations" / "innovation_organizations.json",

]


# ==========================================================
# LIBRARY RESOURCES
# ==========================================================

LIBRARY_RESOURCE_FIXTURES = [

    FIXTURE_ROOT / "library_resources" / "healthcare_resources.json",

    FIXTURE_ROOT / "library_resources" / "research_resources.json",

    FIXTURE_ROOT / "library_resources" / "software_engineering_resources.json",

    FIXTURE_ROOT / "library_resources" / "data_science_resources.json",

    FIXTURE_ROOT / "library_resources" / "artificial_intelligence_resources.json",

    FIXTURE_ROOT / "library_resources" / "leadership_resources.json",

    FIXTURE_ROOT / "library_resources" / "innovation_resources.json",

    FIXTURE_ROOT / "library_resources" / "learning_resources.json",

]


# ==========================================================
# LEARNING VIDEOS
# ==========================================================

LEARNING_VIDEO_FIXTURES = [

    FIXTURE_ROOT / "learning_videos" / "healthcare_videos.json",

    FIXTURE_ROOT / "learning_videos" / "research_videos.json",

    FIXTURE_ROOT / "learning_videos" / "software_engineering_videos.json",

    FIXTURE_ROOT / "learning_videos" / "data_science_videos.json",

    FIXTURE_ROOT / "learning_videos" / "artificial_intelligence_videos.json",

    FIXTURE_ROOT / "learning_videos" / "leadership_videos.json",

    FIXTURE_ROOT / "learning_videos" / "innovation_videos.json",

    FIXTURE_ROOT / "learning_videos" / "learning_videos.json",

]


# ==========================================================
# PRACTICAL RESOURCES
# ==========================================================

PRACTICAL_RESOURCE_FIXTURES = [

    FIXTURE_ROOT / "practical_resources" / "healthcare_toolkits.json",

    FIXTURE_ROOT / "practical_resources" / "research_toolkits.json",

    FIXTURE_ROOT / "practical_resources" / "software_engineering_toolkits.json",

    FIXTURE_ROOT / "practical_resources" / "data_science_toolkits.json",

    FIXTURE_ROOT / "practical_resources" / "artificial_intelligence_toolkits.json",

    FIXTURE_ROOT / "practical_resources" / "leadership_toolkits.json",

    FIXTURE_ROOT / "practical_resources" / "innovation_toolkits.json",

    FIXTURE_ROOT / "practical_resources" / "learning_toolkits.json",

]


# ==========================================================
# RESEARCH CONTRIBUTIONS
# ==========================================================

RESEARCH_CONTRIBUTION_FIXTURES = [

    FIXTURE_ROOT / "research_contributions" / "personal_research.json",

    FIXTURE_ROOT / "research_contributions" / "healthcare_research.json",

    FIXTURE_ROOT / "research_contributions" / "monitoring_evaluation_research.json",

    FIXTURE_ROOT / "research_contributions" / "software_engineering_research.json",

    FIXTURE_ROOT / "research_contributions" / "artificial_intelligence_research.json",

    FIXTURE_ROOT / "research_contributions" / "leadership_research.json",

    FIXTURE_ROOT / "research_contributions" / "innovation_research.json",

    FIXTURE_ROOT / "research_contributions" / "landmark_research.json",

]


# ==========================================================
# SEARCH CONFIGURATION
# ==========================================================

CONFIGURATION_FIXTURES = [

    FIXTURE_ROOT / "search_configuration.json",

]


# ==========================================================
# FIXTURE GROUPS
# ==========================================================

FIXTURE_GROUPS = {

    "core": CORE_FIXTURES,

    "tags": TAG_FIXTURES,

    "organizations": ORGANIZATION_FIXTURES,

    "library_resources": LIBRARY_RESOURCE_FIXTURES,

    "learning_videos": LEARNING_VIDEO_FIXTURES,

    "practical_resources": PRACTICAL_RESOURCE_FIXTURES,

    "research_contributions": RESEARCH_CONTRIBUTION_FIXTURES,

    "configuration": CONFIGURATION_FIXTURES,

}


# ==========================================================
# COMPLETE FIXTURE REGISTRY
# ==========================================================

FIXTURE_PATHS = [

    *CORE_FIXTURES,

    *TAG_FIXTURES,

    *ORGANIZATION_FIXTURES,

    *LIBRARY_RESOURCE_FIXTURES,

    *LEARNING_VIDEO_FIXTURES,

    *PRACTICAL_RESOURCE_FIXTURES,

    *RESEARCH_CONTRIBUTION_FIXTURES,

    *CONFIGURATION_FIXTURES,

]


# ==========================================================
# HELPERS
# ==========================================================

def get_fixture_group(name: str) -> list[Path]:
    """
    Return fixtures belonging to a specific group.

    Raises:
        KeyError:
            If the fixture group does not exist.
    """

    return FIXTURE_GROUPS[name]


def get_fixture_paths() -> list[Path]:
    """
    Return the complete fixture registry.
    """

    return FIXTURE_PATHS.copy()


def total_fixture_files() -> int:
    """
    Return the total number of registered fixture files.
    """

    return len(FIXTURE_PATHS)


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "FIXTURE_ROOT",

    "CORE_FIXTURES",

    "TAG_FIXTURES",

    "ORGANIZATION_FIXTURES",

    "LIBRARY_RESOURCE_FIXTURES",

    "LEARNING_VIDEO_FIXTURES",

    "PRACTICAL_RESOURCE_FIXTURES",

    "RESEARCH_CONTRIBUTION_FIXTURES",

    "CONFIGURATION_FIXTURES",

    "FIXTURE_GROUPS",

    "FIXTURE_PATHS",

    "get_fixture_group",

    "get_fixture_paths",

    "total_fixture_files",

]