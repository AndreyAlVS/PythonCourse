from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['id']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
