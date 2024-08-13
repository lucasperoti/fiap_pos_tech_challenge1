from rest_framework import serializers
from .customer_serializer import CustomerSerializer
from .product_serializer import ProductSerializer

class OrderSerializer(serializers.Serializer):
    customer = CustomerSerializer()
    products = ProductSerializer(many=True)
    status = serializers.CharField(max_length=50, default='RECEIVED')