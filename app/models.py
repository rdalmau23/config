from django.db import models

# Create your models here.
from django.db import models

class Usuari(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
