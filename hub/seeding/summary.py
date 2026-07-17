"""
Knowledge Hub Seeder Console Renderer
=====================================

Provides a consistent console output layer for the
Knowledge Hub seeding infrastructure.

This module intentionally contains NO business logic.

Responsibilities
----------------

• Banners
• Sections
• Success messages
• Warnings
• Errors
• Progress
• Statistics
• Final summary

Author
------
Awoii Bob Willy Portfolio
"""

from __future__ import annotations

from time import perf_counter
from typing import Any


# ==========================================================
# CONSOLE SYMBOLS
# ==========================================================

SUCCESS = "✓"

ERROR = "✗"

WARNING = "!"

INFO = "•"

LINE = "=" * 70

DIVIDER = "-" * 70


# ==========================================================
# BANNER
# ==========================================================

def print_banner() -> None:
    """
    Display the command banner.
    """

    print()

    print(LINE)

    print("Knowledge Hub Seeder")

    print(LINE)

    print()


# ==========================================================
# SECTION
# ==========================================================

def print_section(title: str) -> None:
    """
    Print a section heading.
    """

    print()

    print(DIVIDER)

    print(title)

    print(DIVIDER)


# ==========================================================
# SUCCESS
# ==========================================================

def print_success(message: str) -> None:

    print(f"{SUCCESS} {message}")


# ==========================================================
# WARNING
# ==========================================================

def print_warning(message: str) -> None:

    print(f"{WARNING} {message}")


# ==========================================================
# ERROR
# ==========================================================

def print_error(message: str) -> None:

    print(f"{ERROR} {message}")


# ==========================================================
# INFO
# ==========================================================

def print_info(message: str) -> None:

    print(f"{INFO} {message}")


# ==========================================================
# MODEL COUNT
# ==========================================================

def print_model_count(
    label: str,
    count: int,
) -> None:
    """
    Pretty aligned model counts.

    Example

    Knowledge Themes .......... 12
    """

    print(

        f"{label:.<40}{count}"

    )


# ==========================================================
# FILE PROGRESS
# ==========================================================

def print_file(
    filename: str,
    changed: bool,
) -> None:
    """
    Print fixture processing.

    Example

    ✓ organizations.json

    • healthcare_tags.json
    """

    symbol = SUCCESS if changed else INFO

    print(

        f"{symbol} {filename}"

    )


# ==========================================================
# SUMMARY
# ==========================================================

def print_summary(
    stats: Any,
    elapsed: float,
) -> None:
    """
    Print the final command summary.

    The stats object only needs to expose
    attributes used below.

    This keeps the renderer loosely coupled.
    """

    print()

    print(LINE)

    print("Summary")

    print(LINE)

    print()

    print_model_count(

        "Files processed",

        stats.files_processed,

    )

    print_model_count(

        "Files updated",

        stats.files_updated,

    )

    print_model_count(

        "Files skipped",

        stats.files_skipped,

    )

    print()

    print_model_count(

        "Records processed",

        stats.records_processed,

    )

    print_model_count(

        "Records updated",

        stats.records_updated,

    )

    print()

    print_model_count(

        "Fields removed",

        stats.removed_fields,

    )

    print_model_count(

        "Fields renamed",

        stats.renamed_fields,

    )

    print_model_count(

        "Fields merged",

        stats.merged_fields,

    )

    print_model_count(

        "Choice conversions",

        stats.converted_choices,

    )

    print_model_count(

        "Defaults inserted",

        stats.default_fields,

    )

    print_model_count(

        "Audit fields",

        stats.audit_fields,

    )

    print_model_count(

        "Reordered records",

        stats.reordered_records,

    )

    print()

    if stats.warnings:

        print_warning(

            f"{stats.warnings} warning(s)"

        )

    if stats.errors:

        print_error(

            f"{stats.errors} error(s)"

        )

    print()

    print(

        f"Completed in {elapsed:.2f} seconds."

    )

    print()

    print(LINE)


# ==========================================================
# TIMER
# ==========================================================

class Timer:
    """
    Lightweight execution timer.

    Example

        timer = Timer()

        ...

        print(timer.elapsed)
    """

    def __init__(self) -> None:

        self.start = perf_counter()

    @property
    def elapsed(self) -> float:

        return perf_counter() - self.start


# ==========================================================
# EXPORTS
# ==========================================================

__all__ = [

    "Timer",

    "print_banner",

    "print_section",

    "print_success",

    "print_warning",

    "print_error",

    "print_info",

    "print_file",

    "print_model_count",

    "print_summary",

]