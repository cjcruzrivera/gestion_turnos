# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.db import models
from clientes.models import Cliente
from sucursales.models import Sucursal
from servicio.models import Servicio
from usuarios.models import Usuario
# Create your models here.

class Ciudad (models.Model): 
    name = models.CharField(_('City Name'),max_length = 30)
    class Meta:
        verbose_name = _('ciudad')
        verbose_name_plural = _('ciudades')


    
class Turno (models.Model): 

    turno = models.CharField(max_length=20, unique=True) 
    hora_solicitud = models.DateTimeField(editable=False)
    hora_inicio_turno = models.DateTimeField(null=True)
    hora_fin_turno = models.DateTimeField(null=True)
    isAtendido = models.BooleanField(default=False)
    
    servicio = models.ForeignKey(Servicio, on_delete= models.CASCADE, null=True)
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete= models.CASCADE, null =True )
    cajero = models.ForeignKey(Usuario, on_delete= models.CASCADE, null =True) 

    def save(self, *args, **kwargs):
        if not self.id:
            self.hora_solicitud = timezone.now()
        
        return super(Turno, self).save(*args, **kwargs)
