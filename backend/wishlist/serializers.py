from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    preview = serializers.BooleanField(read_only=True)
    class Meta:
        model = Wishlist
        fields = ['id', 'email', 'preview', 'created_at', 'updated_at']


class WishlistUpdateSerializer(serializers.ModelSerializer):
    preview = serializers.BooleanField(read_only=True)
    email = serializers.CharField(required=False,read_only=True)
    class Meta:
        model = Wishlist
        fields = ['id', 'email', 'preview', 'created_at', 'updated_at']