from django.core.management import BaseCommand
from django.utils import timezone

from web.models import Customer, Orders, Product, OrderItem
import random

# Requires already existing products, can make that on the website
class Command(BaseCommand):
    def handle(self, *args, **options):
        customer = Customer.objects.first()
        products = list(Product.objects.all())
        if len(products) < 2:
            print("make at least 2 products first")
            return

        orders_to_create = []
        order_items_to_create = []

        for order_index in range(30):
            order = Orders(
                order_date=timezone.now(),
                customer=customer
            )
            orders_to_create.append(order)

        created_orders = Orders.objects.bulk_create(orders_to_create)

        for order in created_orders:
            num_items = random.randint(1, len(products))
            selected_products = random.sample(products, num_items)

            for product in selected_products:

                order_item = OrderItem(
                    orders=order,
                    product=product,
                    quantity=random.randint(1, 10)
                )
                order_items_to_create.append(order_item)

        OrderItem.objects.bulk_create(order_items_to_create)

