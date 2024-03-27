from django.core.management.base import BaseCommand
# import os
# import sys
# sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from Django.lectures.myapp2.models import User
# from myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        # user = User(name='Neo', email='neo@example.com', password='secret',age=58)
        user = User(name='Jack', email='captain@example.com', password='secret',age=60)
        ...
        user.save()
        self.stdout.write(f'{user}')
