from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.serializers import CustomerSerializer, OrdersSerializer
from web.models import Customer, Orders, Product


@api_view(["GET"])
def main_view(request):
    return Response({"status": "OK"})


@api_view(["GET", "POST"])
def customer_view(request):
    if request.method == "POST":
        serializer = CustomerSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


class CustomerModelViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(ListModelMixin, GenericViewSet):
    queryset = Orders.objects.prefetch_related("order_items__product").all()
    serializer_class = OrdersSerializer


class ProductViewSet(ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = OrdersSerializer
