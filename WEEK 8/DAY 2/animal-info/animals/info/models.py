from django.db import models

class Family(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    legs = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
