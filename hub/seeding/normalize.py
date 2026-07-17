"""
Knowledge Hub Fixture Normalization Engine
==========================================

Transforms legacy Knowledge Hub fixtures into the current
schema before they are validated and loaded into Django.

The engine is intentionally model-agnostic. It does not
contain model-specific migration rules; instead, it reads
those rules from ``hub.seeding.migrations``.

Normalization Pipeline
----------------------

For each fixture record:

    Load Record
        ↓
    Lookup Migration Rules
        ↓
    Remove Obsolete Fields
        ↓
    Rename Legacy Fields
        ↓
    Merge Legacy Fields
        ↓
    Convert Choice Values
        ↓
    Apply Default Values
        ↓
    Ensure Audit Fields
        ↓
    Canonical Field Ordering
        ↓
    Write Normalized Record

Design Goals
------------

• Idempotent
• Deterministic
• Declarative
• Reusable
• Safe to run repeatedly
• Independent of Django ORM

Author
------
Awoii Bob Willy Portfolio
"""

from __future__ import annotations

# ==========================================================
# STANDARD LIBRARY
# ==========================================================

import copy
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ==========================================================
# LOCAL IMPORTS
# ==========================================================

from .migrations import get_model_rules

# ==========================================================
# CONSTANTS
# ==========================================================

#
# ISO timestamp used when audit fields are missing.
#
DEFAULT_TIMESTAMP = datetime.now(
    tz=timezone.utc,
).isoformat()

#
# Audit fields appended to every fixture.
#
AUDIT_FIELDS = (

    "display_order",

    "is_active",

    "created_at",

    "updated_at",

)

#
# Default audit values.
#
AUDIT_DEFAULTS = {

    "display_order": 0,

    "is_active": True,

    "created_at": DEFAULT_TIMESTAMP,

    "updated_at": DEFAULT_TIMESTAMP,

}

#
# Canonical ordering.
#
# These fields always appear LAST.
#
CANONICAL_TRAILING_FIELDS = [

    "display_order",

    "is_active",

    "created_at",

    "updated_at",

]

#
# Supported migration operations.
#
SUPPORTED_OPERATIONS = {

    "remove_fields",

    "rename_fields",

    "merge_fields",

    "choice_mappings",

    "defaults",

}

#
# Default JSON formatting.
#
JSON_INDENT = 4

JSON_ENCODING = "utf-8"

# ==========================================================
# TYPE ALIASES
# ==========================================================

JSONDict = dict[str, Any]

JSONObject = dict[str, Any]

JSONArray = list[JSONObject]

MigrationRules = dict[str, Any]

# ==========================================================
# NORMALIZATION STATISTICS
# ==========================================================

@dataclass(slots=True)
class NormalizationStats:
    """
    Statistics collected during normalization.

    These values accumulate across the entire
    normalization process.
    """

    #
    # Files
    #

    files_processed: int = 0

    files_updated: int = 0

    files_skipped: int = 0

    #
    # Records
    #

    records_processed: int = 0

    records_updated: int = 0

    #
    # Migration Operations
    #

    removed_fields: int = 0

    renamed_fields: int = 0

    merged_fields: int = 0

    converted_choices: int = 0

    default_fields: int = 0

    audit_fields: int = 0

    reordered_records: int = 0

    #
    # Errors
    #

    errors: int = 0

    warnings: int = 0

    #
    # Optional details
    #

    messages: list[str] = field(default_factory=list)

    # ------------------------------------------------------
    # Helpers
    # ------------------------------------------------------

    def warning(self, message: str) -> None:
        """Register a warning."""

        self.warnings += 1
        self.messages.append(f"WARNING: {message}")

    def error(self, message: str) -> None:
        """Register an error."""

        self.errors += 1
        self.messages.append(f"ERROR: {message}")

    def as_dict(self) -> dict[str, Any]:
        """
        Export statistics.

        Useful for summaries and testing.
        """

        return {

            "files": self.files_processed,

            "updated_files": self.files_updated,

            "skipped_files": self.files_skipped,

            "records": self.records_processed,

            "updated_records": self.records_updated,

            "removed_fields": self.removed_fields,

            "renamed_fields": self.renamed_fields,

            "merged_fields": self.merged_fields,

            "choice_conversions": self.converted_choices,

            "default_fields": self.default_fields,

            "audit_fields": self.audit_fields,

            "reordered_records": self.reordered_records,

            "warnings": self.warnings,

            "errors": self.errors,

        }

# ==========================================================
# INTERNAL HELPERS
# ==========================================================

