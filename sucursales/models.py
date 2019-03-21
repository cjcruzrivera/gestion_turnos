from django.db import models
from .validators import validateNumber, TYPE_CHOICES

# Create your models here.

class Sucursal(models.Model):
    """ Clase modelo Sucursal """
    codigo = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10, validators=[validateNumber])
    tipo = models.CharField(max_length=1, choices=TYPE_CHOICES)    
    actual = models.BooleanField(default=False)

    def get_actual(self):
        """ Metodo que retorna la sucursal del aplicativo actual """
        return self.objects.get(actual=True)

    class Meta:
        verbose_name = "sucursal"
        verbose_name_plural = "sucursales"
        ordering = ['codigo']

    def __str__(self):
        return self.nombre