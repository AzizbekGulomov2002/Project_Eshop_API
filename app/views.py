from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .serializers import *
from app.models import *
from rest_framework import viewsets


class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    
class OrderModelViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
class OrderItemModelViewSet(viewsets.ModelViewSet):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer
    
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer