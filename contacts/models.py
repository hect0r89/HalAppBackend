from django.db import models

# Create your models here.


class Phone(models.Model):
    numero = models.CharField(blank=False, null=False, max_length=13)
    tipo = models.IntegerField(blank=False, null=False)


class Contact(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=50)
    apellidos = models.CharField(blank=True, null=True, max_length=50)
    direccion = models.CharField(blank=True, null=True, max_length=50)
    correo = models.EmailField(blank=True, null=True, max_length=50)
    telefono = models.ForeignKey(Phone, verbose_name="Telefono", null=True, blank=True)
    color = models.IntegerField(blank=False, null=False)


