from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    preview = serializers.BooleanField(read_only=True)
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message', 'preview', 'created_at', 'updated_at']

class ContactUpdateSerializer(serializers.ModelSerializer):
    preview = serializers.BooleanField(read_only=True)
    name = serializers.CharField(required=False, read_only=True)
    email = serializers.CharField(required=False, read_only=True)
    message = serializers.CharField(required=False, read_only=True)
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message', 'preview', 'created_at', 'updated_at']