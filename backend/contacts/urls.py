from django.urls import path
from .views import CreateContactView, ContactListView, UpdateContactView

urlpatterns = [
    path('new/', CreateContactView.as_view(), name="contact-create"),
    path('list/', ContactListView.as_view(), name="contact-list"),
    path('update/<str:pk>/', UpdateContactView.as_view(), name="contact-update"),
]