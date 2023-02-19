from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    phone_number = PhoneNumberField()

    address = models.CharField(max_length=200, null=True)
