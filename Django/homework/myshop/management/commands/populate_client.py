# myapp/management/commands/populate_clients.py
import random
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
                name=fake.name(),  # Генерация случайного имени
                email=fake.email(),  # Генерация случайного email
                phone_number=fake.phone_number(),  # Генерация случайного номера телефона
                address=fake.address(),  # Генерация случайного адреса
            )

        self.stdout.write(self.style.SUCCESS('Clients populated successfully!'))
