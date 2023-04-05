from django.core.management import BaseCommand
from women.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.bulk_create(
            [Category(name=title) for title in ['Actress', 'Singer', 'Politician', 'Scientist']]
        )
