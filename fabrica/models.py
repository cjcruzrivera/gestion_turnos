from django.db import models
from sucursales.models import Sucursal

import factory
import factory.django

class FabricaSucursalPrincipal(factory.django.DjangoModelFactory):
	class Meta:
		model = Sucursal
	codigo = factory.Faker('iban')
	nombre = factory.Faker('name')
	direccion = factory.Faker('address')
	localidad = factory.Faker('city')
	telefono = factory.Faker('phone_number')
	tipo = 'P'
	actual = True

class FabricaSucursalGeneral(factory.django.DjangoModelFactory):
	class Meta:
		model = Sucursal
	codigo = factory.Faker('iban')
	nombre = factory.Faker('name')
	direccion = factory.Faker('address')
	localidad = factory.Faker('city')
	telefono = factory.Faker('phone_number')
	tipo = 'G'
	actual = True


# Create your models here.
