from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from contacts.models import Contact, Phone
from contacts.serializers import PhoneSerializer

URL = '/api/1.0/contacts/'
URL_PHONE = '/api/1.0/phones/'


class HalAppTest(APITestCase):
    def setUp(self):
        self.phonec1 = Phone.objects.create(numero='111111111', tipo=1)
        self.contact1 = Contact.objects.create(nombre='Contacto1', apellidos='Contacto1', telefono=self.phonec1, color=1)

        self.phonec2 = Phone.objects.create(numero='222222222', tipo=1)
        self.contact2 = Contact.objects.create(nombre='Contacto2', apellidos='Contacto2', telefono=self.phonec2, color =1)

    def test_list_contacts(self):
        response = self.client.get(URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_contact_with_phone(self):
        response = self.client.post(URL, data={'telefono': PhoneSerializer(self.phonec1).data,'nombre': "Cotacto 3",'apellidos': 'Contacto 3', 'direccion': 'address3', 'email': 'email3@user.com',  'color':1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_phone(self):
        response = self.client.post(URL_PHONE, data={'numero': "numperP3C2", 'tipo': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_contact(self):
        response = self.client.patch(URL+str(self.contact2.pk)+'/', data={'nombre': "Contacto2 Edited",
                                               'apellidos': 'Contacto2 Edited'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_contact(self):
        response = self.client.delete(URL+str(self.contact2.pk)+'/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



