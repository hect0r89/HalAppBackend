from django.db import models

TIPO = (
    ('C', 'Casa'),
    ('M', 'Móvil'),
    ('T', 'Trabajo'),

)


# Create your models here.
class Telefono(models.Model):
    number = models.IntegerField(blank=False, null=False)
    type = models.CharField(max_length=1, choices=TIPO, default='C')
