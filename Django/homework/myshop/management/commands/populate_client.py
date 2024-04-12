from faker import Faker
from django.core.management.base import BaseCommand
from myshop.models import Client


class Command(BaseCommand):
    help = 'Populates the Client model with test data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Генерация 50 клиентов
        for _ in range(50):
            # Создание клиента
            Client.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
            )

        self.stdout.write(self.style.SUCCESS('Clients populated successfully!'))
