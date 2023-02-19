from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=200, null=True)
    image = models.URLField()

    def __str__(self):
        return self.nom


class Todo(models.Model):
    title = models.CharField(max_length=200, null=True)
    details = models.TextField()
    has_been_done = models.BooleanField()
    date_creation = models.DateField()
    date_completion = models.DateField()
    date_end = models.DateField()
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
