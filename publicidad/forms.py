from django import forms
from .models import Publicidad

class PublicidadForm(forms.ModelForm):
    class Meta: 
        model = Publicidad

        fields = ['codigo', 'nombre', 'descripcion', 'imagen']

        widgets = {
            'codigo' : forms.TextInput(attrs={'class':'form-control','id':'codigo', 'placeholder': 'Ingrese el codigo de la publicidad'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre de la publicidad'}),            
            'descripcion' : forms.TextInput(attrs={'class':'form-control','id':'desc', 'placeholder': 'Ingrese la descripcion de la publicidad'}),            
        }
