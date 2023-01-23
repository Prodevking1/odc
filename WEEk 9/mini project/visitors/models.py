from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Visitor (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = PhoneNumberField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


    def __str__(self):
       return self.last_name + self.first_name
   
class Bedroom_type (models.Model):
   name = models.CharField(max_length=150)
   
   def __str__(self):
       return self.name
   
class Bedroom_size(models.Model):
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name

    
class Bedroom(models.Model):
    type_bedroom = models.ForeignKey(Bedroom_type, on_delete=models.CASCADE)
    size_bedroom = models.ForeignKey(Bedroom_size, on_delete=models.CASCADE)
    cost = models.FloatField()
    photo = models.ImageField(upload_to='img_chambre',default='img_chambre/default.jpg')
    date_created = models.DateField(auto_now_add=True)
    avaibility = models.BooleanField(default=True)
    
    def photoUrl(self ):
        try:
            url=self.photo.url 
        except : 
            url="img_chambre/default.jpg"
        return url
    
    def __str__(self):
        return self.type_bedroom

class Review(models.Model):

    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    review = models.TextField()
    


    def __str__(self):
        return str(self.visitor) + str(self.review)

class Simple_Reviews(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    
    def __str__(self):
        return str(self.name) + str(self.review)



class Book(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    bedroom = models.ForeignKey(Bedroom, on_delete=models.CASCADE, limit_choices_to={'avaibility': True})
    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs):
        bedroom = self.bedroom
        bedroom.avaibility = False
    
    
    def __str__(self):
         return self.visitor

