import random
from django.core.management.base import BaseCommand
from myshop.models import Product
from faker import Faker


class Command(BaseCommand):
    help = 'Populates the Product model with test data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(100):
            product_name = fake.word()
            description = fake.text()

            price = round(random.uniform(10, 100), 2)
            quantity = random.randint(1, 100)

            add_date = fake.date_time_between(start_date="-5y", end_date="now", tzinfo=None)

            Product.objects.create(
                prod_name=product_name,
                description=description,
                price=price,
                quantity=quantity,
                add_date=add_date
            )

        self.stdout.write(self.style.SUCCESS('Products populated successfully!'))
