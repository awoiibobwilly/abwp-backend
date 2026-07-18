"""
Knowledge Hub Seeder Console Renderer
=====================================

Provides a unified console rendering layer for the
Knowledge Hub seeding framework.

This module intentionally contains NO business logic.

Responsibilities
----------------
• Command banners
• Section headings
• Success / Warning / Error messages
• File progress
• Verification tables
• Statistics
• Final summaries
• Execution timing

Author
------
Awoii Bob Willy Portfolio
"""

from __future__ import annotations

from time import perf_counter
from typing import Any


# ==========================================================
# BACKWARD COMPATIBILITY
# ==========================================================

def print_model_count(
    label: str,
    count: int,
) -> None:
    """
    Backward-compatible wrapper.

    Existing commands can continue calling
    print_model_count() while newer code
    uses print_total() or print_table_row().
    """

    print_total(label, count)


# ==========================================================
# TABLE LAYOUT
# ==========================================================

MODEL_WIDTH = 32

RECORD_WIDTH = 10

STATUS_WIDTH = 12

TABLE_WIDTH = (
    MODEL_WIDTH
    + RECORD_WIDTH
    + STATUS_WIDTH
)


# ==========================================================
# CONSOLE SYMBOLS
# ==========================================================

SUCCESS = "✓"

ERROR = "✗"

WARNING = "⚠"

INFO = "•"

LINE = "=" * TABLE_WIDTH

DIVIDER = "-" * TABLE_WIDTH


# ==========================================================
# BANNER
# ==========================================================

def print_banner() -> None:
    """
    Display the command banner.
    """

    print()

    print(LINE)

    print("Knowledge Hub Seeder".center(TABLE_WIDTH))

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
# MESSAGES
# ==========================================================

def print_success(message: str) -> None:

    print(f"{SUCCESS} {message}")


def print_warning(message: str) -> None:

    print(f"{WARNING} {message}")


def print_error(message: str) -> None:

    print(f"{ERROR} {message}")


def print_info(message: str) -> None:

    print(f"{INFO} {message}")


# ==========================================================
# FILE PROGRESS
# ==========================================================

def print_file(
    filename: str,
    *,
    status: str = "success",
) -> None:
    """
    Render fixture progress.

    Status values

    success
    info
    warning
    error
    """

    symbols = {

        "success": SUCCESS,

        "info": INFO,

        "warning": WARNING,

        "error": ERROR,

    }

    print(

        f"{symbols.get(status, INFO)} {filename}"

    )


# ==========================================================
# TABLE
# ==========================================================

def print_table_header() -> None:
    """
    Render a verification table header.
    """

    print()

    print(LINE)

    print(

        f"{'Model':<{MODEL_WIDTH}}"

        f"{'Records':>{RECORD_WIDTH}}"

        f"{'Status':>{STATUS_WIDTH}}"

    )

    print(LINE)


def print_table_row(
    model: str,
    records: int,
    status: str = f"{SUCCESS} PASS",
) -> None:
    """
    Render one verification row.
    """

    print(

        f"{model:<{MODEL_WIDTH}}"

        f"{records:>{RECORD_WIDTH}}"

        f"{status:>{STATUS_WIDTH}}"

    )


def print_table_footer() -> None:

    print(LINE)


# ==========================================================
# TOTALS
# ==========================================================

def print_total(
    label: str,
    value: int,
) -> None:
    """
    Render summary totals.
    """

    print(

        f"{label:<{MODEL_WIDTH}}"

        f"{value:>{RECORD_WIDTH}}"

    )


# ==========================================================
# SUMMARY
# ==========================================================

def print_summary(
    stats: Any,
    elapsed: float,
) -> None:
    """
    Print normalization summary.
    """

    print()

    print(LINE)

    print("Summary")

    print(LINE)

    print()

    print_total(

        "Files Processed",

        stats.files_processed,

    )

    print_total(

        "Files Updated",

        stats.files_updated,

    )

    print_total(

        "Files Skipped",

        stats.files_skipped,

    )

    print()

    print_total(

        "Records Processed",

        stats.records_processed,

    )

    print_total(

        "Records Updated",

        stats.records_updated,

    )

    print()

    print_total(

        "Fields Removed",

        stats.removed_fields,

    )

    print_total(

        "Fields Renamed",

        stats.renamed_fields,

    )

    print_total(

        "Fields Merged",

        stats.merged_fields,

    )

    print_total(

        "Choice Conversions",

        stats.converted_choices,

    )

    print_total(

        "Defaults Inserted",

        stats.default_fields,

    )

    print_total(

        "Audit Fields",

        stats.audit_fields,

    )

    print_total(

        "Records Reordered",

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

    print_success(

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
    """

    def __init__(self) -> None:

        self.start = perf_counter()

    @property
    def elapsed(self) -> float:

        return perf_counter() - self.start

# ==========================================================
# TABLE DIVIDER
# ==========================================================


def print_table_divider() -> None:
    """
    Render a divider between table rows and totals.
    """

    print(DIVIDER)


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

    "print_table_header",

    "print_table_row",

    "print_table_footer",

    "print_total",

    "print_summary",

    "print_model_count",

    "print_table_divider",

]
