from django.db import models

# Create your models here.
class Client(models.Model):
    matricule = models.CharField(max_length=5, unique=True)
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=200)
    tel = models.CharField(max_length=10, )

    def __str__(self):
        return f"{self.prenoms} {self.nom}"