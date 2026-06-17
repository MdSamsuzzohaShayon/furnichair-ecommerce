from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .serializers import ContactSerializer, ContactUpdateSerializer
from .models import Contact
from accounts.mixins import StaffEditorPermissionMixin

# Create your views here.
class CreateContactView(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class ContactListView(StaffEditorPermissionMixin, ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class UpdateContactView(StaffEditorPermissionMixin, UpdateAPIView):
    # Make sure Preview
    serializer_class = ContactUpdateSerializer
    queryset = Contact.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save(preview=True)
        # instance.preview = True
