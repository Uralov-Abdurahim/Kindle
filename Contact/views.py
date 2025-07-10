from django.shortcuts import render
from rest_framework import generics, permissions
from Contact.models import Contact
from Contact.serializers import ContactSerializers

class ContactCreateAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    permission_classes = [permissions.AllowAny]