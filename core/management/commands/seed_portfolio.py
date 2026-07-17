from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):

    help = "Seeds the entire portfolio."

    def handle(self, *args, **options):

        call_command("seed_hub")