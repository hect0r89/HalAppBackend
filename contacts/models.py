from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)


class Phone(models.Model):
    number = models.CharField(blank=False, null=False, max_length=13)
    type = models.IntegerField(blank=False, null=False)
    contact = models.ForeignKey(Contact, verbose_name="Contact", blank=False, null=False, related_name='phones')


class Email(models.Model):
    address = models.EmailField(blank=False, null=False)
    type = models.IntegerField(blank=False, null=False)
    contact = models.ForeignKey(Contact, verbose_name="Contact", blank=False, null=False, related_name='emails')
