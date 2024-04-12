from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = "Generate fake authors and posts."
    def handle(self, *args, **kwargs):
        self.stdout.write('Populating the database with random data...')

        num_orders = 50

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', email=f'mail{i}@mail.ru')
            author.save()
        for j in range(1, count + 1):
            post = Post(
                title=f'Title{j}',
                content=f'Text from{author.name}  #{j} is bla bla bla many long text',
                author=author
            )
            post.save()
