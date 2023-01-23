from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(AbstractUser):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'
    ROLE = [(ADMIN, 'Admin'), (CUSTOMER, 'Customer')]

    profil_photo = models.ImageField(upload_to='uploads_images/', verbose_name='Photo_user', null=True,blank=True, default='')
    role = models.CharField(max_length=50, choices=ROLE, verbose_name='Role', null=True, blank=True)
    phone = PhoneNumberField()

    def profile_photoURL(self):
        try:
            url =self.profile_photo.url
        except:
            url= ''
        return url