def utc_timestamp() -> str:
    """
    Return the current UTC timestamp in ISO-8601 format.

    Used when inserting missing audit fields.
    """

    return datetime.now(

        tz=timezone.utc,

    ).isoformat()


def deepcopy_record(record: JSONObject) -> JSONObject:
    """
    Return a defensive deep copy.

    The normalization engine never mutates the caller's
    object directly.
    """

    return copy.deepcopy(record)


def model_name(record: JSONObject) -> str:
    """
    Return the Django model label from a fixture record.

    Example:

        hub.organization
        hub.libraryresource
    """

    return record["model"]


def migration_rules(record: JSONObject) -> MigrationRules:
    """
    Retrieve migration rules for a fixture record.

    Unknown models automatically receive an empty
    migration configuration.
    """

    return get_model_rules(

        model_name(record),

    )

# ==========================================================
# LOW-LEVEL NORMALIZATION HELPERS
# ==========================================================

def remove_fields(
    fields: JSONObject,
    rules: MigrationRules,
    stats: NormalizationStats,
) -> bool:
    """
    Remove obsolete fields.

    Returns
    -------
    bool
        True if at least one field was removed.
    """

    changed = False

    obsolete_fields = rules.get("remove_fields", set())

    for field in obsolete_fields:

        if field in fields:

            del fields[field]

            stats.removed_fields += 1

            changed = True

    return changed


# ----------------------------------------------------------


def rename_fields(
    fields: JSONObject,
    rules: MigrationRules,
    stats: NormalizationStats,
) -> bool:
    """
    Rename legacy fields.

    Existing destination fields are never overwritten.
    """

    changed = False

    mappings = rules.get("rename_fields", {})

    for old_name, new_name in mappings.items():

        if old_name not in fields:
            continue

        if new_name in fields:
            continue

        fields[new_name] = fields.pop(old_name)

        stats.renamed_fields += 1

        changed = True

    return changed


# ----------------------------------------------------------


def merge_fields(
    fields: JSONObject,
    rules: MigrationRules,
    stats: NormalizationStats,
) -> bool:
    """
    Merge multiple legacy fields into one list.

    Example
    -------

    primary_theme

    secondary_themes

            ↓

        themes
    """

    changed = False

    mappings = rules.get("merge_fields", {})

    for destination, sources in mappings.items():

        merged: list[Any] = []

        for source in sources:

            if source not in fields:
                continue

            value = fields.pop(source)

            if value is None:
                continue

            if isinstance(value, list):

                merged.extend(value)

            else:

                merged.append(value)

        #
        # Remove duplicates while preserving order.
        #

        unique: list[Any] = []

        for item in merged:

            if item not in unique:

                unique.append(item)

        if not unique:
            continue

        #
        # Existing destination values are preserved.
        #

        existing = fields.get(destination, [])

        if not isinstance(existing, list):

            existing = [existing]

        combined = existing.copy()

        for value in unique:

            if value not in combined:

                combined.append(value)

        fields[destination] = combined

        stats.merged_fields += 1

        changed = True

    return changed


# ----------------------------------------------------------


def convert_choice_values(
    fields: JSONObject,
    rules: MigrationRules,
    stats: NormalizationStats,
) -> bool:
    """
    Convert legacy choice labels into
    model-compatible values.
    """

    changed = False

    mappings = rules.get("choice_mappings", {})

    for field_name, choices in mappings.items():

        if field_name not in fields:
            continue

        current_value = fields[field_name]

        converted = choices.get(current_value)

        if converted is None:
            continue

        if converted == current_value:
            continue

        fields[field_name] = converted

        stats.converted_choices += 1

        changed = True

    return changed


# ----------------------------------------------------------


def apply_defaults(
    fields: JSONObject,
    rules: MigrationRules,
    stats: NormalizationStats,
) -> bool:
    """
    Insert default values for newly introduced fields.

    Existing values are never replaced.
    """

    changed = False

    defaults = rules.get("defaults", {})

    for field_name, default in defaults.items():

        if field_name in fields:
            continue

        fields[field_name] = copy.deepcopy(default)

        stats.default_fields += 1

        changed = True

    return changed


# ==========================================================
# AUDIT FIELD NORMALIZATION
# ==========================================================

