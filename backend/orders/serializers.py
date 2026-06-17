from rest_framework import serializers
from .models import Order
from accounts.serializers import AddressSerializer
from products.serializers import ProductSerializer, DeliveryPlaceSerializer


class OrderSerializer(serializers.ModelSerializer):
    # total = serializers.CharField(read_only=True)
    total = serializers.IntegerField(read_only=True)
    is_paid = serializers.BooleanField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ["id", "status", "is_paid", "product", "address", "city", "quantity", "total"]


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "is_paid", "total", "status"]


class OrderListSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)
    city = DeliveryPlaceSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "status", "is_paid", "product", "address", "quantity", "total", "city"]


class OrderCancelSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(read_only=True)
    is_paid = serializers.BooleanField(read_only=True)
    status = serializers.CharField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    address = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    city = DeliveryPlaceSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "status", "is_paid", "product", "address", "quantity", "total", "city"]
