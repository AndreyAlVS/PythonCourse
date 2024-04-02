from django.core.management.base import BaseCommand
from myshop.models import Client


# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(
            name='Bob',
            email='bob@example.com',
            phone_number='123456789',
            address='Bob street, 1',
            reg_date=True)
        client.save()
        self.stdout.write(f'{client}')
