from django.db import models


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=256)
    supplier_contact = models.CharField(max_length=256)
    supplier_address = models.CharField(max_length=256)


class Category(models.Model):
    category_name = models.CharField(max_length=256)
    category_desc = models.CharField(max_length=256)


class Product(models.Model):
    product_name = models.CharField(max_length=256)
    product_desc = models.CharField(max_length=256)
    product_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Shipment(models.Model):
    shipment_address = models.CharField(max_length=256)
    quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Customer(models.Model):
    customer_name = models.CharField(max_length=256)
    customer_email = models.CharField(max_length=256)
    customer_phone = models.CharField(max_length=256)
    customer_address = models.CharField(max_length=256)


class Orders(models.Model):
    order_date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderItem(models.Model):
    quantity = models.FloatField()
    product = models.ForeignKey(Product)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)


class Payment(models.Model):
    payment_date = models.DateTimeField()
    amount = models.FloatField()
    payment_method = models.CharField(32)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
