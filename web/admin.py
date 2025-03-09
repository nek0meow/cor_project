from django.contrib import admin

from web.models import Customer, Orders


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "customer_email", "customer_phone", "customer_address")
    search_fields = ("id", "customer_name", "customer_email")
    ordering = ("-id",)


class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "order_date")
    search_fields = ("id", "order_date")
    ordering = ("-order_date",)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Orders, OrdersAdmin)