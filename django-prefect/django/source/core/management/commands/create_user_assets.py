from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create user assets'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(
            'Successfully created user assets'))
