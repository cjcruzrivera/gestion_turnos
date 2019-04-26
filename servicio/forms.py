from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio

		fields = ['codigo','nombre','tipo']

		widgets = {
            'codigo' : forms.TextInput(attrs={'class':'form-control','id':'codigo', 'placeholder': 'Ingrese el codigo del Servicio'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control','id':'nombre', 'placeholder': 'Ingrese el nombre del Servicio'}),
            'tipo' : forms.Select(attrs={'class':'form-control','id':'tipo', 'placeholder': 'Seleccione el tipo de Servicio'}),
        }