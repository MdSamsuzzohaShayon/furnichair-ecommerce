from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .serializers import WishlistSerializer, WishlistUpdateSerializer
from .models import Wishlist
from accounts.mixins import StaffEditorPermissionMixin

# Create your views here.
class CreateWishlistView(CreateAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

class WishlistListView(StaffEditorPermissionMixin, ListAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

class UpdateWishlistView(StaffEditorPermissionMixin, UpdateAPIView):
    # Make sure Preview
    serializer_class = WishlistUpdateSerializer
    queryset = Wishlist.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.preview = True
