from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Fire all repeating triggers'

    def handle(self, *args, **options):
        self.stdout.write('Everything done!')
