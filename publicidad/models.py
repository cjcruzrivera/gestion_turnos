from django.db import models

class Publicidad(models.Model):
    codigo = models.CharField(max_length = 15, primary_key = True)
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 300)
    imagen = models.ImageField(upload_to = 'images/publicidad/')
'''
    @staticmethod
    def get_publicidad():
        try:
            publicidad = Publicidad.objects.all()
            return publicidad
        except Publicidad.DoesNotExist:
            return None
'''
def __str__(self):
    return self.nombre
        
