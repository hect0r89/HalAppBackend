from django.db import models


# Create your models here.
from telefonos.models import Telefono


class Contacto(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    phone = models.ManyToManyField(Telefono, blank=False)


