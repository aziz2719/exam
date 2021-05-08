from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Order, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer
from .permissions import IsOrderUserOrReadOnly


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsOrderUserOrReadOnly) 
