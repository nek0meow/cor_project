# Generated by Django 5.1.4 on 2025-01-03 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=256)),
                ("category_desc", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.CharField(max_length=256)),
                ("customer_email", models.CharField(max_length=256)),
                ("customer_phone", models.CharField(max_length=256)),
                ("customer_address", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("supplier_name", models.CharField(max_length=256)),
                ("supplier_contact", models.CharField(max_length=256)),
                ("supplier_address", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_date", models.DateTimeField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.customer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_date", models.DateTimeField()),
                ("amount", models.FloatField()),
                ("payment_method", models.CharField(max_length=32)),
                (
                    "orders",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.orders"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=256)),
                ("product_desc", models.CharField(max_length=256)),
                ("product_price", models.FloatField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.category"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.FloatField()),
                (
                    "orders",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.orders"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Shipment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("shipment_address", models.CharField(max_length=256)),
                ("quantity", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.product"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.supplier"
                    ),
                ),
            ],
        ),
    ]
