# myapp/management/commands/populate_order_items.py
import random
from django.core.management.base import BaseCommand
from myshop.models import OrderItem, Order, Product


class Command(BaseCommand):
    help = 'Populates the OrderItem model with test data'

    def handle(self, *args, **kwargs):
        # Получение всех заказов и всех товаров
        orders = Order.objects.all()
        products = Product.objects.all()

        # Генерация OrderItem для каждого заказа
        for order in orders:
            # Генерация случайного количества OrderItem для каждого заказа
            for _ in range(random.randint(1, 5)):
                # Выбор случайного товара
                product = random.choice(products)
                # Генерация случайного количества товара
                quantity = random.randint(1, 10)
                # Создание OrderItem
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

        self.stdout.write(self.style.SUCCESS('OrderItems populated successfully!'))
