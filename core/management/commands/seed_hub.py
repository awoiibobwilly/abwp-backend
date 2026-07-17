from pathlib import Path

from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):

    help = "Seeds the Knowledge Hub."

    FIXTURES = [

        "knowledge_hub",

        "knowledge_themes",

        "knowledge_tags",

        "organizations",

        "library_resources",

        "learning_videos",

        "practical_resources",

        "research_contributions",

        "search_configuration",

    ]

    def handle(self, *args, **options):

        self.stdout.write("")

        self.stdout.write(

            self.style.SUCCESS(

                "========== KNOWLEDGE HUB =========="

            )

        )

        self.stdout.write("")

        for fixture in self.FIXTURES:

            self.stdout.write(

                f"Loading {fixture}..."

            )

            call_command(

                "loaddata",

                fixture,

                verbosity=0,

            )

            self.stdout.write(

                self.style.SUCCESS(

                    f"✓ {fixture}"

                )

            )

        self.stdout.write("")

        self.stdout.write(

            self.style.SUCCESS(

                "Knowledge Hub seeded successfully."

            )

        )