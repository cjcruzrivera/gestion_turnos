from django import forms
from .models import Publicidad

class PublicidadForm(forms.ModelForm):
    class Meta: 
        model = Publicidad

        fields = ['codigo', 'nombre', 'descripcion', 'imagen']
