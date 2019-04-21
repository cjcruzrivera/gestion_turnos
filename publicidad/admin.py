from django.contrib import admin
from .models import Publicidad

class PublicidadAdmin(admin.ModelAdmin): 
    list_display = ["nombre"]

    class Meta:
        model = Publicidad

admin.site.register(Publicidad)
