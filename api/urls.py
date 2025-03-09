from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from api.views import main_view, customer_view, CustomerModelViewSet, OrderViewSet, ProductViewSet

router = SimpleRouter()
router.register("customers", CustomerModelViewSet, basename="customers")
router.register("orders", OrderViewSet, basename="orders")
router.register("products", ProductViewSet, basename="products")

urlpatterns = [path("", main_view), path("token/", obtain_auth_token), *router.urls]