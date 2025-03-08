
from django.core.management import BaseCommand
from datetime import datetime

from web.models import Customer, Orders, Product, OrderItem


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(123)
        return 0
        customer = Customer.objects.first()
        products = Product.objects.all()

        for order_index in range(30):
            order = Orders.objects.create(
                order_date=datetime.now(),
                customer=customer
            )

            import random
            num_items = random.randint(1, 5)
            selected_products = random.sample(list(products), num_items)

            for product in selected_products:
                OrderItem.objects.create(
                    orders=order,
                    product=product,
                    quantity=random.randint(1, 10)
                )

