from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, customer_add_edit_view, \
    customer_delete_view, order_add_edit_view, order_delete_view, customer_orders_view, order_item_add_view, \
    product_list_view, product_add_edit_view, product_delete_view, analytics_view, import_view, stat_view

urlpatterns = [
    path('', main_view, name='main'),
    path('registration/', registration_view, name='registration'),
    path('auth/', auth_view, name='auth'),
    path('analytics/', analytics_view, name='analytics'),
    path('import/', import_view, name='import'),
    path('logout/', logout_view, name='logout'),
    path('stat/', stat_view, name='stat'),
    path('customer/add/', customer_add_edit_view, name='customer_add'),
    path('customer/edit/<int:id>/', customer_add_edit_view, name='customer_edit'),
    path('customer/delete/<int:id>/', customer_delete_view, name='customer_delete'),
    path('customer/<int:id>/orders/', customer_orders_view, name='customer_orders'),
    path('order/add/<int:customer_id>/', order_add_edit_view, name='order_add'),
    path('order/edit/<int:customer_id>/<int:id>/', order_add_edit_view, name='order_edit'),
    path('order/delete/<int:id>/', order_delete_view, name='order_delete'),
    path('order/<int:order_id>/add_item/', order_item_add_view, name='order_item_add'),
    path('products/', product_list_view, name='product_list'),
    path('product/add/', product_add_edit_view, name='product_add'),
    path('product/edit/<int:id>/', product_add_edit_view, name='product_edit'),
    path('product/delete/<int:id>/', product_delete_view, name='product_delete'),
]
