from django.db import models
from django.contrib.auth.models import AbstractUser

class Tipo(models.Model):
    TIPOS = (
        ('admin', 'Gerente Administrador'),
        ('gerente', 'Gerente'),
        ('general', 'Cajero General'),
        ('ie', 'Cajero de Importaciones y Exportaciones'),
        ('s', 'Cajero de Seguros'),
        ('d', 'Cajero Transacciones en Dolares'),
        ('vip', 'Cajero Clientes VIP'),
    )
    nombre = models.CharField(max_length=50, choices=TIPOS, unique=True)

    def __str__(self):
        return self.get_nombre_display()

# Create your models here.
class Usuario(AbstractUser):
    '''
    estos campos se heredan de AbastractUser
    username = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    '''
    rol = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=True)
    sucursal = models.ForeignKey('sucursales.Sucursal', on_delete=models.CASCADE, null=True)
    fecha_nacimiento = models.DateField(null=True)
    # TODO: Ponerle foto

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)