from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=256, verbose_name="Название")
    supplier_contact = models.CharField(max_length=256, verbose_name="Контактные данные")
    supplier_address = models.CharField(max_length=256, verbose_name="Адрес")


class Category(models.Model):
    category_name = models.CharField(max_length=256, verbose_name="Название категории")
    category_desc = models.CharField(max_length=256, verbose_name="Описание")


class Product(models.Model):
    product_name = models.CharField(max_length=256, verbose_name="Наименование")
    product_desc = models.CharField(max_length=256, null=True, verbose_name="Описание")
    product_price = models.FloatField(verbose_name="Цена")
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.product_name


class Shipment(models.Model):
    shipment_address = models.CharField(max_length=256, verbose_name="Адрес")
    quantity = models.IntegerField(verbose_name="Количество")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Поставщик")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")


class Customer(models.Model):
    customer_name = models.CharField(max_length=256, verbose_name="Имя")
    customer_email = models.CharField(max_length=256, verbose_name="Email")
    customer_phone = models.CharField(max_length=256, verbose_name="Телефон")
    customer_address = models.CharField(max_length=256, null=True, verbose_name="Адрес")

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


class Orders(models.Model):
    order_date = models.DateTimeField(verbose_name="Дата")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Клиент")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    quantity = models.FloatField(verbose_name="Количество")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name="Заказ", related_name='order_items')


class Payment(models.Model):
    payment_date = models.DateTimeField(verbose_name="Дата")
    amount = models.FloatField(verbose_name="Количество (руб.)")
    payment_method = models.CharField(max_length=32, verbose_name="Метод оплаты")
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name="Заказ")
