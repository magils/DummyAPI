from django.core.management.base import BaseCommand
from django.db import transaction

from dummy_data_app.management.commands.news_seed_generator import generate_news_item
from dummy_data_app.models import News


class Command(BaseCommand):
    help = "Seed the DB with News objects"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count", type=int, default=25, help="Number of news to create"
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all existing News objects in the database.",
        )

    @transaction.atomic
    def handle(self, *args, count, clear, **options):
        if clear:
            News.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("All News objects deleted"))

        News.objects.bulk_create(News(**generate_news_item()) for _ in range(count))

        self.stdout.write(self.style.SUCCESS(f"Created {count} news object."))
