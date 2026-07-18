"""
Knowledge Hub Seeder
====================

Management command responsible for seeding the
Knowledge Hub database from JSON fixtures.

Responsibilities
----------------

• Optional fixture normalization
• Fixture validation
• Fixture loading
• Database verification
• Summary reporting

This command intentionally delegates business logic to
the seeding infrastructure.

Modules

fixtures.py
    Fixture registry.

normalize.py
    Fixture normalization.

registry.py
    Verification registry.

summary.py
    Console rendering.

Author
------
Awoii Bob Willy Portfolio
"""

from __future__ import annotations

# ==========================================================
# STANDARD LIBRARY
# ==========================================================

from pathlib import Path
from typing import Any

# ==========================================================
# DJANGO
# ==========================================================

from django.conf import settings
from django.core.management import BaseCommand
from django.core.management import call_command
from django.core.management.base import CommandError

# ==========================================================
# LOCAL IMPORTS
# ==========================================================

from hub.seeding.fixtures import FIXTURE_PATHS
from hub.seeding.normalize import normalize_fixture_directory
from hub.seeding.validator import FixtureValidator
from hub.seeding.registry import MODEL_REGISTRY
from hub.seeding.summary import (
    Timer,
    print_banner,
    print_error,
    print_info,
    print_section,
    print_success,
    print_summary,
    print_table_header,
    print_table_row,
    print_table_footer,
    print_total,
    print_table_divider,
)

# ==========================================================
# COMMAND
# ==========================================================


