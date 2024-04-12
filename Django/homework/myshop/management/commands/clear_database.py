# myapp/management/commands/clear_database.py
from django.core.management.base import BaseCommand
from myshop.models import Product, Order, OrderItem


class Command(BaseCommand):
    help = 'Clears all data from the database'

    def handle(self, *args, **kwargs):
        # Очистка всех записей из модели Product
        Product.objects.all().delete()
        Order.objects.all().delete()
        OrderItem.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Database cleared successfully!'))
