from __future__ import annotations

from hub.seeding.registry import MODEL_LOOKUP

from collections.abc import Hashable

# ==========================================================
# STANDARD LIBRARY
# ==========================================================

import json
from pathlib import Path
from collections import defaultdict

# ==========================================================
# DJANGO
# ==========================================================

from django.core.management.base import CommandError


# ==========================================================
# FIXTURE VALIDATOR
# ==========================================================

class FixtureValidator:
    """
    Performs integrity validation on fixture files before
    they are loaded into the database.
    """

    # ======================================================
    # REGISTRY HELPERS
    # ======================================================

    def __init__(self, fixture_paths: list[Path]) -> None:

        self.fixture_paths = fixture_paths

        self.records: list[dict] = []

        self.errors: list[str] = []

    # ======================================================
    # PUBLIC API
    # ======================================================

    def validate(self) -> None:
        """
        Execute all validation checks.
        """

        self._validate_registry()

        self._load_records()

        self._validate_data_integrity()

        self._raise_if_errors()

    # ======================================================
    # REGISTRY VALIDATION
    # ======================================================

    def _validate_registry(self) -> None:

        self._check_registry_not_empty()

        self._check_duplicate_paths()

        self._check_missing_files()

        self._check_invalid_json()

        self._check_empty_fixtures()

    # ------------------------------------------------------

    def _check_registry_not_empty(self) -> None:

        if self.fixture_paths:
            return

        self.errors.append(
            "No fixture files have been registered."
        )

    # ------------------------------------------------------

    def _check_duplicate_paths(self) -> None:

        seen = set()

        for path in self.fixture_paths:

            resolved = path.resolve()

            if resolved in seen:

                self.errors.append(
                    f"Duplicate fixture registration:\n"
                    f"  {path.name}"
                )

            else:

                seen.add(resolved)

    # ------------------------------------------------------

    def _check_missing_files(self) -> None:

        for path in self.fixture_paths:

            if path.exists():
                continue

            self.errors.append(
                f"Missing fixture file:\n"
                f"  {path}"
            )

    # ------------------------------------------------------

    def _check_invalid_json(self) -> None:

        for path in self.fixture_paths:

            if not path.exists():
                continue

            try:

                with path.open(
                    "r",
                    encoding="utf-8",
                ) as fp:

                    json.load(fp)

            except json.JSONDecodeError as exc:

                self.errors.append(
                    f"Invalid JSON:\n"
                    f"  {path.name}\n"
                    f"  Line {exc.lineno}, "
                    f"Column {exc.colno}"
                )

    # ------------------------------------------------------

    def _check_empty_fixtures(self) -> None:

        for path in self.fixture_paths:

            if not path.exists():
                continue

            with path.open(
                "r",
                encoding="utf-8",
            ) as fp:

                data = json.load(fp)

            if len(data) == 0:

                self.errors.append(
                    f"Empty fixture:\n"
                    f"  {path.name}"
                )

    # ======================================================
    # RECORD LOADER
    # ======================================================

    def _load_records(self) -> None:
        """
        Load every fixture record into memory once.
        """

        self.records.clear()

        for path in self.fixture_paths:

            if not path.exists():
                continue

            with path.open(
                "r",
                encoding="utf-8",
            ) as fp:

                data = json.load(fp)

            for obj in data:

                self.records.append(
                    {
                        "file": path.name,
                        "model": obj["model"],
                        "pk": obj["pk"],
                        "fields": obj["fields"],
                    }
                )

    # ======================================================
    # DATA INTEGRITY
    # ======================================================

    def _validate_data_integrity(self) -> None:

        validators = (

            self._validate_schema,

            self._validate_primary_keys,

            self._validate_unique_fields,

            self._validate_required_fields,

            self._validate_relationships,

        )

        for validator in validators:
            validator()
    # ------------------------------------------------------

    def _validate_schema(self) -> None:
        """
        Validate the structure of every fixture record before
        performing deeper integrity checks.
        """

        required_keys = {

            "model",

            "pk",

            "fields",

        }

        for index, record in enumerate(self.records, start=1):

            missing = required_keys - record.keys()

            if missing:

                self.errors.append(

                    "Invalid Fixture Record\n\n"

                    f"Record : {index}\n"

                    f"Missing Keys : {', '.join(sorted(missing))}"

                )

                continue

            if not isinstance(record["model"], str):

                self.errors.append(

                    "Invalid Fixture Record\n\n"

                    f"Record : {index}\n"

                    "Field : model\n"

                    "Expected : string"

                )

            if record["pk"] is None:

                self.errors.append(

                    "Invalid Fixture Record\n\n"

                    f"Record : {index}\n"

                    "Field : pk\n"

                    "Primary key cannot be null."

                )

            if not isinstance(record["fields"], dict):

                self.errors.append(

                    "Invalid Fixture Record\n\n"

                    f"Record : {index}\n"

                    "Field : fields\n"

                    "Expected : object/dictionary."

                )

    # ------------------------------------------------------

    def _validate_primary_keys(self) -> None:
        """
        Ensure primary keys are unique per model.
        """

        seen = defaultdict(dict)

        for record in self.records:

            model = record["model"]

            pk = record["pk"]

            file = record["file"]

            if pk in seen[model]:

                self._record_duplicate(

                    check="Duplicate Primary Key",

                    model=model,

                    value=pk,

                    first_file=seen[model][pk],

                    duplicate_file=file,

                )

            else:

                seen[model][pk] = file

    def _validate_unique_fields(self) -> None:
        """
        Ensure configured fields are unique per model.
        """

        seen = defaultdict(
            lambda: defaultdict(dict)
        )

        for record in self.records:

            model = record["model"]

            entry = MODEL_LOOKUP.get(model)

            if entry is None:
                continue

            for field in entry.unique_fields:

                value = record["fields"].get(field)

                #
                # Ignore empty values.
                #
                if value in (None, ""):
                    continue

                if value in seen[model][field]:

                    self._record_duplicate(

                        check=f"Duplicate '{field}'",

                        model=model,

                        value=value,

                        first_file=seen[model][field][value],

                        duplicate_file=record["file"],

                    )

                else:

                    seen[model][field][value] = record["file"]
    
    # ------------------------------------------------------

    def _validate_required_fields(self) -> None:
        """
        Ensure configured required fields exist and contain values.
        """

        for record in self.records:

            model = record["model"]

            entry = MODEL_LOOKUP.get(model)

            if entry is None:
                continue

            fields = record["fields"]

            for field in entry.required_fields:

                #
                # Field missing entirely.
                #
                if field not in fields:

                    self.errors.append(

                        "Missing Required Field\n\n"

                        f"Model : {model}\n"

                        f"Field : {field}\n"

                        f"Fixture : {record['file']}"

                    )

                    continue

                value = fields[field]

                #
                # Empty values are treated as missing.
                #
                if value is None:

                    self.errors.append(

                        "Required Field Cannot Be Null\n\n"

                        f"Model : {model}\n"

                        f"Field : {field}\n"

                        f"Fixture : {record['file']}"

                    )

                    continue

                #
                # Empty strings are also invalid.
                #
                if isinstance(value, str) and not value.strip():

                    self.errors.append(

                        "Required Field Cannot Be Empty\n\n"

                        f"Model : {model}\n"

                        f"Field : {field}\n"

                        f"Fixture : {record['file']}"

                    )
    # ------------------------------------------------------

    def _build_primary_key_index(
        self,
    ) -> dict[str, set[Hashable]]:

        """
        Build a lookup of every available primary key
        grouped by Django model label.

        Example

        {
            "hub.organization": {1,2,3},
            "hub.knowledgetheme": {1,5,9},
        }
        """

        index = defaultdict(set)

        for record in self.records:

            index[
                record["model"]
            ].add(record["pk"])

        return index

    # ------------------------------------------------------

    def _validate_relationships(self) -> None:
        """
        Ensure every configured relationship points to an
        existing fixture record.
        """

        pk_index = self._build_primary_key_index()

        for record in self.records:

            model = record["model"]

            entry = MODEL_LOOKUP.get(model)

            if entry is None:
                continue

            fields = record["fields"]

            for (
                field_name,
                target_model,
                is_many,
            ) in entry.relationship_fields:

                #
                # Relationship not supplied.
                #
                if field_name not in fields:
                    continue

                value = fields[field_name]

                #
                # Skip optional relationships.
                #
                if value in (None, ""):
                    continue

                #
                # ManyToMany
                #
                if is_many:

                    if not isinstance(value, list):

                        self.errors.append(

                            "Invalid Relationship\n\n"

                            f"Model : {model}\n"

                            f"Field : {field_name}\n"

                            "Expected a list of primary keys."

                        )

                        continue

                    for pk in value:

                        if pk not in pk_index[target_model]:

                            self._record_missing_relationship(

                                model=model,

                                record_pk=record["pk"],

                                field=field_name,

                                target_model=target_model,

                                value=pk,

                                fixture=record["file"],

                            )

                #
                # ForeignKey / OneToOne
                #
                else:

                    if value not in pk_index[target_model]:

                        self._record_missing_relationship(

                            model=model,

                            field=field_name,

                            target_model=target_model,

                            value=value,

                            fixture=record["file"],

                        )

    # ======================================================
    # HELPERS
    # ======================================================

    def _record_duplicate(
        self,
        *,
        check: str,
        model: str,
        value,
        first_file: str,
        duplicate_file: str,
    ) -> None:

        self.errors.append(

            f"{check}\n\n"

            f"Model : {model}\n"

            f"Value : {value}\n"

            f"First Fixture : {first_file}\n"

            f"Duplicate Fixture : {duplicate_file}"

        )

    # ------------------------------------------------------

    def _record_missing_relationship(
        self,
        *,
        model: str,
        field: str,
        target_model: str,
        value,
        fixture: str,
    ) -> None:

        self.errors.append(

            "Broken Relationship\n\n"

            f"Model : {model}\n"

            f"Field : {field}\n"

            f"Referenced Model : {target_model}\n"

            f"Referenced PK : {value}\n"

            f"Fixture : {fixture}"

        )

    # ------------------------------------------------------

    def _raise_if_errors(self) -> None:

        if not self.errors:
            return

        message = (

            "\n"

            "Fixture Integrity Validation Failed\n"

            "===================================\n\n"

            + "\n\n".join(self.errors)

        )

        raise CommandError(message)
