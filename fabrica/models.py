from django.db import models
from sucursales.models import Sucursal
from clientes.models import Cliente

import factory
import factory.django

class FabricaSucursalPrincipal(factory.django.DjangoModelFactory):
	class Meta:
		model = Sucursal
	codigo = factory.Faker('pyint')
	nombre = factory.Faker('company')
	direccion = factory.Faker('address')
	localidad = factory.Faker('city')
	telefono = factory.Faker('phone_number')
	tipo = 'P'
	actual = True

class FabricaSucursalGeneral(factory.django.DjangoModelFactory):
	class Meta:
		model = Sucursal
	codigo = factory.Faker('pyint')
	nombre = factory.Faker('company')
	direccion = factory.Faker('address')
	localidad = factory.Faker('city')
	telefono = factory.Faker('phone_number')
	tipo = 'G'
	actual = True

class FabricaClientes(factory.django.DjangoModelFactory):
	class Meta:
		model = Cliente
	cedula = factory.Faker('ean8')
	nombre = factory.Faker('first_name')
	apellidos = factory.Faker('last_name')
	vip = factory.Faker('pybool')

# Create your models here.