def ensure_audit_fields(
    fields: JSONObject,
    stats: NormalizationStats,
) -> bool:
    """
    Ensure every fixture record contains the required
    audit fields.

    Existing values are preserved.

    Missing fields receive sensible defaults.

    Returns
    -------
    bool
        True if at least one audit field was inserted.
    """

    changed = False

    #
    # display_order
    #

    if "display_order" not in fields:

        fields["display_order"] = AUDIT_DEFAULTS["display_order"]

        stats.audit_fields += 1

        changed = True

    #
    # is_active
    #

    if "is_active" not in fields:

        fields["is_active"] = AUDIT_DEFAULTS["is_active"]

        stats.audit_fields += 1

        changed = True

    #
    # created_at
    #

    if "created_at" not in fields:

        fields["created_at"] = utc_timestamp()

        stats.audit_fields += 1

        changed = True

    #
    # updated_at
    #

    if "updated_at" not in fields:

        fields["updated_at"] = utc_timestamp()

        stats.audit_fields += 1

        changed = True

    return changed


# ==========================================================
# CANONICAL FIELD ORDERING
# ==========================================================

def canonical_order(
    record: JSONObject,
    stats: NormalizationStats,
) -> tuple[JSONObject, bool]:
    """
    Rebuild a fixture record into the canonical order.

    Canonical layout
    ----------------

    model

    pk

    fields
        ├── domain fields
        ├── display_order
        ├── is_active
        ├── created_at
        └── updated_at

    Returns
    -------
    tuple
        (
            reordered_record,
            changed
        )
    """

    #
    # Defensive copy
    #

    record = deepcopy_record(record)

    fields = record["fields"]

    #
    # Preserve every domain field first.
    #

    ordered_fields: JSONObject = {}

    for key, value in fields.items():

        if key in CANONICAL_TRAILING_FIELDS:

            continue

        ordered_fields[key] = value

    #
    # Append audit fields in fixed order.
    #

    for field_name in CANONICAL_TRAILING_FIELDS:

        if field_name in fields:

            ordered_fields[field_name] = fields[field_name]

    #
    # Compare ordering.
    #

    changed = list(fields.keys()) != list(ordered_fields.keys())

    if changed:

        stats.reordered_records += 1

    #
    # Replace fields.
    #

    record["fields"] = ordered_fields

    return record, changed


# ==========================================================
# RECORD VALIDATION HELPERS
# ==========================================================

def has_required_keys(
    record: JSONObject,
) -> bool:
    """
    Validate the minimum fixture structure.

    Required keys

    - model
    - pk
    - fields
    """

    return all(

        key in record

        for key in (

            "model",

            "pk",

            "fields",

        )

    )


def ensure_record_structure(
    record: JSONObject,
) -> None:
    """
    Validate fixture structure.

    Raises
    ------
    ValueError
        If the fixture record is malformed.
    """

    if not has_required_keys(record):

        raise ValueError(

            "Fixture record must contain "

            "'model', 'pk', and 'fields'."

        )

    if not isinstance(record["fields"], dict):

        raise TypeError(

            "'fields' must be a dictionary."

        )


# ==========================================================
# CHANGE AGGREGATOR
# ==========================================================

def any_changes(*changes: bool) -> bool:
    """
    Convenience helper used by the pipeline.

    Example
    -------

    changed = any_changes(

        remove,

        rename,

        merge,

        choices,

        defaults,

        audit,

        reorder,

    )
    """

    return any(changes)


# ==========================================================
# RECORD NORMALIZATION
# ==========================================================

@dataclass(slots=True)
class NormalizationResult:
    """
    Result returned after normalizing a single fixture record.
    """

    record: JSONObject

    changed: bool

    model: str

    pk: Any


# ==========================================================
# RECORD NORMALIZATION PIPELINE
# ==========================================================

def normalize_record(
    record: JSONObject,
    stats: NormalizationStats,
) -> NormalizationResult:
    """
    Normalize a single fixture record.

    Pipeline
    --------

        Validate Structure
                ↓
        Defensive Copy
                ↓
        Lookup Migration Rules
                ↓
        Remove Obsolete Fields
                ↓
        Rename Legacy Fields
                ↓
        Merge Legacy Fields
                ↓
        Convert Choice Values
                ↓
        Apply Default Values
                ↓
        Ensure Audit Fields
                ↓
        Canonical Ordering
                ↓
        Return Result

    Parameters
    ----------
    record:
        Django fixture record.

    stats:
        Shared normalization statistics.

    Returns
    -------
    NormalizationResult
    """

    #
    # Validate record.
    #

    ensure_record_structure(record)

    #
    # Never mutate the caller's object.
    #

    record = deepcopy_record(record)

    stats.records_processed += 1

    #
    # Model metadata.
    #

    model = model_name(record)

    pk = record["pk"]

    fields = record["fields"]

    #
    # Migration rules.
    #

    rules = migration_rules(record)

    #
    # Transformation pipeline.
    #

    removed = remove_fields(

        fields,

        rules,

        stats,

    )

    renamed = rename_fields(

        fields,

        rules,

        stats,

    )

    merged = merge_fields(

        fields,

        rules,

        stats,

    )

    converted = convert_choice_values(

        fields,

        rules,

        stats,

    )

    defaulted = apply_defaults(

        fields,

        rules,

        stats,

    )

    audited = ensure_audit_fields(

        fields,

        stats,

    )

    #
    # Canonical ordering.
    #

    record, reordered = canonical_order(

        record,

        stats,

    )

    #
    # Final change detection.
    #

    changed = any_changes(

        removed,

        renamed,

        merged,

        converted,

        defaulted,

        audited,

        reordered,

    )

    if changed:

        stats.records_updated += 1

    return NormalizationResult(

        record=record,

        changed=changed,

        model=model,

        pk=pk,

    )


