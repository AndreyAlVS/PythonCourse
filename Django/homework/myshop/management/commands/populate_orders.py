import random
from django.core.management.base import BaseCommand
from myshop.models import Order, Product, Client


class Command(BaseCommand):
    help = 'Populates the Order model with test data'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Product.objects.all()

        for _ in range(50):
            order = Order.objects.create(
                total_price=random.randint(50, 200),
                order_number=f'Order-{random.randint(1000, 9999)}',
                client=random.choice(clients)
            )

            products_for_order = products.order_by('?')[:random.randint(1, 5)]
            order.products.set(products_for_order)

        self.stdout.write(self.style.SUCCESS('Orders populated successfully!'))
