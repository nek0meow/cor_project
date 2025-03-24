from django import forms
from django.contrib.auth import get_user_model
from django.forms import DateInput

from web.models import Customer, Orders, Product, OrderItem

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data["password2"]:
            self.add_error("password", "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "customer_name",
            "customer_email",
            "customer_phone",
            "customer_address",
        )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ("order_date",)
        widgets = {
            "order_date": DateInput(attrs={"type": "date"}),  # Add a date widget
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ("quantity", "product")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("product_name", "product_desc", "product_price")  # , "category")


class CustomerFilterForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Поиск"}), required=False
    )


class ImportForm(forms.Form):
    file = forms.FileField()
