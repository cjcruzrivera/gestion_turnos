# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from cliente.models import Cliente
from sucursales.models import Sucursal
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Ciudad (models.Model): 
    name = models.CharField(_('City Name'),max_length = 30)
    class Meta:
        verbose_name = _('ciudad')
        verbose_name_plural = _('ciudades')


    
class Turno (models.Model): 

    REGISTRO = 'REG'
    GENERAL= 'GEN'
    IMPO_EXPO= 'IMPO'
    SEGUROS= 'SEG' 
    DOLARES= 'DOL'
    #VIP = 'VIP'

    OPCIONES_TIPO_TURNO = (
        (REGISTRO, 'Registro'),
        (GENERAL, 'General'),
        (IMPO_EXPO, 'Importaciones y Exportaciones'),
        (SEGUROS, 'Seguros'),
        (DOLARES, 'Dólares')
       # (VIP, 'Clientes VIP') 
    )

    turno = models.AutoField (max_length = 20 , primary_key= True,  ) 
    tipo_turno= models.IntegerField(null= True, choices= OPCIONES_TIPO_TURNO)

    isAtendido = models.BooleanField (default= False)
    
    
    #cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete= models.CASCADE, null =True ) 
