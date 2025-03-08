from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Prefetch
from django.urls import reverse

from web.models import User, Customer, Orders, Product, OrderItem
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout

from web.forms import RegistrationForm, AuthForm, CustomerForm, OrderForm, OrderItemForm, ProductForm, \
    CustomerFilterForm

User = get_user_model()

@login_required
def main_view(request):
    customers = Customer.objects.all()

    filter_form = CustomerFilterForm(request.GET)
    filter_form.is_valid()
    filters = filter_form.cleaned_data

    if filters['search']:
        customers = customers.filter(customer_name__icontains=filters['search'])
    count = customers.count()

    paginator = Paginator(customers, per_page=15)
    page_i = request.GET.get("page", 1)

    return render(request, 'web/main.html',
                  { "customers": paginator.get_page(page_i),
                    "filter_form": filter_form,
                    "count": count})

def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'])

            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
            print(form.cleaned_data)

    return render(request, 'web/registration.html',
                  { 'form': form, 'is_success': is_success })


def auth_view(request):
    form = AuthForm()
    if request.method == "POST":
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Введены неверные данные")
            else:
                login(request, user)
                return redirect("main")
    return render(request, 'web/auth.html',
                  { 'form': form} )


@login_required
def logout_view(request):
    logout(request)
    return redirect("main")


def _add_edit_temp(request, Cls, ClsForm, template, return_to, id=None):
    item = get_object_or_404(Cls, id=id) if id is not None else None
    is_edit = id is not None
    form = ClsForm(instance=item)
    if request.method == "POST":
        form = ClsForm(data=request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(return_to)
    return render(request, template, {'form': form, "is_edit": is_edit})


@login_required
def customer_add_edit_view(request, id=None):
    return _add_edit_temp(request, Customer, CustomerForm, "web/customer_add_edit.html", "main", id)


@login_required
def customer_delete_view(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect("main")


@login_required
def customer_orders_view(request, id):
    customer = get_object_or_404(Customer, id=id)
    orders = Orders.objects.filter(customer_id=id).prefetch_related(
        Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('product'))
    )

    # To send complex objects OrderItem + Order of that OrderItem
    orders_with_products = []

    for order in orders:
        # order_items = OrderItem.objects.filter(orders=order)
        order_items = order.orderitem_set.all()
        orders_with_products.append({
            'order': order,
            'products': order_items })



    paginator = Paginator(orders_with_products, per_page=10)
    page_i = request.GET.get("page", 1)

    return render(request, "web/customer_orders.html",
                  {"customer": customer,
                         "orders_with_products": paginator.get_page(page_i)})


@login_required
def order_add_edit_view(request, customer_id, id=None):
    customer = get_object_or_404(Customer, id=customer_id)
    order = get_object_or_404(Orders, id=id) if id is not None else None
    is_edit = id is not None
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(data=request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = customer
            order.save()
            return redirect('customer_orders', id=customer_id)

    return render(request, "web/order_add_edit.html", {'form': form, "is_edit": is_edit})


@login_required
def order_delete_view(request, id):
    order = get_object_or_404(Orders, id=id)
    customer_id = order.customer.id
    order.delete()
    return redirect("customer_orders", id=order.customer.id)


@login_required
def order_item_add_view(request, order_id):
    order = get_object_or_404(Orders, id=order_id)
    form = OrderItemForm()
    if request.method == "POST":
        form = OrderItemForm(data=request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.orders = order   # the reason we cannot replace that function with _add_edit_temp
            order_item.save()
            return redirect('customer_orders', id=order.customer.id)
    return render(request, 'web/order_item_add.html', {'form': form, 'order': order})


@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'web/products.html', {'products': products})


@login_required
def product_add_edit_view(request, id=None):
    product = get_object_or_404(Product, id=id) if id is not None else None
    is_edit = id is not None
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list page

    return render(request, 'web/product_add_edit.html', {'form': form, 'is_edit': is_edit})

@login_required
def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')  # Redirect to the product list page after deletion