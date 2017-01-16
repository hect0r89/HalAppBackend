from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from contacts.models import Contact, Phone, Email

URL = '/api/1.0/contacts/'
URL_PHONE = '/api/1.0/phones/'
URL_EMAIL = '/api/1.0/emails/'


class HalAppTest(APITestCase):
    def setUp(self):
        self.contact1 = Contact.objects.create(first_name='Contacto1', last_name='Contacto1')
        self.phone1_c1 = Phone.objects.create(number='numberP1C1', type=1, contact=self.contact1)
        self.email1_c1 = Email.objects.create(address='emailE1C1@gmail.com', type=1, contact=self.contact1)
        self.phone2_c1 = Phone.objects.create(number='numberP2C1', type=2, contact=self.contact1)
        self.email2_c1 = Email.objects.create(address='emailE2C1@gmail.com', type=2, contact=self.contact1)

        self.contact2 = Contact.objects.create(first_name='Contacto2', last_name='Contacto2')
        self.phone1_c2 = Phone.objects.create(number='numberP1C2', type=1, contact=self.contact2)
        self.email1_c2 = Email.objects.create(address='emailE1C2@gmail.com', type=1, contact=self.contact2)
        self.phone2_c2 = Phone.objects.create(number='numberP2C2', type=2, contact=self.contact2)
        self.email2_c2 = Email.objects.create(address='emailE2C2@gmail.com', type=2, contact=self.contact2)

    def test_list_contacts(self):
        response = self.client.get(URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_contact(self):
        response = self.client.post(URL, data={'first_name': "Cotacto 3",
                                               'last_name': 'Contacto 3'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_phone(self):
        response = self.client.post(URL_PHONE, data={'number': "numperP3C2",
                                               'type': 1, 'contact': self.contact2.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_email(self):
        response = self.client.post(URL_EMAIL, data={'address': "emailE3C2@gmail.com",
                                    'type': 1, 'contact': self.contact2.pk})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_contact(self):
        response = self.client.patch(URL+str(self.contact2.pk)+'/', data={'first_name': "Contacto2 Edited",
                                               'last_name': 'Contacto2 Edited'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_contact(self):
        response = self.client.delete(URL+str(self.contact2.pk)+'/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



