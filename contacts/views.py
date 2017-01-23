from rest_framework import viewsets

from contacts.models import Contact, Phone
from contacts.serializers import ContactSerializer, PhoneSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer




class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