class Command(BaseCommand):
    """
    Seed the Knowledge Hub database.

    Workflow

        Banner

            ↓

        Normalize (optional)

            ↓

        Validate

            ↓

        Load

            ↓

        Verify

            ↓

        Summary
    """

    help = "Seed the Knowledge Hub using the registered JSON fixtures."

    #
    # Constructor
    #

    def __init__(self) -> None:
        super().__init__()
        self.timer = Timer()
        self.base_dir = Path(settings.BASE_DIR)
        self.fixture_paths = FIXTURE_PATHS
        self.normalization_stats = None

    # ======================================================
    # CLI ARGUMENTS
    # ======================================================

    def add_arguments(
        self,
        parser,
    ) -> None:
        """
        Register command-line arguments.
        """

        #
        # Normalize fixtures before loading.
        #

        parser.add_argument(
            "--normalize",
            action="store_true",
            help=(
                "Normalize fixture files before "
                "validation and loading."
            ),
        )

        #
        # Validate only.
        #

        parser.add_argument(
            "--dry-run",
            action="store_true",
            help=(
                "Run normalization and validation "
                "without loading fixtures."
            ),
        )

        #
        # Verify database only.
        #

        parser.add_argument(
            "--verify-only",
            action="store_true",
            help=(
                "Skip normalization and loading. "
                "Verify database contents only."
            ),
        )

        #
        # Verbose file progress.
        #

        parser.add_argument(
            "--verbose-files",
            action="store_true",
            help="Display every processed fixture.",
        )

        #
        # Stop on first error.
        #

        parser.add_argument(
            "--fail-fast",
            action="store_true",
            help=(
                "Abort immediately when an error "
                "is encountered."
            ),
        )

        print_section("Checking fixture integrity...")

        validator = FixtureValidator(
            self.fixture_paths,
        )

        validator.validate()

        print_success("Registry validation passed.")

    # ======================================================
    # FIXTURE VALIDATION
    # ======================================================

    def _resolve_fixture_path(
        self,
        fixture: Path,
    ) -> Path:
        """
        Resolve a fixture path relative to BASE_DIR.

        Absolute paths are returned unchanged.
        """

        if fixture.is_absolute():
            return fixture

        return self.base_dir / fixture

    # ------------------------------------------------------

    def _validate_fixture_paths(self) -> None:
        """
        Ensure every registered fixture exists.
        """

        print_section("Validating fixture files...")

        missing: list[Path] = []

        for fixture in self.fixture_paths:
            path = self._resolve_fixture_path(
                fixture,
            )

            if not path.exists():
                missing.append(path)
                continue

            print_success(
                path.name,
            )

        if missing:
            raise CommandError(
                "Missing fixture(s):\n"
                + "\n".join(str(path) for path in missing)
            )

    # ------------------------------------------------------

    def _validate_fixture_contents(self) -> None:
        """
        Validate that every fixture contains
        valid JSON.

        Structural normalization is delegated to
        normalize.py.
        """

        import json

        for fixture in self.fixture_paths:
            path = self._resolve_fixture_path(
                fixture,
            )

            try:
                with path.open(
                    "r",
                    encoding="utf-8",
                ) as stream:
                    data = json.load(stream)
            except json.JSONDecodeError as exc:
                raise CommandError(f"{path.name}: {exc}")

            if not isinstance(
                data,
                list,
            ):
                raise CommandError(f"{path.name} must contain a JSON array.")

    # ======================================================
    # NORMALIZATION
    # ======================================================

    def _normalize_fixtures(self) -> None:
        """
        Normalize every registered fixture.
        """

        print_section("Normalizing fixtures...")

        self.normalization_stats = normalize_fixture_directory(
            fixture_paths=self.fixture_paths,
            base_dir=self.base_dir,
        )

        print_success(
            f"{self.normalization_stats.files_processed} files processed"
        )
        print_success(
            f"{self.normalization_stats.records_processed} records scanned"
        )
        print_success(
            f"{self.normalization_stats.records_updated} records updated"
        )

    # ======================================================
    # FIXTURE LOADING
    # ======================================================

    def _load_fixture(self, fixture: Path) -> None:
        path = self._resolve_fixture_path(fixture)

        try:
            call_command(
                "loaddata",
                str(path),
                verbosity=0,
            )

        except Exception as exc:
            raise CommandError(
                f"\n"
                f"Failed loading fixture:\n"
                f"  File : {path.name}\n"
                f"  Path : {path}\n"
                f"  Error: {exc}"
            ) from exc

        print_success(path.name)

    # ------------------------------------------------------

    def _load_all_fixtures(self) -> None:
        """
        Load all registered fixtures in dependency order
        and report progress.
        """

        print_section("Loading fixtures...")

        for fixture in self.fixture_paths:
            self._load_fixture(fixture)

        print()
        print_success("All fixtures loaded.")

    # ======================================================
    # DATABASE VERIFICATION
    # ======================================================

    def _verify_model(
        self,
        entry,
    ) -> int:
        """
        Verify a single registry model.

        Parameters
        ----------
        entry:
            RegistryEntry

        Returns
        -------
        int
            Number of records.
        """

        count = entry.model.objects.count()

        #
        # Minimum records.
        #

        if count < entry.minimum_records:
            raise CommandError(
                f"{entry.label}: "
                f"expected at least {entry.minimum_records}, "
                f"found {count}."
            )

        return count

    # ------------------------------------------------------

    def _verify_registry(self) -> dict[str, int]:
        """
        Verify every registered model.

        Returns
        -------
        dict

            {

                "Knowledge Hub": 1,

                "Knowledge Themes": 12,

                ...

            }
        """

        results: dict[str, int] = {}

        for entry in MODEL_REGISTRY:
            count = self._verify_model(
                entry,
            )

            results[entry.label] = count

        return results

    # ------------------------------------------------------

    # ==========================================================
    # DATABASE VERIFICATION
    # ==========================================================

    def _verify_database(self) -> dict[str, int]:
        """
        Verify the seeded Knowledge Hub database.

        Executes a final verification pass after all fixture files
        have been loaded to confirm that every registered model
        contains at least the expected number of records.

        The verification results are rendered as a formatted table
        showing each model, its record count, and verification
        status, followed by overall database totals.

        Returns
        -------
        dict[str, int]
            Mapping of model labels to the number of records
            currently stored in the database.

        Notes
        -----
        This method is responsible only for orchestrating the
        verification workflow.

        Actual verification logic is delegated to
        ``_verify_registry()``.

        Console rendering is delegated entirely to the
        ``hub.seeding.summary`` module.
        """

        # ------------------------------------------------------
        # Display verification section heading.
        # ------------------------------------------------------

        print_section(
            "Verifying database..."
        )

        # ------------------------------------------------------
        # Verify every registered model and collect the
        # resulting record counts.
        # ------------------------------------------------------

        results = self._verify_registry()

        # ------------------------------------------------------
        # Render verification table.
        # ------------------------------------------------------

        print_table_header()

        total_records = 0

        for label, count in results.items():

            total_records += count

            print_table_row(
                label,
                count,
            )

        # ------------------------------------------------------
        # Render verification totals.
        # ------------------------------------------------------

        print_table_divider()

        print_total(
            "Total Models",
            len(results),
        )

        print_total(
            "Total Records",
            total_records,
        )

        print_table_footer()

        # ------------------------------------------------------
        # Display completion message.
        # ------------------------------------------------------

        print()

        print_success(
            "Database verification completed."
        )

        return results

    # ======================================================
    # ORCHESTRATION
    # ======================================================

    def handle(
        self,
        *args: Any,
        **options: Any,
    ) -> None:
        """
        Execute the complete seeding workflow.

        Workflow
        --------

            Banner
                ↓
            Normalize (optional)
                ↓
            Validate Fixtures
                ↓
            Dry Run?
                ↓
            Load Fixtures
                ↓
            Verify Database
                ↓
            Summary
        """

        print_banner()

        try:
            #
            # -------------------------------------------------
            # VERIFY ONLY
            # -------------------------------------------------
            #

            if options["verify_only"]:
                print_info("Verification-only mode.")

                self._verify_database()

                print_success("Verification successful.")

                return

            #
            # -------------------------------------------------
            # OPTIONAL NORMALIZATION
            # -------------------------------------------------
            #

            if options["normalize"]:
                self._normalize_fixtures()

            #
            # -------------------------------------------------
            # VALIDATION
            # -------------------------------------------------
            #

            self._validate_fixture_paths()
            self._validate_fixture_contents()

            #
            # -------------------------------------------------
            # DRY RUN
            # -------------------------------------------------
            #

            if options["dry_run"]:
                print()
                print_success("Dry run completed successfully.")

                if self.normalization_stats is not None:
                    print_summary(
                        self.normalization_stats,
                        self.timer.elapsed,
                    )

                return

            #
            # -------------------------------------------------
            # LOAD FIXTURES
            # -------------------------------------------------
            #

            self._load_all_fixtures()

            #
            # -------------------------------------------------
            # VERIFY DATABASE
            # -------------------------------------------------
            #

            self._verify_database()

            #
            # -------------------------------------------------
            # FINAL SUMMARY
            # -------------------------------------------------
            #

            if self.normalization_stats is not None:
                print_summary(
                    self.normalization_stats,
                    self.timer.elapsed,
                )
            else:
                print()
                print_success(f"Completed in {self.timer.elapsed:.2f} seconds.")

        #
        # -----------------------------------------------------
        # DJANGO ERRORS
        # -----------------------------------------------------
        #

        except CommandError:
            raise

        #
        # -----------------------------------------------------
        # UNEXPECTED ERRORS
        # -----------------------------------------------------
        #

        except Exception as exc:
            print()
            print_error("Unexpected failure.")
            raise CommandError(str(exc)) from exc