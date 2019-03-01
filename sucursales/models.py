from django.db import models
from .validators import validateNumber, TYPE_CHOICES

# Create your models here.

class Sucursal(models.Model):
    codigo = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10, validators=[validateNumber])
    tipo = models.CharField(max_length=1, choices=TYPE_CHOICES)