# ==========================================================
# FIXTURE FILE NORMALIZATION
# ==========================================================

def load_fixture_file(
    fixture_path: Path,
) -> JSONArray:
    """
    Load a Django fixture file.

    Parameters
    ----------
    fixture_path:
        Path to a JSON fixture.

    Returns
    -------
    list[dict]

    Raises
    ------
    FileNotFoundError
    json.JSONDecodeError
    """

    with fixture_path.open(

        "r",

        encoding=JSON_ENCODING,

    ) as stream:

        data = json.load(stream)

    if not isinstance(data, list):

        raise TypeError(

            f"{fixture_path} must contain a JSON array."

        )

    return data


# ----------------------------------------------------------


def save_fixture_file(
    fixture_path: Path,
    records: JSONArray,
) -> None:
    """
    Write a normalized fixture file.

    Existing files are overwritten only after the
    normalization pipeline has completed successfully.
    """

    with fixture_path.open(

        "w",

        encoding=JSON_ENCODING,

    ) as stream:

        json.dump(

            records,

            stream,

            indent=JSON_INDENT,

            ensure_ascii=False,

        )

        stream.write("\n")


# ----------------------------------------------------------


def normalize_fixture_file(
    fixture_path: Path,
    stats: NormalizationStats,
) -> bool:
    """
    Normalize an entire fixture file.

    Workflow
    --------

        Read JSON
            ↓
        Normalize every record
            ↓
        Detect changes
            ↓
        Rewrite file (if needed)

    Parameters
    ----------
    fixture_path

    stats

    Returns
    -------
    bool

        True if the file changed.
    """

    #
    # File bookkeeping.
    #

    stats.files_processed += 1

    #
    # Load.
    #

    records = load_fixture_file(

        fixture_path,

    )

    normalized_records: JSONArray = []

    file_changed = False

    #
    # Normalize each record.
    #

    for record in records:

        result = normalize_record(

            record,

            stats,

        )

        normalized_records.append(

            result.record,

        )

        if result.changed:

            file_changed = True

    #
    # Persist.
    #

    if file_changed:

        save_fixture_file(

            fixture_path,

            normalized_records,

        )

        stats.files_updated += 1

    else:

        stats.files_skipped += 1

    return file_changed

# ==========================================================
# DIRECTORY NORMALIZATION
# ==========================================================

def normalize_fixture_directory(
    fixture_paths: list[Path],
    base_dir: Path | None = None,
) -> NormalizationStats:
    """
    Normalize multiple fixture files.

    Parameters
    ----------
    fixture_paths

        Ordered fixture registry.

    base_dir

        Optional Django BASE_DIR.

        Relative fixture paths are resolved
        against this directory.

    Returns
    -------
    NormalizationStats
    """

    stats = NormalizationStats()

    for fixture in fixture_paths:

        #
        # Resolve absolute path.
        #

        path = fixture

        if base_dir is not None:

            path = base_dir / fixture

        try:

            normalize_fixture_file(

                path,

                stats,

            )

        except FileNotFoundError:

            stats.error(

                f"Fixture not found: {path}"

            )

        except json.JSONDecodeError as exc:

            stats.error(

                f"Invalid JSON: {path} ({exc})"

            )

        except Exception as exc:

            stats.error(

                f"{path}: {exc}"

            )

    return stats

# ==========================================================
# PUBLIC API
# ==========================================================

__all__ = [

    #
    # Statistics
    #

    "NormalizationStats",

    "NormalizationResult",

    #
    # Record
    #

    "normalize_record",

    #
    # File
    #

    "normalize_fixture_file",

    #
    # Directory
    #

    "normalize_fixture_directory",

]