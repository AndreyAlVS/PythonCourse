import random
from django.core.management.base import BaseCommand
from myshop.models import OrderItem, Order, Product


class Command(BaseCommand):
    help = 'Populates the OrderItem model with test data'

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        products = Product.objects.all()

        for order in orders:
            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                quantity = random.randint(1, 10)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

        self.stdout.write(self.style.SUCCESS('OrderItems populated successfully!'))
