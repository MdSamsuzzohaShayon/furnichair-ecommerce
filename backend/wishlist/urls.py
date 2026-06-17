from django.urls import path
from .views import CreateWishlistView, WishlistListView, UpdateWishlistView

urlpatterns = [
    path('new/', CreateWishlistView.as_view(), name="wishlist-create"),
    path('list/', WishlistListView.as_view(), name="wishlist-list"),
    path('update/<str:pk>/', UpdateWishlistView.as_view(), name="wishlist-update"),
]