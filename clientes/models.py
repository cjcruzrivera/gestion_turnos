"""Models from clientes app"""
from django.db import models
from .validators import validateNumber

class Cliente(models.Model):
    cedula = models.CharField(max_length=20, validators=[validateNumber])
    nombre = models.CharField(max_length=50, null=True)
    apellidos = models.CharField(max_length=50, null=True)
    vip = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)

