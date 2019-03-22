"""Models from clientes app"""
from django.db import models
from .validators import validateNumber

class Cliente(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    cedula = models.CharField(max_length=20, validators=[validateNumber])
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    vip = models.BooleanField(default=False)

    def get_actual(self):
        """ Metodo que retorna la sucursal del aplicativo actual """
        return self.objects.get(actual=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)

