from django.db import models
from usuarios.models import Tipo

# Create your models here.
class Servicio(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.nombre
